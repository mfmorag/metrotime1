    function initialize1() {

        var map = new google.maps.Map(document.getElementById('mapa'), {
            zoom: 15,
            center: new google.maps.LatLng(-2.13657, -79.89571),
            mapTypeId: google.maps.MapTypeId.ROADMAP
        });
        var markers = [];

         function datos() {
        $.ajax({
            url: "/transporte/listapar/1/",
            dataType: "json",
            type: "POST",
            success: function (data) {
                var puntos = data[0];
                var paradas = data[1];
                var infowindow = new google.maps.InfoWindow();

                for (var j = 0; j < paradas.length; j++) {
                    marker = new google.maps.Marker({
                        position: new google.maps.LatLng(paradas[j]['latitud'], paradas[j]['longitud']),
                        map: map,
                        icon: src = "/static/images/parada.png"
                    });

                    google.maps.event.addListener(marker, 'click', (function (marker, j) {
                        return function () {
                            infowindow.setContent(paradas[j]['nombre']);
                            infowindow.open(map, marker);
                        }
                    })(marker, j));
                }

                for (var i = 0; i < puntos.length - 1; i++) {
                    var l1 = new google.maps.LatLng(puntos[i]['r_list']['rlat'], puntos[i]['r_list']['rlong']);
                    var l2 = new google.maps.LatLng(puntos[i + 1]['r_list']['rlat'], puntos[i + 1]['r_list']['rlong']);
                    var miRuta = [l1, l2];
                    var trazo = new google.maps.Polyline({
                        path: miRuta,
                        strokeColor: "#0000FF",
                        strokeOpacity: 0.8,
                        strokeWeight: 3
                    });
                    trazo.setMap(map);
                }
            }
        });
    }
            datos();

            function posicion_car() {
            $.ajax({
            url:"/transporte/lcar/1/",
            dataType:"json",
            type: "POST",
            success: function(data){
                    var posicion = data;
                    for (var i = 0; i < posicion.length; i++) {
                        var carros =posicion[i]['pos'];
                        for (var j = 0; j < carros.length; j++) {
                            var vehiculo= carros[j];
                            if (vehiculo.length!=0){
                                var pos = carros.length;
                                var finalpos = pos - 1;
                                var veh= carros[finalpos];
                                addMarker(new google.maps.LatLng(veh['latitud'], veh['longitud']));
                                j=carros.length;
                            }
                        }
                    }
                }
            });
            showMarkers();
            deleteMarkers();
        }

        function addMarker(location) {
            var marker = new google.maps.Marker({
                position: location,
                map: map,
                icon:src="/static/images/iconcar.png"
                });
                markers.push(marker);
        }

        function setMapOnAll(map) {
            for (var i = 0; i < markers.length; i++) {
            markers[i].setMap(map);
            }
        }

        function showMarkers() {
            setMapOnAll(map);
        }

        function clearMarkers() {
            setMapOnAll(null);
        }

        function deleteMarkers() {
            clearMarkers();
            markers = [];
        }

        setInterval(posicion_car,4000);
    }
    
    google.maps.event.addDomListener(window, 'load', initialize1);

