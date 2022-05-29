from django.db import models

# Create your models here.

class blogpost(models.Model):
    title = models.CharField(max_length=200 )
    Post = models.TextField(null=True, blank=True)
    logo = models.ImageField('head image', null=True, blank=True)
    summary = models.CharField(max_length=200, null=True, blank=True)
    pub_date = models.DateField('Date Published', auto_now=True)
    pub_time = models.TimeField('Time Published', auto_now=True)

    def __str__(self):
        return self.title

