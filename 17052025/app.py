import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

st.set_page_config(page_title="System Sprzedaży", page_icon="📊", layout="wide")


def get_connection():
    return sqlite3.connect('sales.db')


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT name FROM sqlite_master 
        WHERE type='table' AND name='sales'
    """)

    if not cursor.fetchone():
        cursor.execute("""
            CREATE TABLE sales (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                product TEXT NOT NULL,
                quantity INTEGER NOT NULL,
                price REAL NOT NULL,
                date TEXT NOT NULL
            )
        """)

        sample_data = [
            ('Laptop', 2, 2500.0, '2025-05-07'),
            ('Smartphone', 5, 1200.0, '2025-05-07'),
            ('Tablet', 3, 800.0, '2025-05-08'),
            ('Laptop', 1, 2400.0, '2025-05-08'),
            ('Monitor', 4, 600.0, '2025-05-09'),
            ('Smartphone', 2, 1100.0, '2025-05-09'),
        ]

        cursor.executemany("""
            INSERT INTO sales (product, quantity, price, date)
            VALUES (?, ?, ?, ?)
        """, sample_data)

        conn.commit()

    conn.close()


init_db()

st.title("📊 System Zarządzania Sprzedażą")
st.markdown("---")

st.sidebar.header("Opcje")

st.sidebar.subheader("Dodaj nową sprzedaż")
with st.sidebar.form("add_sale_form"):
    product = st.selectbox("Produkt", ["Laptop", "Smartphone", "Tablet", "Monitor", "Inny"])
    quantity = st.number_input("Ilość", min_value=1, value=1)
    price = st.number_input("Cena jednostkowa (zł)", min_value=0.0, value=0.0, step=0.01)
    date = st.date_input("Data", datetime.now())

    submitted = st.form_submit_button("Dodaj sprzedaż")

    if submitted:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO sales (product, quantity, price, date) VALUES (?, ?, ?, ?)",
            (product, quantity, price, date.strftime("%Y-%m-%d"))
        )
        conn.commit()
        conn.close()
        st.sidebar.success("Dodano nową sprzedaż!")
        st.balloons()

st.sidebar.subheader("Filtry")
show_all = st.sidebar.checkbox("Pokaż wszystkie produkty", value=True)

if not show_all:
    conn = get_connection()
    products = pd.read_sql_query("SELECT DISTINCT product FROM sales ORDER BY product", conn)
    conn.close()

    selected_products = st.sidebar.multiselect(
        "Wybierz produkty do wyświetlenia",
        options=products['product'].tolist(),
        default=products['product'].tolist()[0] if not products.empty else None
    )
else:
    selected_products = None

conn = get_connection()

if selected_products:
    query = "SELECT * FROM sales WHERE product IN ({})".format(','.join('?' * len(selected_products)))
    df = pd.read_sql_query(query, conn, params=selected_products)
else:
    df = pd.read_sql_query("SELECT * FROM sales", conn)

conn.close()

df['sale_value'] = df['quantity'] * df['price']

st.subheader("Dane sprzedaży")
st.dataframe(df)

st.subheader("Wizualizacja danych")
col1, col2 = st.columns(2)

with col1:
    st.markdown("**Sprzedaż dzienna (wartość)**")

    daily_sales = df.groupby('date')['sale_value'].sum().reset_index()

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(daily_sales['date'], daily_sales['sale_value'])
    ax.set_xlabel('Data')
    ax.set_ylabel('Wartość sprzedaży (zł)')
    ax.tick_params(axis='x', rotation=45)
    plt.tight_layout()
    st.pyplot(fig)

with col2:
    st.markdown("**Suma sprzedanych produktów wg typu**")

    product_sales = df.groupby('product')['quantity'].sum().reset_index()

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.pie(product_sales['quantity'], labels=product_sales['product'], autopct='%1.1f%%')
    ax.set_title('Udział produktów w sprzedaży')
    st.pyplot(fig)

st.subheader("Podsumowanie")
total_sales = df['sale_value'].sum()
total_quantity = df['quantity'].sum()

col1, col2, col3 = st.columns(3)
col1.metric("Łączna wartość sprzedaży", f"{total_sales:,.2f} zł")
col2.metric("Łączna liczba sprzedanych sztuk", f"{total_quantity:,}")
col3.metric("Liczba transakcji", f"{len(df):,}")

st.markdown("---")
st.markdown("© 2025 System Zarządzania Sprzedażą")