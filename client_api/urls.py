from django.conf.urls import url
from django.urls import include

from client_api.views import TaskList, ClientView, ResponsibleView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'task', TaskList)
router.register(r'client', ClientView)
router.register(r'responsible', ResponsibleView)

urlpatterns = [
    url(r'^', include(router.urls)),

]
