function altImage() {
x = document.getElementById("image0").getAttribute("src");
if (x == "src/img/banner-image.jpg")
	x = "src/img/caveavin.jpg";
else
	if (x == "src/img/caveavin.jpg")
		x = "src/img/tonneau.jpg";

document.getElementById("image0").src = x;
console.log(x)
}
window.setInterval("altImage()", 5000);