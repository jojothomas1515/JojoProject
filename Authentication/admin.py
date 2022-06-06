from django.contrib import admin

# Register your models here.
from . import models as m

admin.site.register(m.Profile)