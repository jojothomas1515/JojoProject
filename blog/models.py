from django.db import models
from tinymce import models as tmodel

# Create your models here.

class blogpost(models.Model):
    title = models.CharField(max_length=200 )
    Post = tmodel.HTMLField()
    logo = models.ImageField('head image', null=True, blank=True, upload_to='./upload/')
    summary = models.CharField(max_length=30, null=True, blank=True)
    pub_date = models.DateField('Date Published', auto_now=True)
    pub_time = models.TimeField('Time Published', auto_now=True)

    def __str__(self):
        return self.title

