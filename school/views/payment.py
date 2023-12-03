from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView

from school.models import Payments
from school.serializers.payment import PaymentListSerializer


class PaymentListView(ListAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentListSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('course', 'lesson', 'payment_method')
    ordering_fields = ('date_payment',)