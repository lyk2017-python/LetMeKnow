function init() {
    window.addEventListener('scroll', function(e){
        var distanceY = window.pageYOffset || document.documentElement.scrollTop,
            shrinkOn = 80,
            header = document.querySelector("header");
            var curr = document.getElementsByClassName("current");
            var back = document.getElementsByClassName("back");
            var firstBig = back[0].offsetWidth; //143
            var smalX = curr[0].offsetWidth; //143
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
