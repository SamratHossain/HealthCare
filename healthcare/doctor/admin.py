from django.contrib import admin
from .models import (Qualification, 
                        Specialist, 
                        Experience,
                        DoctorInfo,
                        Review)

# Register your models here.

admin.site.register(Qualification)
admin.site.register(Specialist)
admin.site.register(Experience)
admin.site.register(DoctorInfo)
admin.site.register(Review)
