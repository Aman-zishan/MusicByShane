from django.contrib import admin
from .models import Track, Event, Gallery_image

admin.site.register(Track)
admin.site.register(Event)
admin.site.register(Gallery_image)
admin.site.site_header = "Admin"
admin.site.site_title = " Admin Portal"
admin.site.index_title = "Welcome to Admin Portal"
