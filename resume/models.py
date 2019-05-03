from django.db import models


class Resume(models.Model):
    title = models.CharField(max_length=255)
    time_period = models.DateTimeField(null=True)
    body = models.TextField(null=True)
    logo = models.ImageField(upload_to='images/', null=True)
    relevant_skills = models.TextField(null=True)

    def __str__(self):
        return self.title

    def time_period_pretty(self):
        return self.time_period.strftime('%b %e %Y')

    def time_period_years(self):
        pass
