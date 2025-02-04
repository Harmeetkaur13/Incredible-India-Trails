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
    const editButtons = document.getElementsByClassName("btn-edit");
    const commentText = document.getElementById("id_comment");
    const commentForm = document.getElementById("reviewForm");
    const submitButton = document.getElementById("submitButton");
    const reviewIdInput = document.getElementById("review_id");

    /**
    * Initializes edit functionality for the provided edit buttons.
    * 
    * For each button in the `editButtons` collection:
    * - Retrieves the associated review's ID upon click.
    * - Fetches the content of the corresponding review.
    * - Populates the `commentText` input/textarea with the review's content for editing.
    * - Updates the submit button's text to "Update".
    * - Sets the form's action attribute to the `edit_review/{reviewId}` endpoint.
    */
    for (let button of editButtons) {
        button.addEventListener("click", (e) => {
            let reviewId = e.target.getAttribute("data-review_id");
            let destinationName = e.target.getAttribute("data-destination_name");
            let reviewElement = document.getElementById(`review${reviewId}`);

            if (!reviewElement) return;

            let reviewContent = reviewElement.innerText.trim();
            commentText.value = reviewContent;
            submitButton.innerText = "Update";
            reviewIdInput.value = reviewId;

            // Set the form action to include the destination name and review ID
            commentForm.setAttribute("action", `/destination/${destinationName}/edit_review/${reviewId}/`);

            // Extract the review rating by counting filled stars
            let stars = reviewElement.querySelectorAll(".rating i.fas");
            let reviewRating = stars.length; // Number of filled stars

            // Set the rating
            document.querySelectorAll(".star-rating input").forEach(input => {
                input.checked = input.value == reviewRating;
            });
            document.querySelectorAll(".star-rating label").forEach((label, index) => {
                label.style.color = index > reviewRating ? "gold" : "#ddd";
            });
        });
    }
});    
    
