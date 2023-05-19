from django.db import models
class IstaLog(models.Model):
    login =models.CharField('Login', max_length=50)  
    password =models.CharField('password', max_length=50)      

    def __str__(self):
         return self.login
    
    class Meta:
        verbose_name="Инста логин"
        verbose_name_plural="Инста логины"

        
# Create your models here.
