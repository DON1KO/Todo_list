from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['is_active']

    def get_queryset(self):
        """Каждый пользователь видит только СВОИ задачи."""
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """Автоматически привязываем задачу к текущему пользователю."""
        serializer.save(user=self.request.user)
