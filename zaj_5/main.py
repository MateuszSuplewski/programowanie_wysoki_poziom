import sqlite3
import pandas as pd

# Połączenie z istniejącą bazą danych
conn = sqlite3.connect("sales.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM sales")

rows = cursor.fetchall()


df = pd.read_sql("SELECT * FROM sales", conn)

print(df)

# a) Sprzedaż laptopów
print(df[df['product'] == 'Laptop'])


# b) Dane z dni 05-07 - 05-08
print(df[(df['date'] >= '2025-05-07') & (df['date'] <= '2025-05-08')])

# c) Transakcje, ktore przekraczaja 200zl za produkt
print(df[df['price']/df['quantity'] > 200])

# d) Laczna wartosc sprzedazy dla kazdego produktu
df['total_value'] = df['quantity'] * df['price']
total_sales_per_product = df.groupby('product')['total_value'].sum().reset_index()
print(total_sales_per_product)


# e) Dzien z najwieksza liczba sprzedanych sztuk
daily_sales = df.groupby('date')['quantity'].sum()
max_sales_day = daily_sales.idxmax()
print(max_sales_day)
conn.close()

