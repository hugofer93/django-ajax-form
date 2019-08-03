from django.db import models
from django.urls import reverse


class Person(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    nickname = models.CharField(max_length=20, unique=True)
    birthdate = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'{self.name} {self.surname} - {self.nickname}'

    def get_absolute_url(self):
        return reverse('myapp:detail', kwargs={'id': self.id})