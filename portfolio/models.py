from django.db import models
from parler.models import TranslatableModel, TranslatedFields

# Create your models here.
class FrontendProject(TranslatableModel):
    TranslatedFields(
    title = models.CharField(max_length=100),
    description = models.TextField(),
    image = models.ImageField(upload_to='frontend_projects'),
    github_link = models.URLField(),
    live_link = models.URLField(),
    )
    def __str__(self):
        return self.title
    
class BackendProject(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='backend_projects')
    github_link = models.URLField()
    live_link = models.URLField()

    def __str__(self):
        return self.title

class AboutMe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='about_me')

    def __str__(self):
        return self.title
    
class Skill(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.ImageField(upload_to='skill')

    def __str__(self):
        return self.title
    

class Contact(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField()
    icon = models.ImageField(upload_to='contact')