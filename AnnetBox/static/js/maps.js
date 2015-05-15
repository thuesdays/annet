/**
 * Created by n_kovganko on 15.05.2015.
 */
function LoadGmaps() {
            var myLatlng = new google.maps.LatLng(50.5273670, 30.5124010);
            var myOptions = {
                zoom: 16,
                center: myLatlng,
                disableDefaultUI: true,
                panControl: true,
                zoomControl: true,
                zoomControlOptions: {
                    style: google.maps.ZoomControlStyle.DEFAULT
                },

                mapTypeControl: true,
                mapTypeControlOptions: {
                    style: google.maps.MapTypeControlStyle.HORIZONTAL_BAR
                },
                streetViewControl: true,
                mapTypeId: google.maps.MapTypeId.ROADMAP
            };
            var map = new google.maps.Map(document.getElementById("MyGmaps"), myOptions);
            var marker = new google.maps.Marker({
                position: myLatlng,
                map: map,
                title: "Северная 50, Киев"
            });
            var infowindow = new google.maps.InfoWindow({
                content: "Annet-Studio, Салон красоты"
            });
            google.maps.event.addListener(marker, "click", function () {
                infowindow.open(map, marker);
            });
        }