
$('#add_post').on('click', function(){
    console.log("click");
    $('.ui.modal').modal('show');
});

$('#app_login').on('click', function(){
    console.log("click");
    $('.ui.login.modal').modal('show');
});

$('#app_signup').on('click', function(){
    console.log("click");
    $('.signup.modal').modal('show');
});

// $(document).ready(function(){
//     $('.carousel').slick({
//     slidesToShow: 1,
//     dots:false,
//     centerMode: false,
//     });
//   });

$('.carousel').slick({
    slidesToShow: 1,
    dots:false, 
    arrows: true
});