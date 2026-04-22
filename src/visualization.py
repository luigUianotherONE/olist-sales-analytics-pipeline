import matplotlib.pyplot as plt
from pathlib import Path


def plot_revenue_by_category(df):
    # 🔹 cria caminho absoluto seguro
    output_path = Path(__file__).resolve().parent.parent / "output" / "charts"
    
    # 🔹 garante que a pasta existe
    output_path.mkdir(parents=True, exist_ok=True)

    data = (
        df.groupby("product_category_name")["payment_value"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    data.plot(kind="bar")
    plt.title("Top Categories by Revenue")
    plt.xticks(rotation=45)

    plt.tight_layout()

    # 🔹 salva corretamente
    plt.savefig(output_path / "top_categories.png")
    plt.close()

def plot_revenue_over_time(df):
    from pathlib import Path
    import pandas as pd
    import matplotlib.pyplot as plt

    # 🔹 caminho profissional
    output_path = Path(__file__).resolve().parent.parent / "output" / "charts"
    output_path.mkdir(parents=True, exist_ok=True)

    # 🔹 garantir datetime
    df["order_purchase_timestamp"] = pd.to_datetime(df["order_purchase_timestamp"])

    # 🔹 criar coluna de mês
    df["month"] = df["order_purchase_timestamp"].dt.to_period("M")

    # 🔹 agregação
    data = df.groupby("month")["payment_value"].sum()

    # 🔹 plot
    data.plot()
    plt.title("Revenue Over Time")

    plt.tight_layout()
    plt.savefig(output_path / "revenue_over_time.png")
    plt.close()