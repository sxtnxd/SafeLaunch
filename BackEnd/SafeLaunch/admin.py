from django.contrib import admin
from .models import *


# Register your models here.
class AdminProviderGroup(admin.ModelAdmin):
    list_display = ('id', 'Group', 'Country', 'Abbreviation')

class AdminProviderContact(admin.ModelAdmin):
    list_display = ('id', 'PrimaryEmail', 'SecondaryEmail', 'PrimaryPhone', 'SecondaryPhone')

class AdminProviderContact(admin.ModelAdmin):
    list_display = ('id', 'PrimaryEmail', 'SecondaryEmail', 'PrimaryPhone', 'SecondaryPhone')

class AdminProvider(admin.ModelAdmin):
    list_display = ('id', 'Name', 'CNPJ', 'Initials', 'Contact', 'Group')

class AdminProduct(admin.ModelAdmin):
    list_display = ('id', 'Product', 'Description')

class AdminProjectEspecification(admin.ModelAdmin):
    list_display = ('id', 'Diameter', 'Length')

class AdminProjectData(admin.ModelAdmin):
    list_display = ('id', 'especification', 'systemDate', 'ProductionDate', 'BatchTracking', 'quantity')

class AdminProject(admin.ModelAdmin):
    list_display = ('id', 'Project', 'Provider', 'Product', 'Data')

class AdminRole(admin.ModelAdmin):
    list_display = ('id', 'Role')

class AdminCollaborator(admin.ModelAdmin):
    list_display = ('id', 'FirstName', 'LastName', 'EDV', 'Email', 'Role', 'Username')

admin.site.register(ProviderGroup, AdminProviderGroup)
admin.site.register(ProviderContact, AdminProviderContact)
admin.site.register(Provider, AdminProvider)
admin.site.register(Product, AdminProduct)
admin.site.register(Project_Especification, AdminProjectEspecification)
admin.site.register(Project_Data, AdminProjectData)
admin.site.register(Project, AdminProject)
admin.site.register(Collaborator, AdminCollaborator)
admin.site.register(Role, AdminRole)




