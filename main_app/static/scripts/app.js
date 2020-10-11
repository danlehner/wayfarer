
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

$('#app_post_delete').on('click', function(){
    console.log("click");
    $('.small.modal').modal('show');
});

$('#app_city_active').on('click', function() {
    if(!$(this).hasClass('dropdown')) {
    $(this)
        .addClass('active')
        .removeClass('active');
    }
});