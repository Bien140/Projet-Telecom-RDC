import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import matplotlib.pyplot as plt

# Colonnes officielles OpenCellID
cols = [
    "radio", "mcc", "net", "area", "cell", "unit",
    "lon", "lat", "range", "samples", "changeable",
    "created", "updated", "averageSignal"
]
# Chargement du fichier des antennes
antenne = pd.read_csv(r"C:\Users\admin\Documents\Documents\Projet Telecom RDC\data\630.csv",
    header=None,
    names=cols,
    compression="infer",
    low_memory=False)
print("Les doublons de l DataFrame antenne sont :", antenne.duplicated().sum())

print(antenne.head())
print(antenne.shape)
print(antenne.isnull().sum())

# Chargement du fichier des provinces
provinces = gpd.read_file(r"C:\Users\admin\Documents\Documents\Projet Telecom RDC\data\gadm41_COD_shp\gadm41_COD_1.shp")
print(provinces.head())
print(provinces["NAME_1"].head())
print(antenne.isnull().sum())

# Chargement du fichier des populations
population = pd.read_csv(r"C:\Users\admin\Documents\Documents\Projet Telecom RDC\data\cod_pd_2020_1km_ASCII_XYZ.csv")
print(population.shape)
print(population.isnull().sum())

print("Les doublons de l DataFrame population sont :", population.duplicated().sum())

geometry_antenne = [Point(x,y) for x,y in zip(antenne["lon"], antenne["lat"])]
geometry_population = [Point(x,y) for x,y in zip(population["X"], population["Y"])]

gdf_antenne = gpd.GeoDataFrame(antenne, geometry=geometry_antenne, crs="EPSG:4326")
gdf_population = gpd.GeoDataFrame(population, geometry=geometry_population, crs="EPSG:4326")

gdf_antenne = gdf_antenne[["radio", "mcc", "net", "area", "cell", "unit","range", "samples", "changeable", "created", "updated", "averageSignal", "geometry"]]
gdf_population = gdf_population[["Z", "geometry"]]

gdf_antenne.to_file("projet_telecom.gpkg",layer="antenne", driver="GPKG")
gdf_population.to_file("projet_telecom.gpkg",layer="population", driver="GPKG")
provinces.to_file("projet_telecom.gpkg",layer="provinces", driver="GPKG")

print(gdf_antenne.isnull().sum())
print(gdf_population.isnull().sum())
print(provinces.isnull().sum())

