from django.contrib import admin
from .models import *
from django.utils.html import format_html

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        if obj.image and hasattr(obj.image, 'url'):
            return format_html('<img src="{}" style="max-width:400px; max-height:400px"/>'.format(obj.image.url))
        else:
            # Usando um placeholder de 200x200 pixels
            placeholder_url = "https://th.bing.com/th/id/R.4614b1581f6187a9beceea4187db135f?rik=h2CwAt3T4o8T9g&pid=ImgRaw&r=0"
            return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(placeholder_url))


    image_tag.short_description = 'Foto'

    list_display = ('nome',"email","telefone","foto")

admin.site.register(User,UserAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ("user","mensage","data_publicacao")

admin.site.register(Post,PostAdmin)