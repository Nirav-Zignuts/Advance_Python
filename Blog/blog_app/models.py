from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)
    def __str__(self):
        return self.title + " - " + self.user.username
