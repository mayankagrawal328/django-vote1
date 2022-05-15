from django.contrib import admin
from result.models import Result
# Register your models here.from votinglist.models import Votlins
class result(admin.ModelAdmin):
    list_display=('show',)
admin.site.register(Result,result,)
