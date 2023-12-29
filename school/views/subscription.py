from rest_framework import generics, status
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from school.models import Subscription
from school.serializers.subscription import SubscriptionSerializer, SubscriptionListSerializer


class SubscriptionCreateView(generics.CreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = SubscriptionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(status=status.HTTP_201_CREATED)


class SubscriptionListView(generics.ListAPIView):
    serializer_class = SubscriptionListSerializer

    def get_queryset(self):
        return Subscription.objects.all()#filter(user=self.request.user)


class SubscriptionDestroyView(generics.DestroyAPIView):
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Subscription.objects.filter(user=self.request.user)

