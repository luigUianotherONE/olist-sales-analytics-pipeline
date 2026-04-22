def calculate_metrics(df):
    metrics = {}

    total_revenue = df["payment_value"].sum()
    total_orders = df["order_id"].nunique()

    metrics["total_revenue"] = total_revenue
    metrics["total_orders"] = total_orders
    metrics["avg_ticket"] = total_revenue / total_orders

    metrics["top_categories"] = (
        df.groupby("product_category_name")["payment_value"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
    )

    metrics["revenue_by_state"] = (
        df.groupby("customer_state")["payment_value"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
    )

    return metrics