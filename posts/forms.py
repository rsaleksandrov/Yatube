from django import forms
from django.core.exceptions import ValidationError
from pytils.translit import slugify

from posts.models import Comment, Group, Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text', 'group']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['title', 'slug', 'description']

    def clean_slug(self):
        """Обрабатывает случай, если slug не уникален."""
        cleaned_data = super().clean()
        slug = cleaned_data['slug']
        if not slug:
            title = cleaned_data['title']
            slug = slugify(title)[:100]
        if Group.objects.filter(slug=slug).exists():
            raise ValidationError(f'Адрес "{slug}" уже существует, '
                                  'придумайте уникальное значение')
        return slug
