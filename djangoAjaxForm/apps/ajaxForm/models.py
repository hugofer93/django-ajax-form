from django.db import models
from django.urls import reverse

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    nickname = models.CharField(max_length=20, unique=True)
    birthDay = models.DateField(blank=True, null=True)

    def __str__(self):
        return '{} {} - {}'.format(self.name, self.surname, self.nickname)

    def get_absolute_url(self):
        return reverse('ajaxform:detail', kwargs={'id': self.id})