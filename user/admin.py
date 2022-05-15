from django.contrib import admin
from user.models import user
class Voater(admin.ModelAdmin):
    list_display=('email','password','name','phone','postal','gender')
admin.site.register(user,Voater)

# Register your models here.
