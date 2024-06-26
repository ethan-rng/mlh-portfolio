


// Map Functionality Stuff
document.addEventListener('DOMContentLoaded', function() {
    var map = L.map('maparea').setView([39.7837304, -100.445882], 3);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '© OpenStreetMap'
    }).addTo(map);

    // Hospital LMAO
    var marker = L.marker([14.5995, 120.9842]).addTo(map);
    marker.bindPopup("<h2 style='color:black;'>Manilla, Philippines</h2><h3 style='color:black;'>lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</h3>");

    // Honolulu
    var marker = L.marker([21.3099, -157.8581]).addTo(map);
    marker.bindPopup("<h2 style='color:black;'>Honolulu, HA</h2><h3 style='color:black;'>lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</h3>");

    // Rome
    var marker = L.marker([41.8967, 12.4822]).addTo(map);
    marker.bindPopup("<h2 style='color:black;'>Rome, Italy</h2><h3 style='color:black;'>lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</h3>");

    // Tokyo
    var marker = L.marker([35.6764, 139.6500]).addTo(map);
    marker.bindPopup("<h2 style='color:black;'>Tokyo, Japan</h3><h3 style='color:black;'>lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</h3>");

    // Vancouver
    var marker = L.marker([49.2827, -123.1207]).addTo(map);
    marker.bindPopup("<h2 style='color:black;'>Vancouver, BC</h2><h3 style='color:black;'>lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</h3>");

    // Cancun
    var marker = L.marker([21.1619, -86.8515]).addTo(map);
    marker.bindPopup("<h2 style='color:black;'>Cancun, Mexico</h2><h3 style='color:black;'>lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</h3>");
});