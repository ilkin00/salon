from django.db import models
from PIL import Image


# USERS
class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    signup_type = models.CharField(max_length=20, choices=[('google', 'Google'), ('facebook', 'Facebook'), ('email', 'Email')])
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
from django.db import models
from PIL import Image  # Image modülünü ekliyoruz

class Settings(models.Model):
    site_name = models.CharField(max_length=255)
    site_logo = models.ImageField(upload_to='logos/')  # Logo için ImageField
    site_favicon = models.ImageField(upload_to='favicons/', null=True, blank=True)  # Favicon için ImageField
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()

    logo_width = models.IntegerField(null=True, blank=True)
    logo_height = models.IntegerField(null=True, blank=True)

    def save(self, *args, **kwargs):
        # Eğer logo eklenmişse, boyutları alıyoruz
        if self.site_logo:
            img = Image.open(self.site_logo)
            self.logo_width, self.logo_height = img.size
        super().save(*args, **kwargs)

    def __str__(self):
        return self.site_name

# SOCIAL LINKS
class SocialLink(models.Model):
    platform = models.CharField(max_length=50)
    url = models.URLField()
    icon = models.CharField(max_length=100, blank=True, null=True)

# APPOINTMENTS
class Appointment(models.Model):
    STATUS_CHOICES = [(0, 'WhatsApp'), (1, 'Site içi')]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField()
    status = models.IntegerField(choices=STATUS_CHOICES)
    confirmed = models.BooleanField(default=False)
    contact_info = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

# CATEGORIES
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

# STAFF
class Staff(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    bio = models.TextField()
    image = models.URLField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    social = models.JSONField(blank=True, null=True)

# HANDCRAFTS
class Handcraft(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class HandcraftImage(models.Model):
    handcraft = models.ForeignKey('Handcraft', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='handcrafts/')  # media/handcrafts/ klasörüne yüklenir

    def __str__(self):
        return f"{self.handcraft.title} Resmi"

# HANDCRAFT VIDEOS
class HandcraftVideo(models.Model):
    handcraft = models.ForeignKey(Handcraft, on_delete=models.CASCADE)
    video_url = models.URLField()

# STATIC PAGES
class Page(models.Model):
    slug = models.SlugField(unique=True)
    content = models.TextField()
