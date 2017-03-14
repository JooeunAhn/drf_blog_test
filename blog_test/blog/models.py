from django.db import models
from django.conf import settings

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="posts") 
    title = models.CharField(max_length=50, blank=True)
    content = models.CharField(max_length=1000, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

