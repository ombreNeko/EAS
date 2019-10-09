from django.db import models

class Hospital(models.Model):
    name = models.CharField(max_length=256)
    available_beds = models.PositiveIntegerField()
    crowd = models.PositiveIntegerField(null = True , blank = True)
    departments = models.ForeignKey('Department', on_delete = models.DO_NOTHING)

class Department(models.Model):
    name = models.CharField(max_length=256)