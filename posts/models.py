from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.
class Post(models.Model):
    content = models.TextField()
    # image = models.ImageField(blank=True)
    
    def __ste__(self):
        return self.content
        
class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    file = ProcessedImageField(
                upload_to='posts/images',							
                processors=[ResizeToFill(600, 600)],
                )