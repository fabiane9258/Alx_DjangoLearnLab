from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager  # for tags

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)  # required field
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = TaggableManager()  # allows tagging

    def publish(self):
        """Set published_date to now and save"""
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
