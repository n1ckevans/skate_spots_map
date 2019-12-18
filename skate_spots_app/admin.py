from django.contrib import admin

# Register your models here.
from skate_spots_app.models import User, Message, Comment, Marker

admin.site.register(User)
admin.site.register(Message)
admin.site.register(Comment)
admin.site.register(Marker)