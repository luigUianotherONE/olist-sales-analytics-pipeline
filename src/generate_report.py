from data_loader import load_data
from data_processing import (
    create_order_revenue,
    create_items_dataset,
    create_final_dataset,
    save_processed_data
)
from analysis import calculate_metrics
from visualization import (
    plot_revenue_by_category,
    plot_revenue_over_time
)

from pathlib import Path


def main():
    # Load
    orders, items, products, customers, payments = load_data()

    # Process
    order_revenue = create_order_revenue(orders, payments)
    items_products = create_items_dataset(items, products)

    df = create_final_dataset(
        order_revenue,
        items_products,
        customers,
        orders
    )

    # Save processed dataset
    save_processed_data(df)

    # Analysis
    metrics = calculate_metrics(df)

    # Visualization
    plot_revenue_by_category(df)
    plot_revenue_over_time(df)

    # Report
    report_path = Path(__file__).resolve().parent.parent / "output" / "reports"
    report_path.mkdir(parents=True, exist_ok=True)

    with open(report_path / "report.txt", "w", encoding="utf-8") as f:
        f.write("RELATÓRIO DE VENDAS - OLIST\n\n")
        f.write(f"Receita Total: {metrics['total_revenue']:.2f}\n")
        f.write(f"Pedidos Totais: {metrics['total_orders']}\n")
        f.write(f"Ticket Médio: {metrics['avg_ticket']:.2f}\n\n")

        f.write("Top Categorias:\n")
        for k, v in metrics["top_categories"].items():
            f.write(f"- {k}: {v:.2f}\n")

        f.write("\nTop Estados:\n")
        for k, v in metrics["revenue_by_state"].items():
            f.write(f"- {k}: {v:.2f}\n")


if __name__ == "__main__":
    main()