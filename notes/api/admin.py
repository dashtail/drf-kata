from django.contrib import admin

from .models import Note

class NotesAdmin(admin.ModelAdmin):
    model = Note

admin.site.register(Note, NotesAdmin)