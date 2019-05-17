from django.db import models


class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()
    description = models.TextField()


class SQLData(models.Model):
    fill_me = models.CharField(max_length=1000)

    def __str__(self):
        return self.fill_me
