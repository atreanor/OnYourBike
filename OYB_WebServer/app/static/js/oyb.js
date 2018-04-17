      // NB map code and marker code and are all adapted from googlemaps api tutorial code
  function initMap() {
      var centre = new google.maps.LatLng(53.34,-6.26);      
      var mapOptions = {
        zoom: 14,
        center: centre};
    var map = new google.maps.Map(document.getElementById('map'),mapOptions);
    createMarkers(map);
    
      var input = document.getElementById('pac-input');
      
      // The following code from googlemaps tutorial adds a search box and formats it so that a marker will appear on our map to tell user where the street they are looking for is
      var searchBox = new google.maps.places.SearchBox(input);
        map.addListener('bounds_changed', function() {
          searchBox.setBounds(map.getBounds());
        });
      var markers = [];
        searchBox.addListener('places_changed', function() {
          var places = searchBox.getPlaces();

          if (places.length == 0) {
            return; }
          markers.forEach(function(marker) {
            marker.setMap(null);
          });
          markers = [];
      
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

            markers.push(new google.maps.Marker({
              map: map,
              icon: icon,
              title: place.name,
              position: place.geometry.location
            }));

            if (place.geometry.viewport) {
              bounds.union(place.geometry.viewport);
            } else {
              bounds.extend(place.geometry.location);
            }
          });
          map.fitBounds(bounds);
        });
         
      
      
      
      
  } // end initMap
     

var infowindow = new google.maps.InfoWindow();
            
 function createMarkers(map){
     
     $.getJSON('http://127.0.0.1:5000/getStations', function(data)
               {
         
         console.log("success", data);
         
         var size = Object.keys(data.info).length;
           
    
            for (var i = 0; i < size; i++)  
            {                           
            var name = data.info[i].name;   
             var available_bikes = data.info[i].available_bikes;
         var free_stands = data.info[i].available_bike_stands;
         var lat = data.info[i].lat;
         var lng = data.info[i].lng;
         var number = data.info[i].number;   
                

               var marker = new google.maps.Marker({
            position: {
                lat:lat,
                lng:lng   
            }, // end position brackets
            map: map
          }); 
                
      
                
        attachContent(marker, name, available_bikes, free_stands, number);

            
                
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
            




//       Attaches an info window to a marker with the provided station info. When the
//      marker is clicked, the info window will open with the station info.
      function attachContent(marker, name, avbikes, freestands, number) {

                  var content =  "<b>Station: </b>" + name + "<br>" + "<b>Station No: </b>" + number + "<br><b>Available bikes: </b>" + avbikes + "<br>"+ "<b>Free stands: </b>" + freestands
     
        google.maps.event.addListener(marker, 'click', function() {
   infowindow.setContent(content);
   infowindow.open(map, this);
});
          
    
       
      }   // end function attachContent         
               
       
                      
                           
                           
  
function on() {
    document.getElementById("overlay").style.display = "block";
}

function off() {
    document.getElementById("overlay").style.display = "none";
}






function displayWeather(){
     
     $.getJSON('http://127.0.0.1:5000/getweather', function(data)
               {
     console.log("success", data);
   
         
         
         
         var main = data.w.description.main;
         var desc = data.w.description.description;
         var icon = data.w.description.icon;
         var temp = data.w.temp;
         var tempmin = data.w.tempmin;
         
         var weathercontent = "The weather in Dublin: <br><br>" + main + ". Description: " + desc + "<br>Temperature: " + temp + "<br>"+ "Minimum temperature: " + tempmin;
         
         document.getElementById("overlay").innerHTML = weathercontent;
         
         
         
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
     
 }//







    