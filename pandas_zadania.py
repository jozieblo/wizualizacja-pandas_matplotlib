# import numpy as np
# import pandas as pd
# import xlrd
# import openpyxl

# print("zad1")
# xlsx = pd.ExcelFile('imiona.xlsx')
# df = pd.read_excel(xlsx, header=0)
# print(df)

# print("zad2")

# print(df[df['Liczba']>1000])

# print(df[df['Imie'] == "JAROSŁAW"])
# print(df['Liczba'].sum())
# print(df[(df.Rok>=2000) & (df.Rok<=2005)]['Liczba'].sum())
#print(df[df['Plec']=="M"]['Liczba'].sum())
#print(df[df['Plec']=="K"]['Liczba'].sum())
#print(df.describe())
# print(df[(df['Plec']=='M') & (df['Rok']==2000)]['Liczba'].value_counts())
# print(df[(df['Plec']=='K') & (df['Rok']==2000)]['Liczba'].value_counts())
#print(df[(df['Plec']=='M')[['Imie'].value_counts()]['Liczba'].value_counts()])
#print(df[(df['Plec']=='K')[['Imie'].value_counts()]['Liczba'].value_counts()])
# print("zad3")
# df = pd.read_csv('zamowienia.csv', header=0, sep=";", decimal=".")
# print(df['Sprzedawca'].unique())
# print(df.groupby(['Sprzedawca'])[['Utarg']].sum())
# print(df.groupby(['Kraj'])[['Utarg']].sum())
# print(df[(df['Data zamowienia']==2005) & (df['Kraj']=="Polska")]['Utarg'].sum())
