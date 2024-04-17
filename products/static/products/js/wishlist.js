$(document).on("click", ".add-to-wishlist", function() {
    let product_id = $(this).attr("data-product-item");
    let this_val = $(this);

    // Get the base URL
    let baseUrl = window.location.origin;

    // Construct the URL
    let wishlistUrl = baseUrl + "/products/add-to-wishlist/" + product_id + "/";

    $.ajax({
        url: wishlistUrl,
        data: {
            "id": product_id
        },
        dataType: "json",
        beforeSend: function() {
            console.log("Adding to wishlist");
        },
        success: function(response) {
            this_val.html("✔");
            if(response.bool === true) {
                console.log("Added to wishlist...");
                // Store the product ID in local storage
                let wishlistItems = JSON.parse(localStorage.getItem('wishlist')) || [];
                wishlistItems.push(product_id);
                localStorage.setItem('wishlist', JSON.stringify(wishlistItems));
            }
        }
    });
});
