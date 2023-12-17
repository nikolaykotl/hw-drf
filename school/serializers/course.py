from datetime import date

from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from school.models import Course, Lessons, Payments
from school.services import link_to_pay, payment


class CourseSerializer(serializers.ModelSerializer):
  #  payment_link = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Course
        fields = '__all__'

 #   def get_payment_link(self, course):
 ##       user = self.context['request'].user
  #      current_date = date.today()
  #      Payments.objects.create(
  #          user=user,
  #          date_payment=current_date,
  #          lesson=course.name,
  #          payment_amount=course.price,
  #          payment_method='TRANSFER'
  #      )
  #      print(link_to_pay(course))
  #      return link_to_pay(course)

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
        print(link_to_pay(course))
        print(payment())
        return link_to_pay(course)

    class Meta:
        model = Course
        fields = '__all__'