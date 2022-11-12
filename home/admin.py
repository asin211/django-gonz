from django.contrib import admin
from .models import *   # will import all classes
from home.models import Contact

# Register your models here.
admin.site.register(Contact)
admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(TourData)

