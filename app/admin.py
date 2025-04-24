from django.contrib import admin
from .models import User, Settings, SocialLink, Appointment, Category, Staff, Handcraft, HandcraftImage, HandcraftVideo, Page


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'site_logo', 'logo_size', 'site_favicon')

    def logo_size(self, obj):
        if obj.logo_width and obj.logo_height:
            return f'{obj.logo_width}x{obj.logo_height}'
        return 'N/A'
# SOCIAL LINK Model
@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('platform', 'url', 'icon')

# APPOINTMENT Model
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'status', 'confirmed', 'created_at')

# CATEGORY Model
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')

# STAFF Model
@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'category', 'bio', 'image')

# HANDCRAFT Model
@admin.register(Handcraft)
class HandcraftAdmin(admin.ModelAdmin):
    list_display = ('staff', 'title', 'description', 'created_at')

# HANDCRAFT IMAGE Model
@admin.register(HandcraftImage)
class HandcraftImageAdmin(admin.ModelAdmin):
    list_display = ('handcraft', 'image')

# HANDCRAFT VIDEO Model
@admin.register(HandcraftVideo)
class HandcraftVideoAdmin(admin.ModelAdmin):
    list_display = ('handcraft', 'video_url', 'video_file')

# PAGE Model
@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('slug', 'content')
