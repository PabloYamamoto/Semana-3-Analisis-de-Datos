import pandas as pd

def find_nth(string, to_find, n):
    start = string.find(to_find)
    while start >= 0 and n > 1:
        start = string.find(to_find, start+len(to_find))
        n -= 1
    return start

def to_american_date(date: str):
    l = find_nth(date, "-", 1) + 1
    r = find_nth(date, "-", 2)
    d = date[l:r]
    m = str(int(date[r + 1:date.find(" ")]))
    return m + "/" + d + "/" + date[:l - 1] + " " + date[date.find(" ") + 1:]

def to_yyyy(date : str):

    if(date.find("/20") != -1):
        return date

    l = find_nth(date, "/", 2)
    r = date.find(" ")
    y = date[l+1:r]
    return date[:l] + "/20" + y + date[r:]



def preprocess_deliveries(df: pd.DataFrame):
    print("-----Preprocessing Raw-Deliveries.xlsx-----")
    # First we fix KM2 IDs
    df["KM2 ID"] = df["KM2 ID"].transform(lambda x: x.split("(")[1].split(")")[0])

    fixed_coordinates = pd.read_excel("./Raw-Shops-Deliveries-fixed.xlsx")
    fixed_coordinates = fixed_coordinates.loc[fixed_coordinates["KM2 ID"] == 22]
    
    # Then we add the missing coordinates for Rio
    df = df.set_index("Delivery Key").fillna(fixed_coordinates.set_index("Shop ID"))
    print("result", df.loc[df["KM2 ID"] == "22", "Latitude"])
    df.to_excel("./Raw-Deliveries.xlsx")

    print("-----------------Done!----------------")


merged = pd.read_excel("./Merged_1.xlsx")
merged["Vehicle Type"] = merged["Vehicle Type"].str.capitalize()
merged["Notes"] = merged["Notes"].str.capitalize()
merged["Started At"] = merged["Started At"].transform(lambda x: to_yyyy(x))
merged["Ended At"] = merged["Ended At"].transform(lambda x: to_yyyy(x))
merged.drop_duplicates(keep="first").to_excel("./Merged_2.xlsx")


# deliveries_df = pd.read_excel("./Raw-Deliveriesoriginal.xlsx")
# disruptions_df = pd.read_excel("./Disruptions_unique_duration.xlsx")

#disruptions_df = disruptions_df.drop(columns=["ID","disruption_count","delivery_count"]).drop_duplicates(keep="first")
# print(disruptions_df["Started At"])
# print(disruptions_df["Started At"].transform(lambda x: x if x[0] == '7' else to_american_date(x)))
# disruptions_df["Started At"] = disruptions_df["Started At"].transform(lambda x: x if x[0] == '7' else to_american_date(x))
# disruptions_df["Ended At"] = disruptions_df["Ended At"].transform(lambda x: x if x[0] == '7' else to_american_date(x))

# disruptions_df.to_excel("./Disruptions_unique_final.xlsx")
# disruptions_df = pd.read_excel("./Deliveries_disruptions.xlsx", "Hoja3")

# preprocess_deliveries(deliveries_df)


# ["KM2 ID","ID.1","Street ID","Shop ID","Started At","Ended At","Vehicle Type","Divering Company","Product Delivered","Refrigerated Vehicle","Boxes Delivered","Delivery Type","Equipment","Number of Trips","Notes","Latitude","Longitude","Delivery Key","Distance to Shop","is_out_of_segment","shops_served"]
# ["ID","KM2 ID","ID.1","Street ID","Shop ID","Started At","Ended At","Duration","Vehicle Type","Divering Company","Product Delivered","Refrigerated Vehicle","Boxes Delivered","Delivery Type","Equipment","Number of Trips","Notes","Latitude","Longitude","Delivery Key","Distance to Shop","is_out_of_segment","shops_served","disruption_count","delivery_count"]

# s[:r]
# 
# final[:final.find("/")]+ "/" + s[:r]  + final[find_2nd(final, "/"):]
