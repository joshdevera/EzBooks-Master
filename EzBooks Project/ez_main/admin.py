###############################################################################
#                  Registrations for the ez_main app models                   #
###############################################################################

from django.contrib import admin
from .models import Classes_list, Class_schedule

admin.site.register(Classes_list)
admin.site.register(Class_schedule)
