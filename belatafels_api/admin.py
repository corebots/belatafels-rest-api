from django.contrib import admin
from .models import Table
from .models import Content
from .models import Photo

# Register your models here.

admin.site.register(Table)
admin.site.register(Content)
admin.site.register(Photo)