from django.db import models
from django.db.models import CASCADE
from phonenumber_field.modelfields import PhoneNumberField


class Responsible(models.Model):
    fio = models.CharField(max_length=150)
    position = models.TextField()

    def __str__(self):
        return self.fio


class Client(models.Model):
    fio = models.CharField(max_length=150)
    phone = PhoneNumberField()

    def __str__(self):
        return self.fio


class Task(models.Model):
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    responsible = models.ForeignKey(Responsible, on_delete=CASCADE)
    client = models.ForeignKey(Client, on_delete=CASCADE)

    def __str__(self):
        return self.text
