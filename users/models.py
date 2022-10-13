from django.db import models
from django.contrib.auth.models import User, AbstractUser
# Create your models here.


# class PersonManagerInactive(models.Manager):

#     def get_queryset(self):
#         return super().get_queryset().filter(is_active=False)


# class PersonManagerActive(models.Manager):

#     def get_queryset(self):
#         return super(PersonManagerActive, self).get_queryset().filter(is_active=True)


# TypeError: Person cannot proxy the swapped model 'user.NewUser'.
# class Person(User):

#     inactive = PersonManagerInactive()
#     active = PersonManagerActive()

#     class Meta:
#         proxy = True
#         ordering = ['first_name']

#     @classmethod
#     def count_all(cls,):
#         return cls.objects.all().count()
    
#     def check_active(self):
#         return "You are Active" if self.is_active else "You are not active"

#     def __str__(self) -> str:
#         return self.first_name


class NewUser(AbstractUser):

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    user_id = models.BigAutoField(primary_key=True)
    age = models.IntegerField(null=True,blank=True)
    nickname = models.CharField(null=True,blank=True, max_length=50)
    username = models.CharField(max_length=250)
    email = models.EmailField(unique=True)

    class Meta:
        indexes = [models.Index(fields=['username', 'email'])]