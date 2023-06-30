from django.contrib import admin
from parler.admin import TranslatableAdmin

from .models import FrontendProject, BackendProject, AboutMe, Skill, Contact

# Register your models here.
admin.site.register([BackendProject, AboutMe, Skill, Contact])

admin.site.register(FrontendProject, TranslatableAdmin)