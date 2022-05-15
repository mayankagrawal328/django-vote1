from django.contrib import admin
from temp.models import tempuser
class temp(admin.ModelAdmin):
    list_display=('email','password','name','phone','postal','gender')
admin.site.register(tempuser,temp)

# Register your models here.
