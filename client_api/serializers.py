from rest_framework.serializers import ModelSerializer

from client_api.models import Task, Client, Responsible


class ResponsibleSerializer(ModelSerializer):
    class Meta:
        model = Responsible
        fields = '__all__'


class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ["id", "text", "date", "responsible", "client"]

    def to_representation(self, obj):
        return {
            'id': obj.id,
            'tetx': obj.text,
            'date': str(obj.date),
            'responsible': {"id": obj.responsible.id, "fio": obj.responsible.fio, "position": obj.responsible.position},
            'client': {"id": obj.client.id, "fio": obj.client.fio, "phone": str(obj.client.phone)}
        }



