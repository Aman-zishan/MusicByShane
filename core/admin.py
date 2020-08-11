from django.contrib import admin
from .models import Track, Event

admin.site.register(Track)
admin.site.register(Event)
admin.site.site_header = "Admin"
admin.site.site_title = " Admin Portal"
admin.site.index_title = "Welcome to Admin Portal"
