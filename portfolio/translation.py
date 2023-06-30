from modeltranslation.translator import translator, TranslationOptions

from .models import Project, AboutMe, Skill, Contact

class ProjectTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)

class AboutMeTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)

class SkillTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)

class ContactTranslationOptions(TranslationOptions):
    fields = ('name',)

translator.register(Project, ProjectTranslationOptions)
translator.register(AboutMe, AboutMeTranslationOptions)
translator.register(Skill, SkillTranslationOptions)
translator.register(Contact, ContactTranslationOptions)