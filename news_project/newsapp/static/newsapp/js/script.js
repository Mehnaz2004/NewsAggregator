let button = document.querySelector("#ChangeMode");
let body = document.querySelector("body");
let articlescontainers = document.querySelectorAll(".articles-container");

button.onclick = changeMode;

function changeMode() {
    if (button.innerText == "🌑") {
        body.style.backgroundColor = "rgb(50, 50, 50)";
        button.innerText = "☀";
        articlescontainers.forEach(container => {
            container.style.backgroundColor = "rgb(73, 73, 73)";
        });
    } else {
        body.style.backgroundColor = "rgb(145, 142, 142)";
        button.innerText = "🌑";
        articlescontainers.forEach(container => {
            container.style.backgroundColor = "rgb(172, 174, 173)";
        });
    }
}

// Wait for the document to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    // Get the search input element
    const searchInput = document.getElementById('search-input');

    // Add an event listener for input changes
    searchInput.addEventListener('input', function() {
        // Get the current search term
        const searchTerm = searchInput.value.trim();

        // Check if search term is not empty
        if (searchTerm !== '') {
            // Select all article headlines
            const headlines = document.querySelectorAll('.article h2, .article p');

            // Loop through each headline
            headlines.forEach(function(headline) {
                // Get the headline text content
                let headlineText = headline.textContent;

                // Handle different elements in different pages
                if (headline.tagName === 'P') {
                    headlineText = headlineText.replace(/<\/?[^>]+(>|$)/g, ''); // Strip HTML tags if present
                }

                // Create a regular expression to match the search term
                const regex = new RegExp('(' + searchTerm + ')', 'gi');

                // Replace the search term with highlighted HTML
                const highlightedText = headlineText.replace(regex, '<mark>$1</mark>');

                // Update the headline HTML with highlighted text
                headline.innerHTML = highlightedText;
            });
        } else {
            // If search term is empty, reset all headlines to original text
            const headlines = document.querySelectorAll('.article h2, .article p');
            headlines.forEach(function(headline) {
                headline.innerHTML = headline.textContent;
            });
        }
    });
});
