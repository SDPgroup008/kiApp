from django.db import models
from django.contrib.auth.models import User


class TodoAppModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    due_datetime = models.DateTimeField(blank=True, auto_now=False)
    completed = models.BooleanField(default=False)
    email_notification_sent = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.title
