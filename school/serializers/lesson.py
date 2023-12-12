from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from school.models import Lessons, Course
from school.validators import UrlValidator


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lessons
        fields = '__all__'
        validators = [UrlValidator(field='url_materials')]

class LessonListSerializer(serializers.ModelSerializer):
    course = SlugRelatedField(slug_field='name', queryset=Course.objects.all())
    class Meta:
        model = Lessons
        fields = '__all__'
