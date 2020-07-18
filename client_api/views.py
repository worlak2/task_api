from django.utils.decorators import method_decorator
from rest_framework import viewsets
from django.views.decorators.cache import cache_page

from client_api.models import Task, Client, Responsible
from client_api.serializers import TaskSerializer, ClientSerializer, ResponsibleSerializer
from task_api.settings import CASHE_TIME


class BaseRetrieveCashed(viewsets.ModelViewSet):
    queryset = None
    serializer_class = None

    @method_decorator(cache_page(CASHE_TIME))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @method_decorator(cache_page(CASHE_TIME))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class TaskList(BaseRetrieveCashed):
    """
    Class to retrieve, update, delete and create task.
    """
    queryset = Task.objects.select_related()
    serializer_class = TaskSerializer


class ClientView(BaseRetrieveCashed):
    """
    Class to retrieve, update, delete and create client.
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ResponsibleView(BaseRetrieveCashed):
    """
    Class to retrieve, update, delete and create responsible.
    """
    queryset = Responsible.objects.all()
    serializer_class = ResponsibleSerializer
