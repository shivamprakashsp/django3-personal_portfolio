from django.db import models

# Create your models here.

class Blogs(models.Model):
    blog_title = models.CharField(max_length=264)
    blog_descritions = models.CharField(max_length=264)
    blog_date = models.DateField()
    blog_url = models.URLField(blank=True)
    
    def __str__(self):
        return self.blog_title
