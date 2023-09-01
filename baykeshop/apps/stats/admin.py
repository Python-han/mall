from django.contrib import admin

# Register your models here.
from .models import BaykeClientUser, BaykeDataStats

admin.site.register([BaykeClientUser, BaykeDataStats])