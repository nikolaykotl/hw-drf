from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from school.models import Lessons
from school.serializers.lesson import LessonSerializer, LessonListSerializer


class LessonDetailView(RetrieveAPIView):
    queryset = Lessons.objects.all()
    serializer_class = LessonSerializer

class LessonListView(ListAPIView):
    queryset = Lessons.objects.all()
    serializer_class = LessonListSerializer

class LessonCreateView(CreateAPIView):
    queryset = Lessons.objects.all()
    serializer_class = LessonSerializer

class LessonUpdateView(UpdateAPIView):
    queryset = Lessons.objects.all()
    serializer_class = LessonSerializer

class LessonDeleteView(DestroyAPIView):
    queryset = Lessons.objects.all()
    serializer_class = LessonSerializer
