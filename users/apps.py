from django.apps import AppConfig
from django.contrib.auth import get_user_model

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def sayhi(self):
        print('hello world')

    def ready(self):
        User = get_user_model()
        User.sayhi = self.sayhi
