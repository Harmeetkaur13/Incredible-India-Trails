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
function showMessage(message) {
    document.getElementById('popup-text').innerText = message;
    document.getElementById('popup-message').style.display = 'block';
}

document.getElementById('popup-close').addEventListener('click', function() {
    document.getElementById('popup-message').style.display = 'none';
});

function validateForm() {
    console.log("validateForm called"); // Debug statement
    const rating = document.querySelector('input[name="rating"]:checked');
    if (!rating) {
        alert("Please select a rating before submitting your review.");
        return false;
    }
    return true;
}