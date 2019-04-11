from django.db import models

# Create your models here.
class Post(models.Model):
    content = models.TextField()
    
    def __ste__(self):
        return self.content