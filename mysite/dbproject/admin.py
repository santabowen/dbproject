from django.contrib import admin

from .models import Population
from .models import StateCode

admin.site.register(Population)
admin.site.register(StateCode)