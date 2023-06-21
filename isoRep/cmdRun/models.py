# # Database import

# from django import db


# # Settings import
# from django.conf import settings

# # Other import
# from datetime import datetime

# class Task(models.Model):
#     sdate = models.DateTimeField()
#     fdate = models.DateTimeField()
#     file = models.TextField()
#     name = models.CharField(max_length=255)
#     command = models.CharField(max_length=255)
#     status = models.IntegerField(null=True)

# def command_run_db(name, command, status,log_file):

#     task = Task(
#         sdate=datetime.today().strftime('%Y-%m-%d-%H-%M-%S'),
#         fdate=None,
#         file=log_file,
#         name=name,
#         command=command,
#         status=status
#     )

#     task.save()
#     process_id = task.id

#     if status == 0:
#         task = Task.objects.get(id=process_id)
#         task.sdate = items["Sdate"]
#         task.fdate = datetime.now()
#         task.file = items["File"]
#         task.name = items["Name"]
#         task.command = items["Command"]
#         task.status = status
#         task.save()
#     else:
#         task = Task.objects.get(id=process_id)
#         task.sdate = items["Sdate"]
#         task.fdate = datetime.now()
#         task.file = items["File"]
#         task.name = items["Name"]
#         task.command = items["Command"]
#         task.status = status
#         task.save()


from django.db import models

class CommandExecution(models.Model):
    command = models.CharField(max_length=255)
    status = models.IntegerField()
    log_file = models.CharField(max_length=255)
    start_execution = models.DateTimeField(auto_now_add=True)
    end_execution = models.DateTimeField(auto_now=True)
    duration = models.FloatField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.start_execution and self.end_execution:
            self.duration = (self.end_execution - self.start_execution).total_seconds()
        super().save(*args, **kwargs)