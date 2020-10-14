
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

$('#app_comment').on('click', function(){
    console.log("comment click"); 
    $('.comment.modal').modal('show'); 
}); 

$(document).ready(function(){ 
    $('.submit-edit').hide() 
})

$('.app_comment_edit').on('click', function(){
   const elm = $(this).parent().parent().children()[0]
   fetch(`/posts/${this.id}/edit_comment`)
   .then(function(response){
       return response.json()
   })
   .then(function(json){
       const comment = json[0].fields
       $(elm).html(`<textarea id='textarea-edit'>${comment.text}</textarea>`)
       $('.submit-edit').show() 
   })
})

$('.submit-edit').on('click', function() {
    const elm = $('#textarea-edit')
    fetch(`/posts/${this.id}/edit_comment`, {
        method: 'POST', 
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            text: elm.val()
        })
    })
    .then(function() {
        window.location.reload()
    })
})

$('.carousel').slick({
    slidesToShow: 1,
    dots:false, 
    arrows: true, 
    autoplay: true
});

$('#app_post_delete').on('click', function(){
    console.log("click");
    $('#delete_modal').modal('show');
});

$(document).ready(function() {
    $('.ui .item').on('click', function() {
        $('.ui .item').removeClass('active');
        $(this).addClass('active');
    });       
});

