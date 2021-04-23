from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=264)
    image = models.ImageField(upload_to = 'portfolio/images/')
    Descriptions = models.CharField(max_length=264)
    url = models.URLField(blank=True)
    
    def __str__(self):
        return self.title

