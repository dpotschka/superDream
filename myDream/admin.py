from django.contrib import admin

# Register your models here.
from .models import PendingUser, User

admin.site.register(PendingUser)

admin.site.register(User)