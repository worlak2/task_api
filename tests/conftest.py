from django.core.management import call_command
from django.core.management.commands.loaddata import Command
from pytest import fixture


@fixture
def client_data():
    return {
        "fio": "Derek V.S",
        "phone": "+79998822452"
    }


@fixture
def client_updated_data():
    return {
        "fio": "Gena",
        "phone": "+79998822453"
    }


@fixture
def responsible_data():
    return {
        "fio": "Dim V.S",
        "position": "HR"
    }


@fixture
def responsible_updated_data():
    return {
        "fio": "Dim V.S",
        "position": "Admin"
    }


@fixture
def task_data():
    return {
        "text": "My test task",
        "responsible": 1,
        "client": 1
    }

@fixture
def task_update_data():
    return {
        "text": "My new task",
        "responsible": 1,
        "client": 1
    }


@fixture
def tasks_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command('loaddata', "tests/fixtures/tasks.json")
