from django.db import models

# Create your models here.

class CredentialOauth(models.Model):
    userref = models.ForeignKey(models.Model.User)
    token = models.CharField()