from django.db import models

# Create your models here.



class Autor(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=50)



class Publisher(models.Model):
    name = models.CharField(max_length=70)



class Book(models.Model):

    title = models.CharField(max_length=100)
    author = models.ForeignKey(Autor)
    isbn = models.CharField(max_length=17)
    publisher = models.ForeignKey(Publisher)
