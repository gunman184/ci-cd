// Define the API Gateway URL (Replace this with your actual API URL)
const apiUrl = "https://5rx2ovxoi9.execute-api.us-east-1.amazonaws.com/production/api_processing";

// Function to retrieve the current visit count
function getVisitCount() {
    fetch(apiUrl)  // Send GET request to the API
        .then(response => response.json())  // Parse the JSON response
        .then(data => {
            // Set the visit count inside the HTML element with id="visitCount"
            document.getElementById("visitCount").textContent = data.visit_count;
        })
        .catch(error => {
            console.error('Error fetching visit count:', error);
            alert('Error fetching visit count');
        });
}

// Function to increment the visit count
function incrementVisits() {
    fetch(apiUrl, {
        method: "POST",  // POST request to increment the count
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({}) // Empty body for the increment request
    })
    .then(response => response.json())
    .then(data => {
        // Update the visit count on successful POST request
        document.getElementById("visitCount").textContent = data.visit_count;
    })
    .catch(error => {
        console.error('Error incrementing visit count:', error);
        alert('Error incrementing visit count');
    });
}

// Automatically increment visits when the page loads
window.onload = function() {
    incrementVisits();  // Increment the visit count
    getVisitCount();    // Get and display the current visit count
};