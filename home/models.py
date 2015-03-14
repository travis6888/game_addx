
from django.db import models

# Create your models here.


class Email(models.Model):
    email = models.EmailField()

    # def send_email(self):
