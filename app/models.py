from django.db import models

# Create your models here.
class Url_short(models.Model):
    url = models.CharField(max_length=200)
    short_url = models.CharField(max_length = 100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.url