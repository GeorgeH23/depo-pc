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
            this_val.html("✔");
            if(response.bool === true) {
                console.log("Added to favorite...");
                // Store the product ID in local storage
                let favoriteItems = JSON.parse(localStorage.getItem('favorite')) || [];
                favoriteItems.push(product_id);
                localStorage.setItem('favorite', JSON.stringify(favoriteItems));
            }
        }
    });
});

$(document).on("click", ".delete-favorite-product", function() {
    let favorite_id = $(this).attr("data-favorite-product");
    let this_val = $(this);

    console.log("favorite id is: ", favorite_id);

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

// $(document).on("click", ".delete-favorite-product", function() {
//     let product_id = $(this).data("favorite-product");
//     let removeFromFavoriteUrl = `/remove-from-favorite/${product_id}/`;

//     $.ajax({
//         url: removeFromFavoriteUrl,
//         type: "GET",
//         dataType: "json",
//         success: function(response) {
//             if (response.bool === true) {
//                 // Remove the card containing the removed product from the favorite list
//                 $(this).closest('.col-md-6').remove();
//             } else {
//                 console.log(response.message);
//             }
//         },
//         error: function(xhr, status, error) {
//             console.error("Error:", error);
//         }
//     });
// });


