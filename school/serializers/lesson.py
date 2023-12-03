from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from school.models import Lessons, Course


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lessons
        fields = '__all__'

class LessonListSerializer(serializers.ModelSerializer):
    course = SlugRelatedField(slug_field='name', queryset=Course.objects.all())
    class Meta:
        model = Lessons
        fields = '__all__'