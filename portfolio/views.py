from rest_framework import viewsets
from django.db.models import Q
# Create your views here.
from .models import Project, AboutMe, Skill, Contact

from .serializers import ProjectSerializer, AboutMeSerializer, SkillSerializer, ContactSerializer

class FrontendViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_queryset(self):
        queryset = Project.objects.filter(Q(types='frontend') | Q(types='both'))

        return queryset
    
class BackendViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_queryset(self):
        queryset = Project.objects.filter(Q(types='backend') | Q(types='both'))
        
        return queryset

class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class AboutMeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AboutMe.objects.all()
    serializer_class = AboutMeSerializer


class SkillViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class FrontendSkillViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

    def get_queryset(self):
        queryset = Skill.objects.filter(Q(types='frontend') | Q(types='both'))

        return queryset

class BackendSkillViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

    def get_queryset(self):
        queryset = Skill.objects.filter(Q(types='backend') | Q(types='both'))

        return queryset
    


class ContactViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer