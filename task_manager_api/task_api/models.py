from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    def __str__(self):
        return self.title + " - " + self.user.username