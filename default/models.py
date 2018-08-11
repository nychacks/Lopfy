from django.db import models
import os

# Create your models here.
def get_image_path(instance, filename):
    return os.path.join('media', str(instance.id), filename)

class Field(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    field = models.ForeignKey(Field, on_delete=models.CASCADE)

    def __str__(self):
        return self.field.name + " - " + self.name

class Mentor(models.Model):
    name = models.CharField(max_length=200)
    picture = models.ImageField(upload_to=get_image_path)
    company = models.CharField(max_length=200)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    start_date =  models.DateTimeField('start date')
    notes = models.TextField(default='')

    def __str__(self):
        return self.name + '(' + self.role.name + ')'

class Logs(models.Model):
    mentor =  models.ForeignKey(Mentor, on_delete=models.CASCADE)
    day = models.IntegerField(default=0)
    hour = models.IntegerField(default=0)
    category = models.CharField(max_length=20, choices = (
            ('intense', 'intense'),
            ('moderate', 'moderate'),
            ('break', 'break'),
            ('chill','chill'),
            ('topic','off topic')
        )
    )
    description = models.TextField()
    
    def __str__(self):
        return self.description + ' ( ' + str(self.day) + ',' + str(self.hour) + ' )'
