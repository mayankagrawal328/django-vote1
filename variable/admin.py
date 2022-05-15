from django.contrib import admin
from variable.models import xyz
class var(admin.ModelAdmin):
    list_display=('vvv',)
admin.site.register(xyz,var)

# Register your models here.
