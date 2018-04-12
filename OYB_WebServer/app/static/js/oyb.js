      
  function initMap() {
      var centre = new google.maps.LatLng(53.34,-6.26);      
      var mapOptions = {
        zoom: 14,
        center: centre};
    var map = new google.maps.Map(document.getElementById('map'),mapOptions);
    createMarkers(map);
    
      var input = document.getElementById('pac-input');
      
      
      var searchBox = new google.maps.places.SearchBox(input);

      
        map.addListener('bounds_changed', function() {
          searchBox.setBounds(map.getBounds());
        });
      
      var markers = [];
        // Listen for the event fired when the user selects a prediction and retrieve
        // more details for that place.
        searchBox.addListener('places_changed', function() {
          var places = searchBox.getPlaces();

          if (places.length == 0) {
            return;
          }

          // Clear out the old markers.
          markers.forEach(function(marker) {
            marker.setMap(null);
          });
          markers = [];
      
      
       // For each place, get the icon, name and location.
          var bounds = new google.maps.LatLngBounds();
          places.forEach(function(place) {
            if (!place.geometry) {
              console.log("Returned place contains no geometry");
              return;
            }
            var icon = {
              url: place.icon,
              size: new google.maps.Size(71, 71),
              origin: new google.maps.Point(0, 0),
              anchor: new google.maps.Point(17, 34),
              scaledSize: new google.maps.Size(25, 25)
            };

            // Create a marker for each place.
            markers.push(new google.maps.Marker({
              map: map,
              icon: icon,
              title: place.name,
              position: place.geometry.location
            }));

            if (place.geometry.viewport) {
              // Only geocodes have viewport.
              bounds.union(place.geometry.viewport);
            } else {
              bounds.extend(place.geometry.location);
            }
          });
          map.fitBounds(bounds);
        });
         
      
  } // end initMap
                  
            
 function createMarkers(map){
     
     $.getJSON('http://127.0.0.1:5000/getjson', function(data)
               {
     console.log("success", data);
         var names = data.c.name;
         var available_bikes = data.c.available_bikes;
         var free_stands = data.c.free_stands;
         var lat = data.c.lat;
         var lng = data.c.lng;
         var number = data.c.number;
         
         //(i in data)
         // (var i = 0; i < coords.length; i++)
            for (var i = 0; i < names.length; i++)
            {                     
                     
               var marker = new google.maps.Marker({
            position: {
                lat:lat[i],
                lng:lng[i]   
            }, // end position brackets
            map: map
          }); 
                
        attachContent(marker, names[i], available_bikes[i], free_stands[i], number[i]);

            } // end for loop
     
         
     })// end function data
         .done(function() {
console.log( "second success" );
})
  .fail(function() {
console.log( "error" );
})   
     
  .always(function() {
console.log( "complete" );
});   
     
 }// end function createMarkers
            
            
            // Attaches an info window to a marker with the provided station info. When the
      // marker is clicked, the info window will open with the station info.
      function attachContent(marker, names, avbikes, freestands, number) {
        var infowindow = new google.maps.InfoWindow({
          content: "<b>Station: </b>" + names + "<br>" + "<b>Station No: </b>" + number + "<br><b>Available bikes: </b>" + avbikes + "<br>"+ "<b>Free stands: </b>" + freestands
        });

          
        marker.addListener('click', function() {
            infowindow.close(marker.get('map'), marker);
          infowindow.open(marker.get('map'), marker);
        });
      }   // end function attachContent         
                
       
         function myFunction() {
    alert("WEATHER INFO GOES HERE!!!");
}

 
function on() {
    document.getElementById("overlay").style.display = "block";
}

function off() {
    document.getElementById("overlay").style.display = "none";
}


    