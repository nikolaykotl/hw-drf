from rest_framework import status
from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from school.models import Lessons
from school.paginators import SchoolPaginator
from school.permissions import IsOwner, IsModeratorOrIsOwner
from school.serializers.lesson import LessonSerializer, LessonListSerializer


class LessonDetailView(RetrieveAPIView):
    queryset = Lessons.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [AllowAny]#[IsAuthenticated, IsModeratorOrIsOwner]

class LessonListView(ListAPIView):
    queryset = Lessons.objects.all()
    serializer_class = LessonListSerializer
    permission_classes = [AllowAny] #IsAuthenticated, IsModeratorOrIsOwner]
    pagination_class = SchoolPaginator

class LessonCreateView(CreateAPIView):
    queryset = Lessons.objects.all()
    serializer_class = LessonSerializer
    #permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()


class LessonUpdateView(UpdateAPIView):
    queryset = Lessons.objects.all()
    serializer_class = LessonSerializer
    #permission_classes = [IsAuthenticated, IsModeratorOrIsOwner]

class LessonDeleteView(DestroyAPIView):
    queryset = Lessons.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsOwner]


