from django.db import models

class Musician(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 15)
    instrument_type = models.CharField(max_length = 50,null = True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Album(models.Model):
    name = models.CharField(max_length = 100)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE,related_name='albums')
    release_date = models.DateField()
    rating = models.IntegerField()
    
    def __str__(self):
        return self.name