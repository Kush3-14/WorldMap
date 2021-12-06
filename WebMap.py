import folium
import pandas
import json

data = pandas.read_csv("E:\Coding\PythonProjects\WebMap\Volcano_db.csv",encoding='latin-1')
lat = list(data["Latitude"])
lon = list(data["Longitude"])
elev = list(data["Elev"])

def colour_pro(elevation):
    if elevation<1000:
        return 'green'
    elif 1000<=elevation<3000 :
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[25.0961, 85.3131], zoom_start=6, titles="Mapbox Bright")

fgV = folium.FeatureGroup(name="Volcanoes")

for lt,ln,el in zip(lat, lon, elev):
    fgV.add_child(folium.Marker(location=[lt, ln], popup=str(el)+'m', icon=folium.Icon(color=colour_pro(el))))

fgV.add_child(folium.Marker(location=[26.3483, 86.0712], popup="Madhubani", icon=folium.Icon(color="blue")))
fgV.add_child(folium.Marker(location=[22.5726, 88.3639], popup="Kolkata", icon=folium.Icon(color="blue")))

fgP = folium.FeatureGroup(name="Population")
json_file_path = "E:\Coding\PythonProjects\WebMap\world.json"
fgP.add_child(folium.GeoJson(open(json_file_path,'r',encoding='utf-8-sig').read(),style_function=lambda x:{'fillColor':'green' if x['properties']['POP2005']<10000000 else 'orange' if 10000000 <= x['properties']['POP2005']<20000000 else 'red'}))

map.add_child(fgV)
map.add_child(fgP)
map.add_child(folium.LayerControl())

map.save("India.html")
