from rest_framework.viewsets import ModelViewSet

from school.models import Course
from school.serializers.course import CourseSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer