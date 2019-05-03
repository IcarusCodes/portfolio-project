from django.db import models


class Home(models.Model):
    title = models.CharField(max_length=255, null=True)
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=500)

    def __str__(self):
        return self.title
