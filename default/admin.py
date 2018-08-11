from django.contrib import admin

from .models import Field, Role, Mentor, Logs

# Register your models here.
admin.site.register(Field)
admin.site.register(Role)
admin.site.register(Mentor)
admin.site.register(Logs)