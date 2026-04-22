def create_order_revenue(orders, payments):
    df = orders.merge(payments, on="order_id")

    # 🔹 garante 1 linha por pedido
    df = (
        df.groupby("order_id", as_index=False)["payment_value"]
        .sum()
    )

    return df


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