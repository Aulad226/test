from django.db import models

# Create your models here.
class Producer(models.Model):
    name=models.CharField(max_length=30)
    city=models.CharField(max_length=30)
    state=models.CharField(max_length=40)
    country=models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Artist(models.Model):
    name=models.CharField(max_length=30)
    age=models.DateField()
    country=models.CharField(max_length=30)

    def __str__(self):
        return self.name + ' ' + str(self.age)

class Song(models.Model):
    title=models.CharField(max_length=30)
    year=models.DateField()
    artist=models.ManyToManyField(Artist)
    producer=models.ForeignKey(Producer)
    def __str__(self):
        return self.title
