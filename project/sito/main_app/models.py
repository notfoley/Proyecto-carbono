from django.db import models

class main_app(models.Model):
    field1 = models.CharField(max_length=255)
    field2 = models.CharField(max_length=255)
