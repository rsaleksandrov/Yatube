from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group

from posts.models import User


class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')

    def save(self, *args, **kwargs):
        new_user = super().save(*args, **kwargs)
        groups = Group.objects.filter(name='can_upload_file')
        new_user.groups.add(groups[0])
        new_user.is_staff = True
        new_user.save()
        return new_user
