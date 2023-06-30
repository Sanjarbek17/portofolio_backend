from django.contrib import admin

from modeltranslation.admin import TranslationAdmin

from .models import Project, AboutMe, Skill, Contact

# Register your models here.
# admin.site.register([Project, AboutMe, Skill, Contact])


class ProjectAdmin(TranslationAdmin):
    pass


class AboutMeAdmin(TranslationAdmin):
    pass


class SkillAdmin(TranslationAdmin):
    pass


class ContactAdmin(TranslationAdmin):
    pass


admin.site.register(AboutMe, AboutMeAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Contact, ContactAdmin)

