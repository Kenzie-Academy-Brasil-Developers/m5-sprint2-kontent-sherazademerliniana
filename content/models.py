from django.db import models

# Create your models here.
class Content(models.Model):
    title = models.CharField(max_length = 50)
    module = models.TextField(max_length = None)
    students = models.IntegerField()
    description = models.TextField(max_length = None, null = True)
    is_active = models.BooleanField(default = False, null= True)

    def __str__(self):
        return f'<[{self.id}] {self.title} - {self.module}>'