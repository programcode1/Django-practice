from django.db import models

# Create your models here.
class onlineDictionary(models.Model):
    letter = models.CharField(max_length=30)
    word = models.CharField(max_length=30)
    defination = models.CharField(max_length=30)
    exmaple = models.CharField(max_length=30)


    def __str__(self):
        return f"{self.letter}, {self.word} ,{self.defination} , {self.exmaple}"