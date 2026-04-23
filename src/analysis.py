def calculate_metrics(df):
    total_revenue = df["payment_value"].sum()
    total_orders = df["order_id"].nunique()
    avg_ticket = total_revenue / total_orders

    top_categories = (
        df.groupby("product_category_name")["payment_value"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    revenue_by_state = (
        df.groupby("customer_state")["payment_value"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    return {
        "total_revenue": total_revenue,
        "total_orders": total_orders,
        "avg_ticket": avg_ticket,
        "top_categories": top_categories,
        "revenue_by_state": revenue_by_state
    }