from datetime import date

from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from school.models import Course, Lessons, Payments
from school.services import link_to_pay

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
    payment_link = serializers.SerializerMethodField(read_only=True)
    def get_lessons_of_course(self, obj):
        return [lesson.name for lesson in Lessons.objects.filter(course=obj)]

    def get_payment_link(self, course):

        return link_to_pay(course)

    class Meta:
        model = Course
        fields = '__all__'