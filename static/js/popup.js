document.addEventListener("DOMContentLoaded", function() {    
    // Pop-up message functionality
    var popup = document.getElementById("popup-message");
    var overlay = document.getElementById("overlay");

    if (popup) {
        popup.style.display = "block";
        overlay.style.display = "block";
    }

    var popupClose = document.getElementById("popup-close");
    if (popupClose) {
        popupClose.addEventListener("click", closePopup);
    }
});
function closePopup() {
    document.getElementById("popup-message").style.display = "none";
    document.getElementById("overlay").style.display = "none";
}
    
