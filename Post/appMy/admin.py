from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Card)
admin.site.register(Contact)
admin.site.register(Comment)
admin.site.register(UserInfo)