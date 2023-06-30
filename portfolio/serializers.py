from rest_framework import serializers

from .models import FrontendProject, BackendProject, AboutMe, Skill, Contact

class FrontendProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = FrontendProject
        fields = '__all__'

class BackendProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = BackendProject
        fields = '__all__'

class AboutMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutMe
        fields = '__all__'


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'