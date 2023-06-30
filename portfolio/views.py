from rest_framework import viewsets
# Create your views here.
from .models import FrontendProject, BackendProject, AboutMe, Skill, Contact

from .serializers import FrontendProjectSerializer, BackendProjectSerializer, AboutMeSerializer, SkillSerializer, ContactSerializer


class FrontendProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FrontendProject.objects.all()
    serializer_class = FrontendProjectSerializer

class BackendProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BackendProject.objects.all()
    serializer_class = BackendProjectSerializer

class AboutMeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AboutMe.objects.all()
    serializer_class = AboutMeSerializer


class SkillViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class ContactViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer