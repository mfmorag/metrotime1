    function initialize() {
      var marcadores = [
        ['Parada Maternidad Enrique Sotomayor', -2.19556, -79.8903, src="/static/images/par.png"],
	['Articulado', -2.19392, -79.89226, src="/static/images/iconcar.png"]
      ];
      var map = new google.maps.Map(document.getElementById('mapa'), {
        zoom: 18,
        center: new google.maps.LatLng(-2.19494, -79.89136),
        mapTypeId: google.maps.MapTypeId.ROADMAP
      });
      var infowindow = new google.maps.InfoWindow();

      var l1 = new google.maps.LatLng(-2.19597, -79.89044);
      var l2 = new google.maps.LatLng(-2.19553, -79.89272);
      var l3 = new google.maps.LatLng(-2.19392, -79.89226);
      var l4 = new google.maps.LatLng(-2.19445, -79.88992);
      var miRuta = [l1, l2, l3, l4, l1];
      var trazo = new google.maps.Polyline({path:miRuta,strokeColor:"#0000FF",strokeOpacity:0.8,strokeWeight:3});
      trazo.setMap(map);
      var marker, i;
      for (i = 0; i < marcadores.length; i++) {  
        marker = new google.maps.Marker({
          position: new google.maps.LatLng(marcadores[i][1], marcadores[i][2]),
	  icon: marcadores[i][3],
          map: map
        });
	
        google.maps.event.addListener(marker, 'click', (function(marker, i) {
          return function() {
	    infowindow.setContent(marcadores[i][0]); 
            infowindow.open(map, marker);
          }
        })(marker, i));
      }
    }
    google.maps.event.addDomListener(window, 'load', initialize);