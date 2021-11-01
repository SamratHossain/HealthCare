from django.contrib import admin
from .models import (Qualification, 
                        Specialist, 
                        Experience,
                        DoctorProfile,
                        Review)

# Register your models here.

admin.site.register(Qualification)
admin.site.register(Specialist)
admin.site.register(Experience)
admin.site.register(DoctorProfile)
admin.site.register(Review)
