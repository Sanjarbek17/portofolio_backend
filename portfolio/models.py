from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='frontend_projects')
    github_link = models.URLField()
    live_link = models.URLField()

    _choices = (
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('both', 'Frontend and Backend')
    )
    types = models.CharField(max_length=100, choices=_choices)

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
    icon = models.FileField(upload_to='skill')

    _choices = (
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('both', 'Frontend and Backend')
    )
    types = models.CharField(max_length=100, choices=_choices, default='frontend')

    def __str__(self):
        return self.title
    

class Contact(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField()
    icon = models.FileField(upload_to='contact')

    def __str__(self):
        return self.name