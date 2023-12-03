from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from school.models import Course, Lessons

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class CourseListSerializer(serializers.ModelSerializer):
    number_of_lessons = serializers.SerializerMethodField()

    def get_number_of_lessons(self, obj):
        return Lessons.objects.filter(course=obj).count()

    class Meta:
        model = Course
        fields = '__all__'


class CourseDetailSerializer(serializers.ModelSerializer):
    lessons_of_course = SerializerMethodField()

    def get_lessons_of_course(self, obj):
        return [lesson.name for lesson in Lessons.objects.filter(course=obj)]

    class Meta:
        model = Course
        fields = '__all__'