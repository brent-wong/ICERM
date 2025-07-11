import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import os

os.environ['SHAPE_RESTORE_SHX'] = 'YES'

gdf = gpd.read_file('/Users/brent/ICERM/Providence_Borders1.shp')

fig, ax = plt.subplots(figsize=(10, 10))
gdf.plot(ax=ax, color='lightgray', edgecolor='black')

points = pd.read_csv("ICERM Project Data - Providence SNAP Vendors.csv")
latitude = points["Latitude"]
longitude = points["Longitude"]
storetype = points.groupby("Proposed_new_category")
storetype.get_group("Convenience Store").plot.scatter(x='Longitude', y='Latitude', s=50, c='blue', ax=ax, label = "Convenience Store")
storetype.get_group("Corner Store").plot.scatter(x='Longitude', y='Latitude', s=50, c='green', ax=ax, label = "Corner Store")
storetype.get_group("Grocery Store").plot.scatter(x='Longitude', y='Latitude', s=50, c='red', ax=ax, label = "Grocery Store")
storetype.get_group("Superstore").plot.scatter(x='Longitude', y='Latitude', s=50, c='yellow', ax=ax, label = "Superstore")
storetype.get_group("Meat Market").plot.scatter(x='Longitude', y='Latitude', s=50, c='magenta', ax=ax, label = "Meat Market")
storetype.get_group("Farmers Market").plot.scatter(x='Longitude', y='Latitude', s=50, c='orange', ax=ax, label = "Farmers Market")
storetype.get_group("Bakery").plot.scatter(x='Longitude', y='Latitude', s=50, c='brown', ax=ax, label = "Bakery")
plt.xlabel("Longitude")
plt.title("Map of SNAP Vendors in Providence, RI")
plt.legend(loc = "lower left")
plt.tight_layout()
plt.show()