$(document).on("click", ".add-to-favorite", function() {
    let product_id = $(this).attr("data-prod-item");
    let this_val = $(this);

    // Get the base URL
    let baseUrl = window.location.origin;

    // Construct the URL
    let favoriteUrl = baseUrl + "/products/add-to-favorite/" + product_id + "/";

    $.ajax({
        url: favoriteUrl,
        data: {
            "id": product_id
        },
        dataType: "json",
        beforeSend: function() {
            console.log("Adding to favorite");
        },
        success: function(response) {
            if(response.bool === true) {
                console.log("Added to favorite...");
                // Store the product ID in local storage
                let favoriteItems = JSON.parse(localStorage.getItem('favorite')) || [];
                favoriteItems.push(product_id);
                localStorage.setItem('favorite', JSON.stringify(favoriteItems));
            }
            window.location.reload();
        }
    });
});

$(document).on("click", ".delete-favorite-product", function() {
    let favorite_id = $(this).attr("data-favorite-product");
    let this_val = $(this);

    // Get the base URL
    let baseUrl = window.location.origin;

    // Construct the URL
    let removeFromFavoriteUrl = baseUrl + "/products/remove-from-favorite/" + product_id + "/";

    $.ajax({
        url: removeFromFavoriteUrl,
        data: {
            "id": favorite_id
        },
        dataType: "json",
        beforeSend: function() {
            console.log("Removing from favorite...");
        },
        success: function(response) {
            $("#favorite-list").html(response.data)
        }
    });
});
