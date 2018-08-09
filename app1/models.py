from django.db import models
from django.contrib.postgres.fields import JSONField
# Create your models here.


class Inputs(models.Model):
    input_data = JSONField()