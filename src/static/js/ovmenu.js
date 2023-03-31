
/* Open */
function openNav() {
  document.getElementById("myNav").style.height = "100%";
}

/* Close */
function closeNav() {
  document.getElementById("myNav").style.height = "0%";
}
function openNavST() {
  document.getElementById("stopTIME_sec_vote").style.height = "100%";
}

/* Close */
function closeNavST() {
  document.getElementById("stopTIME_sec_vote").style.height = "0%";
}

document.addEventListener('keyup', function(e) {
  if (e.key === "Escape") {
      //modalClose();
      closeNav();
  }
});


