from django.db import models

# Create your models here.

class book_tabel(models.Model):
    Name = models.CharField (max_length=55)
    Email = models.EmailField (max_length=55)
    Number = models.IntegerField ()
    Date = models.DateField ()
    Person = models.IntegerField ()
    start_time = models.CharField (max_length=55)
    end_time = models.CharField (max_length=55)
    instructions = models.CharField (max_length=2000)
