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
