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

    

def main():
    print("Hello World")

main()