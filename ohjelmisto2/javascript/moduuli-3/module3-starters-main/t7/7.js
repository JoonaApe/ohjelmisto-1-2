const image = document.getElementById("target");
const p = document.getElementById("trigger");

p.addEventListener('mouseenter', function() {
  image.src = "img/picB.jpg";
});

p.addEventListener('mouseleave', function(){
  image.src="img/picA.jpg";
});