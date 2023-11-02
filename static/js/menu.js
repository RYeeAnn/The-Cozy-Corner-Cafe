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
