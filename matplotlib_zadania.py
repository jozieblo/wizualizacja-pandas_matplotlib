# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import xlrd
# import openpyxl

# print("zad1")
# xlsx=pd.ExcelFile('imiona.xlsx')
# df = pd.read_excel(xlsx, header=0)
# print(df)
# df2=df.groupby(['Rok']).agg({'Liczba':['sum']})
# print(df2)
# df2.plot()
# plt.show()

# print("zad2")
#
# xlsx=pd.ExcelFile('imiona.xlsx')
# df = pd.read_excel(xlsx, header=0)
# print(df)
# df2=df.groupby(['Plec']).agg({'Liczba':['sum']})
# print(df2)
# slup=df2.plot.bar()
# slup.set_ylabel("Liczba w Mln")
# slup.set_xlabel('Plec')
# slup.legend()
# plt.title('Liczba urodzonych chlopcow i dziewczynek')
# plt.xticks(rotation=0)
# plt.show()

# print("zad3")
# xlsx=pd.ExcelFile('imiona.xlsx')
# df=pd.read_excel(xlsx, header=0)
# grupa=df.where(df['Rok']>2012).groupby(['Plec']).agg({'Liczba':["sum"]})
# kolo=grupa.plot.pie(subplots=True, autopct='%.2f %%', fontsize=20, figsize=(6,6),legend=(0,0))
# plt.legend(loc="lower right")
# plt.title("Suma dzieci wg plci wyrazona w procentach w ostatnich 5 latach")
# plt.show()

# print("zad4")
# df=pd.read_csv('zamowienia.csv', header=0, sep=";", decimal=".")
# print(df)
# df2=df.groupby(['Sprzedawca']).agg({'idZamowienia':['sum']})
# print(df2)
# slup=df2.plot.bar()
# slup.set_ylabel("Liczba w Mln")
# slup.set_xlabel('Sprzedawca')
# slup.legend()
# plt.title('ilosc zamowien dla poszczegolnych sprzedawcow')
# plt.xticks(rotation=0)
# plt.show()