from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=255)
    img = models.URLField()
    summary = models.TextField()

    def __str__(self):
        return self.name
