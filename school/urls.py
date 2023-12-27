from django.urls import path

from rest_framework.routers import DefaultRouter

from school.apps import SchoolConfig
from school.views.lesson import *
from school.views.course import *
from school.views.payment import PaymentListView
from school.views.stripe import CourseStripeIntent
#from school.views.stripe import StripeIntentView
from school.views.subscription import SubscriptionCreateView, SubscriptionListView, SubscriptionDestroyView
from school.views.webhook import stripe_webhook

app_name = SchoolConfig.name



router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')


urlpatterns = [
    path('', LessonListView.as_view(), name='list_lesson'),
    path('<int:pk>/', LessonDetailView.as_view(), name='detail_lesson'),
    path('update/<int:pk>/', LessonUpdateView.as_view(), name='update_lesson'),
    path('create/', LessonCreateView.as_view(), name='create_lesson'),
    path('delete/<int:pk>/', LessonDeleteView.as_view(), name='delete_lesson'),
    path('payment/', PaymentListView.as_view(), name='payment_list'),
    path('subscriptions/create/', SubscriptionCreateView.as_view(), name='create_subscription'),
    path('subscriptions/', SubscriptionListView.as_view(), name='list_subscription'),
    path('subscriptions/delete/<int:pk>/', SubscriptionDestroyView.as_view(), name='delete_subscription'),
    path('webhook/stripe/', stripe_webhook, name='stripe_webhook'),
    path('payment_intent/course/<int:pk>', CourseStripeIntent, name='payment_intent_course')

              ] + router.urls