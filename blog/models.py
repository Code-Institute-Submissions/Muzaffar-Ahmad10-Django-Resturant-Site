from django.db import models

# Create your models here.

class book_tabel(models.Model):
    Name = models.CharField (max_length=55)
    Email = models.EmailField (max_length=55)
    Number = models.IntegerField (max_length=25)
    Date = models.DateField ()
    Person = models.IntegerField (max_length=2)