import folium

# Create a map centered around the mean coordinates of your data
mean_lat = points_df['latitude'].mean()
mean_lon = points_df['longitude'].mean()
mymap = folium.Map(location=[mean_lat, mean_lon], zoom_start=10)

# Iterate through each point and add it to the map
for _, row in points_df.iterrows():
    folium.Marker(
        location=[row['latitude'], row['longitude']], 
        popup=row['h3_index']
    ).add_to(mymap)

# Display the map
mymap

