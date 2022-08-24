import pandas as pd
import matplotlib.pyplot as plt

"""
--Viajes--
Preguntas h, j, t
"""
def viajes():
    print("Viajes")


"""
--Ciudades--
Preguntas o-s, f
"""
def ciudades():
    print("Ciudades")



"""
--Shops--
Preguntas l - s
"""
def tiendas():
    print("Tiendas")


"""
--Vehiculos-- 
Preguntas a - e, g, i, k
"""
def vehiculos():
    print("Vehiculos")


def preprocess(df):

    # Remove unamed columns
    df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)

def merge(df_1, df_2):
    priny("Combinando archivos para eliminar repetidos...")

def main():
    print("Hello World")
    pd.read_excel("Raw-Shops-Deliveries.xlsx")
    deliveries_df = pd.read_excel("./Raw-Deliveries.xlsx")
    disruptions_df = pd.read_excel("./Deliveries_disruptions.xlsx", "Hoja3")


main()