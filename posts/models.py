
from django.db import models
from django.contrib.auth.models import  User
from cloudinary.models import CloudinaryField

# Create your models here.
class Post(models.Model):
    class Meta (object):
        db_table = 'post'
    name = models.CharField(
        'Name',max_length=20,blank=False,null=False ,db_index=True
    )
    body = models.CharField(
        'Body', max_length=100, blank=False, null=False, db_index=True
    )
    created_at = models.DateTimeField(
        'Time', auto_now_add=True, blank=True
    )
    image = CloudinaryField(
        'image', db_index = True, null=True, blank=True
    )

    likes = models.PositiveIntegerField(
        'Like', default = 0, null= True, blank = True
    )

    def __str__(self):
        return self.name