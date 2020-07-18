from django.test.client import Client
from django.urls import reverse
from pytest import mark
from client_api.models import Responsible, Task
from client_api.models import Client as model_client
from django.forms.models import model_to_dict


def crud_operations(client: Client, client_data, client_updated_data, path, select_model):
    client.post(reverse(f"{path}-list"), data=client_data)
    assert select_model.objects.exists()
    client.put(reverse(f"{path}-detail", kwargs={"pk": "1"}), data=client_updated_data,
               content_type="application/json")
    updated_data = model_to_dict(select_model.objects.first())
    updated_data.pop("id")
    assert updated_data == client_updated_data
    client.delete(reverse(f"{path}-detail", kwargs={"pk": "1"}), data=client_updated_data,
                  content_type="application/json")
    assert not select_model.objects.exists()


@mark.django_db
def test_client(client: Client, client_data, client_updated_data):
    crud_operations(client, client_data, client_updated_data, "client", model_client)


@mark.django_db
def test_responsible(client: Client, responsible_data, responsible_updated_data):
    crud_operations(client, responsible_data, responsible_updated_data, "responsible", Responsible)


@mark.django_db
def test_tasks(client: Client, task_data, task_update_data, tasks_db_setup):
    assert model_client.objects.exists()
    crud_operations(client, task_data, task_update_data, "task", Task)
