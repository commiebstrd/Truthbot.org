from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(WebPage)
admin.site.register(OrganizationDomain)
admin.site.register(Organization)
admin.site.register(LoggedOrganizationEdit)