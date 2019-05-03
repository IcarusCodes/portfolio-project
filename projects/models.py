from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(null=True)
    logo = models.ImageField(upload_to='images/', null=True)
    technologies_used = models.TextField(null=True)

    def __str__(self):
        return self.title
