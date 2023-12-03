from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from school.models import Lessons, Course, Payments


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'

class PaymentListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payments
        fields = '__all__'