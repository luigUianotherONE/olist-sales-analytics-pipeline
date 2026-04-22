from data_loader import load_data
from data_processing import (
    create_order_revenue,
    create_items_dataset,
    create_final_dataset
)
from analysis import calculate_metrics
from visualization import (
    plot_revenue_by_category,
    plot_revenue_over_time
)


def main():
    # 🔹 Load
    orders, items, products, customers, payments = load_data()

    # 🔹 Process
    order_revenue = create_order_revenue(orders, payments)
    items_products = create_items_dataset(items, products)

    df = create_final_dataset(
        order_revenue,
        items_products,
        customers,
        orders
    )

    # 🔹 Analysis
    metrics = calculate_metrics(df)

    # 🔹 Visualization
    plot_revenue_by_category(df)
    plot_revenue_over_time(df)

    # 🔹 Report
    from pathlib import Path

    # 🔹 cria caminho absoluto seguro
    report_path = Path(__file__).resolve().parent.parent / "output" / "reports"

    # 🔹 garante que a pasta existe
    report_path.mkdir(parents=True, exist_ok=True)

    # 🔹 salva o arquivo
    with open(report_path / "report.txt", "w") as f:
        f.write("SALES REPORT - OLIST\n\n")
        f.write(f"Total Revenue: {metrics['total_revenue']:.2f}\n")
        f.write(f"Total Orders: {metrics['total_orders']}\n")
        f.write(f"Average Ticket: {metrics['avg_ticket']:.2f}\n\n")

        f.write("Top Categories:\n")
        for category, value in metrics["top_categories"].items():
            f.write(f"- {category}: {value:.2f}\n")

        f.write("\nTop States:\n")
        for state, value in metrics["revenue_by_state"].items():
            f.write(f"- {state}: {value:.2f}\n")

if __name__ == "__main__":
    main()