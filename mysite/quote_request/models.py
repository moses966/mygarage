from django.db import models

# model to store quote requests
class QuoteRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    industry = models.CharField(max_length=100)
    message = models.TextField()