
// Search function
document.getElementById("menuSearch").addEventListener("keyup", function() {
    // Get the value of the input field
    const query = this.value.toLowerCase();
    
    // Get all menu item names
    const items = document.querySelectorAll(".menu__item-name");

    // Loop through all items and hide those that don't match the search query
    items.forEach(function(item) {
        if (item.textContent.toLowerCase().indexOf(query) > -1) {
            item.parentElement.style.display = "";
        } else {
            item.parentElement.style.display = "none";
        }
    });
});



// Get modal and list items
const modal = document.getElementById("modal");
const listItems = document.querySelectorAll(".menu__list > li");

// When the user clicks on a list item, open the modal
document.querySelectorAll(".menu__list > li").forEach(li => {
    li.addEventListener('click', function() {
        // Find the .menu__item-name element within the clicked li
        const itemNameDiv = this.querySelector(".menu__item-name");

        // Get the data attributes from the .menu__item-name element
        const itemName = itemNameDiv.getAttribute("data-modal-trigger");
        const itemDescription = itemNameDiv.getAttribute("data-description") || 'No description'; // Fallback in case there is no description
        const itemPrice = itemNameDiv.parentElement.querySelector(".menu__item-price").textContent;
        const itemImage = itemNameDiv.getAttribute("data-image");

        // Set the modal content
        document.getElementById("modalName").textContent = itemName;
        document.getElementById("modalDescription").textContent = itemDescription;
        document.getElementById("modalPrice").textContent = itemPrice;
        document.getElementById("modalImage").src = itemImage;

        // Display the modal
        modal.style.display = "block";
    });
});

// Get the <span> element that closes the modal
const span = document.getElementsByClassName("close")[0];

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
    modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}
