from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from school.models import Course
from school.permissions import IsModeratorOrIsOwner, IsOwner
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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_course = serializer.save()
        new_course.owner = self.request.user
        new_course.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_permissions(self):
        if self.action == 'list' or self.action == 'create':
            permission_classes = [IsAuthenticated]

        elif self.action == 'destroy':
            permission_classes = [IsOwner]
        else:
            permission_classes = [IsModeratorOrIsOwner]
        return [permission() for permission in permission_classes]
