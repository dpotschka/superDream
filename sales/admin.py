from django.contrib import admin

# Register your models here.
from .models import PaypalDB, PaypalTestDB, ClientDB

admin.site.register(PaypalDB)
admin.site.register(PaypalTestDB)
admin.site.register(ClientDB)