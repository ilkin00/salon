from django.shortcuts import render, redirect
from .models import Settings, Category, Staff, Handcraft, HandcraftImage, HandcraftVideo, UserProfile
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from .forms import UserProfileForm
from django.contrib.auth.decorators import login_required


def index(request):
    # Veritabanından verileri çekiyoruz
    settings = Settings.objects.first()  # 'Settings' modelinden veriyi çekiyoruz
    categories = Category.objects.all()
    staff_members = Staff.objects.all()
    handcrafts = Handcraft.objects.all()
    handcraft_images = HandcraftImage.objects.all()
    handcraft_videos = HandcraftVideo.objects.all()

    # Sosyal medya bağlantıları
    social_media = {
        'facebook': 'https://www.facebook.com/username',
        'twitter': 'https://twitter.com/username',
        'instagram': 'https://www.instagram.com/username',
        'linkedin': 'https://www.linkedin.com/in/username',
        'github': 'https://github.com/username',
        'youtube': 'https://www.youtube.com/channel/username'
    }

    return render(request, 'index.html', {
        'settings': settings,
        'categories': categories,
        'staff_members': staff_members,
        'handcrafts': handcrafts,
        'handcraft_images': handcraft_images,
        'handcraft_videos': handcraft_videos,
        'social_media': social_media,
    })


# Register view
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Kayıt başarılı ise login sayfasına yönlendir
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


# Login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')  # Login başarılı ise ana sayfaya yönlendir
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


# Logout view
def logout_view(request):
    logout(request)
    return redirect('index')  # Logout sonrası ana sayfaya yönlendir


@login_required
def profile_view(request):
    try:
        # Kullanıcının profil bilgilerini alıyoruz
        profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        # Profil yoksa, yeni profil oluştur
        profile = UserProfile(user=request.user)
        profile.save()

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Profil sayfasına yönlendiriyoruz
    else:
        form = UserProfileForm(instance=profile)

    return render(request, 'profile.html', {'form': form})
