from django.db import models

class Note(models.Model):
    subject = models.CharField(max_length=75)
    text = models.TextField(max_length=300)