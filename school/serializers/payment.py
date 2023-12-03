from rest_framework import serializers

from school.models import Payments


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'

class PaymentListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payments
        fields = '__all__'