(function ($) {
    "use strict";
    
    // Dropdown on mouse hover
    $(document).ready(function () {
        function toggleNavbarMethod() {
            if ($(window).width() > 992) {
                $('.navbar .dropdown').on('mouseover', function () {
                    $('.dropdown-toggle', this).trigger('click');
                }).on('mouseout', function () {
                    $('.dropdown-toggle', this).trigger('click').blur();
                });
            } else {
                $('.navbar .dropdown').off('mouseover').off('mouseout');
            }
        }
        $('.carousel').carousel({
        autoplay: true, // Reproducción automática de los videos
        nav: true // Habilitar controles de navegación
         });
        toggleNavbarMethod();
        $(window).resize(toggleNavbarMethod);
    });
    // WhatsApp button
    window.addEventListener('scroll', function() {
    var whatsappContainer = document.getElementById('whatsapp-container');
    if (window.scrollY > 100) { // Cambia 100 por la cantidad de píxeles que desees
        whatsappContainer.style.bottom = '35px'; // Muestra el botón cuando se desplaza hacia abajo
    }
    else {
        whatsappContainer.style.bottom = '-60px'; // Oculta el botón cuando se desplaza hacia arriba
    }
    });

    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 100) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false;
    });


    // Date and time picker
    $('.date').datetimepicker({
        format: 'L'
    });
    $('.time').datetimepicker({
        format: 'LT'
    });


    // Testimonials carousel
    $(".testimonial-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1500,
        margin: 30,
        dots: true,
        loop: true,
        center: true,
        responsive: {
            0:{
                items:1
            },
            576:{
                items:1
            },
            768:{
                items:2
            },
            992:{
                items:3
            }
        }
    });
})(jQuery);


