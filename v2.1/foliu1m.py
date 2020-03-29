import folium

m = folium.Map(
    location=[37.5838699,127.0565831],
    zoom_start=15
)

m.save('map.html')
