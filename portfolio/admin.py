from django.contrib import admin

from .models import FrontendProject, BackendProject, AboutMe, Skill, Contact

# Register your models here.
admin.site.register([FrontendProject, BackendProject, AboutMe, Skill, Contact])
