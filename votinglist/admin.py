from django.contrib import admin
from votinglist.models import Votlins
class Table(admin.ModelAdmin):
    list_display=('Candidates','votes','email',)
admin.site.register(Votlins,Table,)
# Register your models here.
