import pandas as pd
from pathlib import Path

def load_data():
    base_path = Path(__file__).resolve().parent.parent / "data" / "raw"

    orders = pd.read_csv(base_path / "olist_orders_dataset.csv")
    items = pd.read_csv(base_path / "olist_order_items_dataset.csv")
    products = pd.read_csv(base_path / "olist_products_dataset.csv")
    customers = pd.read_csv(base_path / "olist_customers_dataset.csv")
    payments = pd.read_csv(base_path / "olist_order_payments_dataset.csv")

    return orders, items, products, customers, payments