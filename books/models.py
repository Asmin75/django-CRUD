from django.db import models

# Create your models here.
from django.urls import reverse


class Book(models.Model):
    name = models.CharField(max_length=200)
    pages = models.IntegerField()

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse('book_edit', kwargs={'pk':self.pk})