from django.db import models

class MongoData(models.Model):
    fill_me = models.CharField(max_length=1000)

    def __str__(self):
        return self.fill_me