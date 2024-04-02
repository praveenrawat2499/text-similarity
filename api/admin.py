from django.contrib import admin

# Register your models here.
from api.models import Texts 
# Register your models here.
@admin.register(Texts)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['text1', 'text2']

