import matplotlib.pyplot as plt
from pathlib import Path
import pandas as pd

def _get_output_path():
    path = Path(__file__).resolve().parent.parent / "output" / "charts"
    path.mkdir(parents=True, exist_ok=True)
    return path


def plot_revenue_by_category(df):
    path = _get_output_path()

    revenue = (
        df.groupby("product_category_name")["payment_value"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    revenue.plot(kind="barh")
    plt.title("Top Categories by Revenue")
    plt.xlabel("Revenue")

    plt.savefig(path / "top_categories.png")
    plt.close()


def plot_revenue_over_time(df):
    path = _get_output_path()

    df["order_purchase_timestamp"] = pd.to_datetime(df["order_purchase_timestamp"])
    df["month"] = df["order_purchase_timestamp"].dt.to_period("M")

    revenue = df.groupby("month")["payment_value"].sum()

    revenue.plot()
    plt.title("Revenue Over Time")

    plt.savefig(path / "revenue_over_time.png")
    plt.close()