import folium
import geopandas as gpd

# Assuming you have the 'geo_to_h3' function defined somewhere

# Convert the GeoDataFrame to H3 hexagons
dfh3 = gdf.h3.geo_to_h3(12)

# Create a map centered around the mean coordinates of your data
mean_lat = dfh3.geometry.centroid.y.mean()
mean_lon = dfh3.geometry.centroid.x.mean()
mymap = folium.Map(location=[mean_lat, mean_lon], zoom_start=10)

# Iterate through each hexagon and add it to the map
for _, row in dfh3.iterrows():
    geojson = row.geometry.__geo_interface__
    folium.GeoJson(
        geojson,
        style_function=lambda feature: {
            'fillColor': 'blue',  # Set the fill color of hexagons
            'color': 'black',     # Set the border color
            'weight': 1,          # Set the border weight
            'fillOpacity': 0.3,   # Set the opacity of hexagons
        },
    ).add_to(mymap)

# Display the map
mymap
