
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

var myWidget = cloudinary.createUploadWidget({
    cloudName: 'dvk80uh1a', 
    uploadPreset: 'fave3ym3'}, (error, result) => { 
        if (!error && result && result.event === "success") { 
            console.log('Done! Here is the image info: ', result.info); 
        }
    }
)

document.getElementById("upload_widget").addEventListener("click", function(){
    myWidget.open();
}, false);