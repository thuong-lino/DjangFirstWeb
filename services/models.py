from django.db import models


# Create your models here.

class Services(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=126)
    status = models.BooleanField(default=False, help_text='PUBLISHED OR NOT')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)