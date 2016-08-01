    function initialize() {
      var marcadores = [
        ['bus1', -2.14989, -79.88129, src="/static/images/iconcar.png"],
        ['bus1', -2.15761, -79.88691, src="/static/images/iconcar.png"],
        ['bus1', -2.16602, -79.89103, src="/static/images/iconcar.png"],
        ['bus1', -2.17494, -79.89309, src="/static/images/iconcar.png"],
          ['bus2', -2.14114, -79.89463, src="/static/images/iconcar.png"],
        ['bus2', -2.13154, -79.89858, src="/static/images/iconcar.png"],
	      ['bus3', -2.11919, -79.92055, src="/static/images/iconcar.png"],
        ['bus2', -2.13154, -79.89858, src="/static/images/iconcar.png"],
        ['bus3', -2.10769, -79.90682, src="/static/images/iconcar.png"],
        ['bus2', -2.14766, -79.92828, src="/static/images/iconcar.png"],
        ['bus3', -2.16619, -79.93806, src="/static/images/iconcar.png"],
        ['bus2', -2.19792, -79.8991, src="/static/images/iconcar.png"],
        ['bus3', -2.2041, -79.92038, src="/static/images/iconcar.png"]	
      ];
      var map = new google.maps.Map(document.getElementById('mapa'), {
        zoom: 14,
        center: new google.maps.LatLng(-2.16876, -79.91317),
        mapTypeId: google.maps.MapTypeId.ROADMAP
      });

      var infowindow = new google.maps.InfoWindow();
 var marker, i;
      for (i = 0; i < marcadores.length; i++) {  
        marker = new google.maps.Marker({
          position: new google.maps.LatLng(marcadores[i][1], marcadores[i][2]),
          icon: marcadores[i][3],
          map: map,
          animation: google.maps.Animation.BOUNCE      
        });
      }
    }
    google.maps.event.addDomListener(window, 'load', initialize);