import folium
from ipywidgets import interact

# Cloudmade Mapbox needs an API key, Mapbox Control Room is limited to a few levels
tiles = [name.strip() for name in """
    OpenStreetMap
    Mapbox Bright
    Mapbox Control Room
    Stamen Terrain
    Stamen Toner
    Stamen Watercolor
    CartoDB positron
    CartoDB dark_matter""".strip().split('\n')]


@interact(lat=(-90., 90.), lon=(-180., 180.), tiles=tiles, zoom=(1, 18))
def create_map(lat=52.518611, lon=13.408333, tiles="Stamen Toner", zoom=10):
    return folium.Map(location=(lat, lon), tiles=tiles, zoom_start=zoom)
