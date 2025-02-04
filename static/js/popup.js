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
    const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
    const deleteButtons = document.getElementsByClassName("btn-delete");
    const deleteConfirm = document.getElementById("deleteConfirm");
    /**
    * Initializes deletion functionality for the provided delete buttons.
    * 
    * For each button in the `deleteButtons` collection:
    * - Retrieves the associated comment's ID upon click.
    * - Updates the `deleteConfirm` link's href to point to the 
    * deletion endpoint for the specific comment.
    * - Displays a confirmation modal (`deleteModal`) to prompt 
    * the user for confirmation before deletion.
    */
    for (let button of deleteButtons) {
        button.addEventListener("click", (e) => {
          let reviewId = e.target.getAttribute("data-review_id");
          deleteConfirm.href = `delete_review/${reviewId}`;
          deleteModal.show();
        });
      }
    
});
