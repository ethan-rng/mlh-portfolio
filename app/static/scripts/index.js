


// Map Functionality Stuff
document.addEventListener('DOMContentLoaded', function() {
    var map = L.map('maparea').setView([39.7837304, -100.445882], 3);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '© OpenStreetMap'
    }).addTo(map);

    // Hospital LMAO
    var marker = L.marker([43.7688, -79.3627]).addTo(map);
    marker.bindPopup("<h2 style='color:black;'>North York General Hospital</h2><h3 style='color:black;'>Where it all started. 20 years ago almost to the day i magically  &#127849;</h3>");

    // Honolulu
    var marker = L.marker([21.3099, -157.8581]).addTo(map);
    marker.bindPopup("<h2 style='color:black;'>Honolulu, HA</h2><h3 style='color:black;'>I'm a Queens native and proud of it! Having lived here all my life, I've done pretty much all of the classic touristy stuff for NYC: went to a Broadway Show, walked the Brooklyn Bridge, been to the top of the Empire State Building, etc. I love going to Chinatown, K-Town and Flushing to try new restaurants or dessert places &#127849;</h3>");

    // Rome
    var marker = L.marker([41.8967, 12.4822]).addTo(map);
    marker.bindPopup("<h2 style='color:black;'>Rome, Italy</h2><h3 style='color:black;'>Went to Venice Beach &#127796; and Hollywood</h3>");

    // Tokyo
    var marker = L.marker([35.6764, 139.6500]).addTo(map);
    marker.bindPopup("<h2 style='color:black;'>Tokoyo, Japan</h3><h3 style='color:black;'>Came here last summer for an internship and had the best BBQ &#129316;</h3>");

    // Vancouver
    var marker = L.marker([49.2827, -123.1207]).addTo(map);
    marker.bindPopup("<h2 style='color:black;'>Vancouver, BC</h2><h3 style='color:black;'>Stood on the equator!</h3>");

    // Cancun
    var marker = L.marker([21.1619, -86.8515]).addTo(map);
    marker.bindPopup("<h2 style='color:black;'>Cancun, Mexico</h2><h3 style='color:black;'>A cool place !</h3>");
});