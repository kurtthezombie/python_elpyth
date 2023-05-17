Webcam.set({
    width: 320,
    height: 240,
    image_type: 'jpeg',
    jpeg_quality: 90 
});
Webcam.attach("#my_camera");

function take_snapshot() {
    Webcam.snap(function(data_uri){
        document.getElementById('result').innerHTML="<img id='imageprev' src='"+data_uri+"'>";
    });
}

function save_snapshot() {
    var base64image = document.getElementById('imageprev').src;
    var idno = document.getElementById('idno').value;
    
    Webcam.upload(base64image,"upload?idno="+idno
    ,function(code,name){
        alert('image uploaded...');
    });
    
}