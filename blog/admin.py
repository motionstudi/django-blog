
from django.contrib import admin

# Register your models here.
from .models import Post

class CatAdmin(admin.ModelAdmin):
        prepopulated_fields = {'slug':('title',)}

admin.site.register(Post)