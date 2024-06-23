from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    


    def __str__(self):
        return f'{self.user.username} - {self.created.strftime("%Y-%m-%d %H:%M")}'
# Create your models here.
