from django.shortcuts import render
from .models import Settings, Category, Staff, Handcraft, HandcraftImage

def index(request):
    # Veritabanından verileri çekiyoruz
    settings = Settings.objects.first()  # Ayarları alıyoruz (sadece bir tane olduğu için .first() kullanıyoruz)
    categories = Category.objects.all()  # Tüm kategorileri alıyoruz
    staff_members = Staff.objects.all()  # Tüm çalışanları alıyoruz
    handcrafts = Handcraft.objects.all()  # Tüm el işleri paylaşımlarını alıyoruz
    handcraft_images = HandcraftImage.objects.all()  # El işlerine ait resimleri alıyoruz

    # Sosyal medya bağlantıları
    social_media = {
        'facebook': 'https://www.facebook.com/username',
        'twitter': 'https://twitter.com/username',
        'instagram': 'https://www.instagram.com/username',
        'linkedin': 'https://www.linkedin.com/in/username',
        'github': 'https://github.com/username',
        'youtube': 'https://www.youtube.com/channel/username'
    }

    # Template'ye veri gönderiyoruz
    return render(request, 'index.html', {
        'settings': settings,
        'categories': categories,
        'staff_members': staff_members,
        'handcrafts': handcrafts,
        'handcraft_images': handcraft_images,  # handcraft_images olarak gönderiyoruz
        'social_media': social_media,
    })
