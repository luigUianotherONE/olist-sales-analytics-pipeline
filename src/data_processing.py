from pathlib import Path

def create_order_revenue(orders, payments):
    order_revenue = orders.merge(payments, on="order_id")

    order_revenue = (
        order_revenue
        .groupby("order_id", as_index=False)["payment_value"]
        .sum()
    )

    return order_revenue


def create_items_dataset(items, products):
    return items.merge(products, on="product_id")


def create_final_dataset(order_revenue, items_products, customers, orders):
    
    
    df = items_products.merge(order_revenue, on="order_id")

    df = df.merge(
        orders[["order_id", "customer_id", "order_purchase_timestamp"]],
        on="order_id"
    )

    df = df.merge(customers, on="customer_id")

    return df


def save_processed_data(df):
    output_path = Path(__file__).resolve().parent.parent / "data" / "processed"
    output_path.mkdir(parents=True, exist_ok=True)

    df.to_csv(output_path / "final_dataset.csv", index=False)