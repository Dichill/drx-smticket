from django.db import models

# Create your models here.

class Account(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username

class MovieResult(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    link = models.CharField(max_length=2083)

    def __str__(self):
        return self.title

class EventResult(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    link = models.CharField(max_length=2083)
    image = models.CharField(max_length=2083)

    def __str__(self):
        return self.title
    

class SMVenuesResult(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    link = models.CharField(max_length=2083)
    image = models.CharField(max_length=2083)

    def __str__(self):
        return self.title

class OtherVenuesResult(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    link = models.CharField(max_length=2083)
    image = models.CharField(max_length=2083)

    def __str__(self):
        return self.title


class AttractionsResult(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    link = models.CharField(max_length=2083)
    image = models.CharField(max_length=2083)

    def __str__(self):
        return self.title

