from django.urls import path

from rest_framework.routers import DefaultRouter

from school.apps import SchoolConfig
from school.views.lesson import *
from school.views.course import *

app_name = SchoolConfig.name



router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')


urlpatterns = [
    path('', LessonListView.as_view(), name='list_lesson'),
    path('<int:pk>/', LessonDetailView.as_view(), name='detail_lesson'),
    path('update/<int:pk>/', LessonUpdateView.as_view(), name='update_lesson'),
    path('create/', LessonCreateView.as_view(), name='create_lesson'),
    path('delete/<int:pk>/', LessonDeleteView.as_view(), name='delete_lesson'),

              ] + router.urls