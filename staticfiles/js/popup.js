document.addEventListener("DOMContentLoaded", function() {
    let stars = document.querySelectorAll(".rating label");

    stars.forEach(star => {
        star.addEventListener("click", function() {
            let value = this.previousElementSibling.value;
            document.querySelectorAll(".rating label").forEach(label => {
                label.style.color = "#ddd"; // Reset all stars
            });
            for (let i = 0; i < value; i++) {
                stars[i].style.color = "gold"; // Highlight selected stars
            }
        });
    });
});