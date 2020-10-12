
$('#app_post').on('click', function(){
    console.log("click");
    $('.ui.post.modal').modal('show');
});

$('#app_login').on('click', function(){
    console.log("click");
    $('.login.modal').modal('show');
});

$('#app_signup').on('click', function(){
    console.log("click");
    $('.signup.modal').modal('show');
});

$('.carousel').slick({
    slidesToShow: 1,
    dots:false, 
    arrows: true, 
    autoplay: true
});
$('#app_post_delete').on('click', function(){
    console.log("click");
    $('.small.modal').modal('show');
});

// $('#app_city_active').on('click', function() {
//     if(!$(this).hasClass('dropdown')) {
//     $(this)
//         .addClass('active')
//         .removeClass('active');
//     }
// });


// from semantic ui docs
// $(document).ready(function() {
//   $('.ui.menu .ui.dropdown').dropdown({
//     on: 'hover'
//   });
//   $('.item').on('click', function() {
//       $(this)
//         .addClass('active')
//         .siblings()
//         .removeClass('active');
//     });
//     console.log('I am menu clicked semantic UI') 
// });

$(document).ready(function(){
    $('.ui .item').on('click', function() {
        $('.ui .item').removeClass('active');
        $(this).addClass('active');
    });
    console.log('I am menu clicked')             
});