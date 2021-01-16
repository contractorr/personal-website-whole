// Open and close sidebar
function toggleNav(x) {
	if (document.getElementById("myNavPanel").style.width == "100%") {
		document.getElementById("myNavPanel").style.width = "0%";
	}	else {
		document.getElementById("myNavPanel").style.width = "100%";
	}
	x.classList.toggle("change");	
}

function messageSent() {
	alert("Message sent");
  }