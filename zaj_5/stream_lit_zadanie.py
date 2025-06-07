import streamlit as st
import sqlite3
import pandas as pd
from datetime import date

st.set_page_config(
    page_title="Analiza Sprzedaży"
)


def get_connection():
    return sqlite3.connect("sales.db", check_same_thread=False)


def load_data():
    conn = get_connection()
    try:
        df = pd.read_sql("SELECT * FROM sales", conn)
        return df
    except pd.io.sql.DatabaseError:
        st.error(
            "Błąd: Tabela 'sales' nie istnieje w bazie 'sales.db'. "
            "Upewnij się, że baza danych i tabela są poprawnie utworzone."
        )
        return pd.DataFrame(
            columns=["id", "product", "quantity", "price", "date"]
        )


# --- Główna część aplikacji ---
st.title("📈 Aplikacja do analizy sprzedaży")

df = load_data()


# 1.
st.write("Tabela sprzedaży")
st.write(df)


# 2.
with st.expander("➕ Dodaj nowy rekord sprzedaży"):
    with st.form("new_sale_form", clear_on_submit=True):
        product = st.selectbox(
            "Nazwa produktu:",
            df["product"].unique()
        )
        quantity = st.number_input(
            "Ilość produktu:", min_value=1, step=1, format="%d"
        )
        price = st.number_input(
            "Cena:", min_value=0.01, format="%.2f"
        )
        sale_date = st.date_input("Data sprzedaży:", value=date.today())
        submitted = st.form_submit_button("Dodaj produkt")

        if submitted and product:
            try:
                conn = get_connection()
                cursor = conn.cursor()
                sql = "INSERT INTO sales (product, quantity, price, date) VALUES (?,?,?,?)"
                values = (product, quantity, price, sale_date.strftime("%Y-%m-%d"))
                cursor.execute(sql, values)
                conn.commit()
                st.success("Pomyślnie dodano nowy produkt!")
                st.balloons()
                st.cache_data.clear()
            except Exception as e:
                st.error(f"Wystąpił błąd podczas dodawania do bazy danych: {e}")

# 3.
st.header("📦 Przeglądaj i filtruj dane")

if df.empty:
    st.warning("Brak danych do wyświetlenia. Dodaj pierwszy rekord sprzedaży.")
else:
    all_products = sorted(df["product"].unique())
    selected_products = st.multiselect(
        "Filtruj po produkcie:", options=all_products, default=all_products
    )
    df_filtered = df[df["product"].isin(selected_products)]

    st.dataframe(df_filtered)
    st.info(f"Wyświetlono {len(df_filtered)} z {len(df)} rekordów.")


# 4.
st.header("📊 Wizualizacje danych")

if df.empty:
    st.warning("Brak danych do narysowania wykresów.")
else:
    df_chart_data = df.copy()
    df_chart_data["total_value"] = df_chart_data["quantity"] * df_chart_data["price"]
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Wartość sprzedaży w ujęciu dziennym")
        daily_sales = (
            df_chart_data.groupby("date")["total_value"].sum().sort_index()
        )
        st.bar_chart(daily_sales)

    with col2:
        st.subheader("Suma sprzedanych sztuk wg produktu")
        product_quantity = (
            df_chart_data.groupby("product")["quantity"].sum().sort_values()
        )
        st.bar_chart(product_quantity)