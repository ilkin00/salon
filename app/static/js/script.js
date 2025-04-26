<<<<<<< HEAD
// Sayfa yüklendiğinde yapılacak işlemler
document.addEventListener('DOMContentLoaded', function() {
    // Navbar mobil menüsü için açma/kapama işlevi
    const navbarToggler = document.querySelector('.navbar-toggler');
    const navbarNav = document.querySelector('#navbarNav');
    
    navbarToggler.addEventListener('click', function() {
        navbarNav.classList.toggle('collapse');
        navbarNav.classList.toggle('show');
    });

    // El İşleri Kartları için Hover Etkisi
    const cardElements = document.querySelectorAll('.card');

    cardElements.forEach(card => {
        card.addEventListener('mouseenter', function() {
            card.style.transform = 'scale(1.05)';
            card.style.transition = 'transform 0.3s ease';
        });
        
        card.addEventListener('mouseleave', function() {
            card.style.transform = 'scale(1)';
        });
    });

    // Profilde Görsel Önizleme
    const imageInput = document.querySelector('#profileImage');
    const imagePreview = document.querySelector('#imagePreview');

    if (imageInput && imagePreview) {
        imageInput.addEventListener('change', function(e) {
            const reader = new FileReader();
            reader.onload = function(event) {
                imagePreview.src = event.target.result;
                imagePreview.style.display = 'block';
            };
            reader.readAsDataURL(e.target.files[0]);
        });
    }

    // Profilde Çıkış Yapma
    const logoutBtn = document.querySelector('#logoutButton');
    if (logoutBtn) {
        logoutBtn.addEventListener('click', function(e) {
            e.preventDefault();
            if (confirm("Çıkış yapmak istediğinizden emin misiniz?")) {
                window.location.href = '/logout/';
            }
        });
    }

    // Sosyal Medya Linklerine Dinamik Ekleme
    const socialMediaLinks = document.querySelectorAll('.social-media a');
    
    socialMediaLinks.forEach(link => {
        link.addEventListener('mouseenter', function() {
            link.style.transform = 'scale(1.1)';
            link.style.transition = 'transform 0.3s ease';
        });
        
        link.addEventListener('mouseleave', function() {
            link.style.transform = 'scale(1)';
        });
    });
});

// Modal için Basit Kullanım (Opsiyonel - Örneğin Login/Register için)
function showModal(modalId) {
    const modal = document.querySelector(`#${modalId}`);
    if (modal) {
        modal.style.display = 'block';
    }
}

function hideModal(modalId) {
    const modal = document.querySelector(`#${modalId}`);
    if (modal) {
        modal.style.display = 'none';
    }
}

// Sayfa Yüklenince Mobil Menü için Açılabilir Menüyü Ayarlama
const mediaQuery = window.matchMedia('(max-width: 991px)');
mediaQuery.addListener(function(e) {
    if (!e.matches) {
        navbarNav.classList.remove('show');
    }
});
=======
$(document).ready(function() {
    // Sayfa yüklendikçe fade-in animasyonu ekleyelim
    $('body').addClass('fade-in');
    
    // Navbar'da scroll efektini aktif hale getirelim
    $(window).scroll(function() {
        if ($(this).scrollTop() > 100) {
            $('.navbar').addClass('bg-dark');
        } else {
            $('.navbar').removeClass('bg-dark');
        }
    });
});
>>>>>>> c6660c705694c7fb36038816303411bc386e7da4
