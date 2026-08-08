import json
import pandas as pd

def load_orders():
    with open("orders.json", "r", encoding="utf-8") as f:
        return json.load(f)

def analyze_orders(data):
    df = pd.DataFrame(data)
    df["total"] = df["price"] * df["quantity"]

    print("📊 گزارش سفارش‌ها:")
    print(df)

    print("\n💰 مجموع کل فروش:", df["total"].sum())
    print("📈 میانگین مبلغ سفارش:", df["total"].mean())
    print("🔝 بزرگ‌ترین سفارش:", df["total"].max())
    print("🟢 کوچک‌ترین سفارش:", df["total"].min())

    return df

def export_excel(df):
    df.to_excel("orders_report.xlsx", index=False)
    print("✅ فایل orders_report.xlsx ساخته شد.")

def filter_by_customer(df, name):
    name = name.lower()
    result = df[df["customer"].str.lower() == name]
    return result



def filter_by_price(df, min_price):
    return df[df["total"] >= min_price]
