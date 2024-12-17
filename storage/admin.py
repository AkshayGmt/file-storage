from django.contrib import admin
from .models import Folder,File, FileRoot  # Import your model

# Register the model with the admin site
admin.site.register(Folder)
admin.site.register(File)
admin.site.register(FileRoot)
