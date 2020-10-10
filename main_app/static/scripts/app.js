
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

$('.carousel').slick({
    slidesToShow: 1,
    dots:false, 
    arrows: true
});