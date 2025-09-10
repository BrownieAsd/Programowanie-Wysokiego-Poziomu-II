import sqlite3
import pandas as pd

conn = sqlite3.connect('sales.db')

print("a) Sprzedaż produktu 'Laptop':")
df_a = pd.read_sql_query("SELECT * FROM sales WHERE product = 'Laptop'", conn)
print(df_a)
print("\n" + "="*50 + "\n")

print("b) Sprzedaż z dni 2025-05-07 i 2025-05-08:")
df_b = pd.read_sql_query("SELECT * FROM sales WHERE date IN ('2025-05-07', '2025-05-08')", conn)
print(df_b)
print("\n" + "="*50 + "\n")

print("c) Transakcje z ceną jednostkową > 200 zł:")
df_c = pd.read_sql_query("SELECT * FROM sales WHERE price > 200", conn)
print(df_c)
print("\n" + "="*50 + "\n")

print("d) Łączna wartość sprzedaży dla każdego produktu:")
df_d = pd.read_sql_query("""
    SELECT product, SUM(quantity * price) as total_value 
    FROM sales 
    GROUP BY product
""", conn)
print(df_d)
print("\n" + "="*50 + "\n")

print("e) Dzień z największą liczbą sprzedanych sztuk:")
df_e = pd.read_sql_query("""
    SELECT date, SUM(quantity) as total_quantity 
    FROM sales 
    GROUP BY date 
    ORDER BY total_quantity DESC 
    LIMIT 1
""", conn)
print(df_e)

conn.close()