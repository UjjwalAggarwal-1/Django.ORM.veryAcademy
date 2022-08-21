from django.db import models
from django.contrib.auth.admin import User
# Create your models here.


class PersonManagerInactive(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(is_active=False)


class PersonManagerActive(models.Manager):

    def get_queryset(self):
        return super(PersonManagerActive, self).get_queryset().filter(is_active=True)



class Person(User):

    inactive = PersonManagerInactive()
    active = PersonManagerActive()

    class Meta:
        proxy = True
        ordering = ['first_name']

    @classmethod
    def count_all(cls,):
        return cls.objects.all().count()
    
    def check_active(self):
        return "You are Active" if self.is_active else "You are not active"

    def __str__(self) -> str:
        return self.first_name