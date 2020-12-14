from django.db import models

# Create your models here.
class Message(models.Model):
    """A model to store the messages sent by visitors"""
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    subject = models.CharField(max_length=100)    
    message = models.CharField(max_length=2000)
    date_sent = models.DateTimeField(auto_now_add=True)