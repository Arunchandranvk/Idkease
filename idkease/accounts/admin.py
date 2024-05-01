from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Users)
admin.site.register(Complaint)
admin.site.register(Recommendation)
admin.site.register(Tracking)
admin.site.register(Informations)