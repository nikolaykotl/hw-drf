from rest_framework.viewsets import ModelViewSet

from school.models import Course
from school.serializers.course import CourseDetailSerializer, CourseSerializer, CourseListSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    default_serializer = CourseSerializer
    serializers = {
        "list": CourseListSerializer,
        "retrieve": CourseDetailSerializer,
    }
    def get_serializer_class(self):
        return self.serializers.get(self.action,self.default_serializer)