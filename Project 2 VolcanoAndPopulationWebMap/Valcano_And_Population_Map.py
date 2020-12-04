import folium
import pandas
data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])#make longtitudes into the lon python list
elev = list(data["ELEV"])
v_name = list(data["NAME"])

def define_color(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

map = folium.Map(location=[37.455310,-122.15105],zoom_start=5,tiles = "CartoDB positron")
#Volcanos layer below
fg = folium.FeatureGroup(name="Volcanos")
for la,lo,el,vn in zip(lat,lon,elev,v_name):
    iframe = folium.IFrame(html=html % (vn, vn, el), width = 200, height = 100)
    fg.add_child(folium.CircleMarker(location=[la,lo],radius = 7,popup=folium.Popup(iframe),
    color=define_color(el),opacity=0.5, fill_color=define_color(el), fill_opacity=0.5))
    #fg.add_child(folium.Marker(location=[la,lo],popup=folium.Popup(iframe),icon=folium.Icon(color=define_color(el))))
fg.add_child(folium.Marker(location=[37.455310,-122.15105],popup="3 Crows",icon=folium.Icon(color='beige')))
#population layer below
fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),
style_function = lambda x: {'fillColor':'green' if x["properties"]["POP2005"] < 20000000  
else 'orange' if 20000000 <= x["properties"]["POP2005"] < 50000000 
else 'red'} ))


map.add_child(fg) #add the feature group tp map as a child
map.add_child(fgp)
map.add_child(folium.LayerControl()) #This will enable us to control layers by different feature groups
map.save("Volcano Maps.html")
