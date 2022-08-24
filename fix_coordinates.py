# We have coordinates for shops in file Raw-Shops-Deliveries
# but they are wrongly formated and must be fixed

# All records for Santiago and Rio are missing coordinates
# All records for Santiago have the same coordinates: which arent even in santiago
# Some coordinates for Rio repeat, not all of them
# Some of the repeated ones have different streets
# Ignore Santiago coordinates

import pandas as pd

latitud_prefix = "-22"
longitud_prefix = "-43"

shops_df = pd.read_excel("./Raw-Shops-Deliveries.xlsx", dtype={"Latitude": str, "Longitude": str})


rio_lat = shops_df.loc[shops_df["KM2 ID"] == 22, "Latitude"]
rio_lon = shops_df.loc[shops_df["KM2 ID"] == 22, "Longitude"]
shops_df.loc[shops_df["KM2 ID"] == 22, "Latitude"] = rio_lat.transform(lambda x: latitud_prefix+"."+str(x).split(latitud_prefix)[1])
shops_df.loc[shops_df["KM2 ID"] == 22, "Longitude"] = rio_lon.transform(lambda x: longitud_prefix+"."+str(x).split(longitud_prefix)[1])
shops_df.to_excel("./Raw-Shops-Deliveries-fixed.xlsx")