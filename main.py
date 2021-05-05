
import plotly.express as px
import geopandas as gpd

geo_df = gpd.read_file(gpd.datasets.get_path('naturalearth_cities'))

px.set_mapbox_access_token(open("pk.eyJ1IjoidGhlYXBwbGVvbmUiLCJhIjoiY2tvYzBqYzljMWoybTJ2bXUzOW56Nm44YSJ9.g6ooCrImGr3EN337C8uY5Q").read())
fig = px.scatter_mapbox(geo_df,
                        lat=geo_df.geometry.y,
                        lon=geo_df.geometry.x,
                        hover_name="name",
                        zoom=1)
fig.show()
