import folium


m = folium.Map(location=[45.5236, -122.6750])
m.save("index.html")

folium.Map(location=[45.5236, -122.6750], zoom_start=13)
