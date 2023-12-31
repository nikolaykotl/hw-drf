from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from school.models import Payments, Course, Lessons
from school.paginators import SchoolPaginator
from school.serializers.course import CourseSerializer
from school.serializers.lesson import LessonSerializer
from school.serializers.payment import PaymentListSerializer


class PaymentListView(ListAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentListSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('course', 'lesson', 'payment_method')
    ordering_fields = ('date_payment',)
    pagination_class = SchoolPaginator