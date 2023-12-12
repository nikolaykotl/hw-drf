from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from school.models import Subscription, Course
from users.models import User


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'


class SubscriptionListSerializer(serializers.ModelSerializer):
    user = SlugRelatedField(slug_field='email', queryset=User.objects.all())
    course = SlugRelatedField(slug_field='name', queryset=Course.objects.all())

    class Meta:
        model = Subscription
        fields = '__all__'
