// This goes inside your menu.js file

// Search function
document.getElementById("menuSearch").addEventListener("keyup", function() {
    // Get the value of the input field
    var query = this.value.toLowerCase();
    
    // Get all menu item names
    var items = document.querySelectorAll(".menu__item-name");

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
var modal = document.getElementById("modal");
var listItems = document.querySelectorAll(".menu__list > li");

// When the user clicks on a list item, open the modal
listItems.forEach(item => {
    item.onclick = function() {
        var btn = item.querySelector(".menu__item-name");
        modal.style.display = "block";
        document.getElementById("modalName").textContent = btn.getAttribute("data-modal-trigger");
        document.getElementById("modalDescription").textContent = btn.getAttribute("data-description");
        document.getElementById("modalPrice").textContent = btn.querySelector(".menu__item-price").textContent;
        document.getElementById("modalImage").src = btn.getAttribute("data-image");
    }
});

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

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
