from django.db import models


class Ctfs(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(null=True)
    logo = models.ImageField(upload_to='images/', null=True)
    tools_used = models.TextField(null=True)

    def __str__(self):
        return self.title
