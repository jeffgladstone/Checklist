from django.db import models


class Task(models.Model):
    description = models.CharField(max_length=100)
    date_created = models.DateTimeField()
    is_done = models.BooleanField(default = True)

    def __str__(self):
        return self.description