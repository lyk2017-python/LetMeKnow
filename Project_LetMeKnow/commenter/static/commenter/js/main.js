function init() {
    window.addEventListener('scroll', function(e){
        var distanceY = window.pageYOffset || document.documentElement.scrollTop,
            shrinkOn = 80,
            header = document.querySelector("header");
        if (distanceY > shrinkOn) {
            classie.add(header,"smaller");
        } else {

            if (classie.has(header,"smaller")) {
                classie.remove(header,"smaller");
            }
        }
        document.getElementsByClassName("back")[0].style.width = document.getElementsByClassName("current")[0].offsetWidth +"px";   });
}
window.onload = init();



$(function() {
      $("#lava_menu").lavaLamp({
        fx: "linear",
        speed: 300
      });
    });


function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
