function initMap() {
  // function to create & initialise Google map
  var centre = new google.maps.LatLng(53.34,-6.26);      
  var mapOptions = {zoom: 14, center: centre};
  var map = new google.maps.Map(document.getElementById('map'),mapOptions);
  createMarkers(map);
  displayWeather();
    
    
	var input = document.getElementById('pac-input');
      
  // The following code adds a search box & formats it so that a marker will 
  // appear on our map to tell user where the street they are looking for is
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

// -----------------------------------------------------------------------------   
// The following code creates the markers. It also calls the 'attachContent' function, which  places content on the infowindow
function createMarkers(map){

 	$.getJSON($SCRIPT_ROOT + '/getStations', function(data) {
    console.log("success", data);
    var size = Object.keys(data.info).length;
    for (var i = 0; i < size; i++) {                           
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
         
  .done(function() { console.log( "second success" );
  })
  .fail(function() { console.log( "error" );
  })    
  .always(function() { console.log( "complete" );
  });   
}// end function createMarkers
            
//-----------------------------------------------------------------------------          
// Attaches an info window to a marker with the provided station info. When the
// marker is clicked, the info window will open with the station info.
function attachContent(marker, name, avbikes, freestands, number) {
  var content =  "<b>Station: </b>" + name + "<br>" + "<b>Station No: </b>" + number + "<br><b>Available bikes: </b>" + avbikes + "<br>"+ "<b>Free stands: </b>" + freestands + "<br><button onclick='drawChart(" + number + ")'>More info</button>";
    
    
     
  google.maps.event.addListener(marker, 'click', function() {
  infowindow.setContent(content);

  
  infowindow.open(map, this);
  });
       
} // end function attachContent         
                                      


//---------------------------------------------------------------------------
// function to display weather.
function displayWeather(){
  // jquery to retrieve json data
  $.getJSON($SCRIPT_ROOT + '/getweather', function(data) {
    console.log("success", data);
    var main = data.weather[0].w_d_main;
    var desc = data.weather[0].w_description;
    var temp = data.weather[0].temp;
    var tempmin = data.weather[0].temp_min;
    var icon = data.weather[0].w_d_icon;
    console.log(typeof icon);
         
    var weathercontent = "The weather in Dublin: <br><h3>" + main + 
    "</h3><img height = '90px' src='http://openweathermap.org/img/w/" + icon + ".png'><br>"+
    "Description: " + desc + "<br>Temperature: " + temp + "<br>"+ "Minimum temperature: " + tempmin;
         

    document.getElementById("weatherhere").innerHTML = weathercontent;   
      
  })
    // end function data
  .done(function() { console.log( "second success" );
  })
  .fail(function() { console.log( "error" );
  })   
  .always(function() { console.log( "complete" );
  });   
     
}// end function displayWeather




// from google charts tutorial - basic chart showing number of bike station (activated by button on infowindow relating to that station)


    function drawChart(number) {
        var data = google.visualization.arrayToDataTable([
          ['Available Bikes', 'Available Stands'],
          [number, 55]
        ]);

        var options = {
          chart: {
            title: 'Company Performance',
            subtitle: 'Sales, Expenses, and Profit: 2014-2017',
          }
        };

        var chart = new google.charts.Bar(document.getElementById('myPieChart'));

        chart.draw(data, google.charts.Bar.convertOptions(options));
      }
    
 










    
