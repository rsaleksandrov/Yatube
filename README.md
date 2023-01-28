# Yatube

## Настройка
- Важно! Проект создан с использованием Python версии 3.10
- Установка модулей
```pip install -r requirements.txt```
- Сделать миграции 

```
python managе makemigrations
python manage migrate
```

- Создать суперпользователя 
 
```python manage createsuperuser```

- Запустить сервер

```python manage runserver```

- Зайти на страницу администрирования ```/admin/auth/group/``` и создать группу ```can_upload_file``` с правами:

```
filebrowser|Менеджер файлов|Can add FileBrowser
filebrowser|Менеджер файлов|Can change FileBrowser
filebrowser|Менеджер файлов|Can delete FileBrowser
filebrowser|Менеджер файлов|Can view FileBrowser
```
(Без указания этой группы с правами не будет работать загрузка файлов в редакторе постов и комментариев)
