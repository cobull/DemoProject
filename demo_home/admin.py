from django.contrib import admin

from .models import Inspection
from .models import Condition

admin.site.register(Inspection)
admin.site.register(Condition)
