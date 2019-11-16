from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from import_export import resources

# Register your models here.
@admin.register(Group)
class GroupAdmin(ImportExportModelAdmin):
	list_display = ('name', 'type', 'id', 'parentGroup')

@admin.register(Christian)
class ChristianAdmin(ImportExportModelAdmin):
	list_display = ('firstName', 'secondName', 'familyGroup', 'gender', 'dateOfBaptism')

@admin.register(Contact)
class ContactAdmin(ImportExportModelAdmin):
	list_display = ('phoneNumber', 'email')

@admin.register(Person)
class PersonAdmin(ImportExportModelAdmin):
	list_display = ('firstName', 'secondName', 'gender', 'dateOfBirth')
