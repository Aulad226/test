from django.contrib import admin
from Assignmentapp.models import Producer
from Assignmentapp.models import Artist
from Assignmentapp.models import Song

# Register your models here.
admin.site.register(Producer)
admin.site.register(Artist)
admin.site.register(Song)
