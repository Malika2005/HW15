from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    creation_date = models.DateField(auto_now_add=True)
    deadline_date = models.DateField()
    priority_ch = (('low', 'Low'), ('medium', 'Medium'), ('high', 'High'))
    priority = models.CharField(max_length=255, choices=priority_ch)
    # status_ch = (('not_done', 'Not Done'), ('done', 'Done'))
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title
