from django.db import models

class User(models.Model):
    user = models.CharField(max_length=40)
    name = models.CharField(max_length=40)
    rol= models.CharField(max_length=40)
    email = models.EmailField()
    avatar = models.CharField(max_length= 250)


class Movie(models.Model):
    title =  models.CharField(max_length=40)
    img = models.CharField(max_length= 250)
    description = models.CharField(max_length=200)
    tag = models.CharField(max_length=40)


class Review(models.Model):
    title =  models.CharField(max_length=40)
    img = models.CharField(max_length= 250)
    text = models.CharField(max_length=200)
    user = models.CharField(max_length=40)
    date = models.DateField()
    stars = models.IntegerField()

