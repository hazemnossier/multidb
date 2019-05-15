from django.db import models


class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()
    description = models.TextField()


class Data(models.Model):
    fill_me = models.CharField(max_length=1000)

# _MONGODB_USER = 'mongouser'
# _MONGODB_PASSWD = 'password'
# _MONGODB_HOST = 'thehost'
# _MONGODB_NAME = 'thedb'
# _MONGODB_DATABASE_HOST = \
#     'mongodb://%s:%s@%s/%s' \
#     % (_MONGODB_USER, _MONGODB_PASSWD, _MONGODB_HOST, _MONGODB_NAME)

# mongoengine.connect(_MONGODB_NAME, host=_MONGODB_DATABASE_HOST)
