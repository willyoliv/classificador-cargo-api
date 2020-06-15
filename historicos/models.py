from django.db import models

# Create your models here.
class Historico(models.Model):
    historico = models.TextField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    
    
    def __str__(self):
        return self.historico