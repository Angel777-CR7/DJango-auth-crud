from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):
                  #Texto cortos
    title = models.CharField(max_length=100) 
                         #Texto largos
    description = models.TextField(blank=True) 
                    #Fechas
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null = True, blank = True)
    important = models.BooleanField(default=False)
                 #enlazar tabla
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title + '- by ' + self.user.username