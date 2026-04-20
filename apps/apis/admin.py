from django.contrib import admin

from apps.apis.models.connection_profile import ConnectionProfiles
from apps.apis.models.user import User
from apps.apis.models.department import Departments
# Register your models here.
admin.site.register(User)
admin.site.register(ConnectionProfiles)
admin.site.register(Departments)
