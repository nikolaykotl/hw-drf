from datetime import date

from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from school.models import Lessons, Course, Payments
from school.services import link_to_pay
from school.validators import UrlValidator


class LessonSerializer(serializers.ModelSerializer):
    payment_link = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Lessons
        fields = '__all__'
        validators = [UrlValidator(field='url_materials')]


    def get_payment_link(self, lesson):
       print(link_to_pay(lesson))
       return link_to_pay(lesson)


class LessonListSerializer(serializers.ModelSerializer):
    course = SlugRelatedField(slug_field='name', queryset=Course.objects.all())
    class Meta:
        model = Lessons
        fields = '__all__'
