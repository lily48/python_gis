import folium

# Create a map centered around the mean coordinates of your data
mean_lat = dfh3.geometry.centroid.y.mean()
mean_lon = dfh3.geometry.centroid.x.mean()
mymap = folium.Map(location=[mean_lat, mean_lon], zoom_start=10)

# Iterate through each polygon and add it to the map
for _, row in dfh3.iterrows():
    h3_index = row['h3_index']  # Assuming 'h3_index' is the column name storing the H3 index
    geojson = row.geometry.__geo_interface__
    folium.GeoJson(
        geojson,
        name=h3_index,  # Set the name of the GeoJson layer to the H3 index
    ).add_to(mymap)

# Add layer control to the map
folium.LayerControl().add_to(mymap)

# Display the map
mymap
