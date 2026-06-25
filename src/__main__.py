import pandas as pd
import matplotlib.pyplot as plt


# data load
df: pd.DataFrame = pd.read_csv("data/sales_data.csv")

# cleaning

df = df.dropna()
df = df.drop_duplicates()
df['date'] = pd.to_datetime(df['date'])

df['revenue'] = df['price'] * df['quantity']
df['tax'] = df['revenue'] * 0.15

# analysis

product_sales = df.groupby('product')['quantity'].sum()
df = df.set_index('date')
monthly_sales = df.resample('MS')['revenue'].sum()
revenue_per_product = df.groupby('product')['revenue'].sum()
best_product_revenue = revenue_per_product.idxmax()


plt.figure(figsize=(12, 8))
product_sales.plot(kind='bar', color='skyblue')
plt.title("Sales per product", fontsize=16)
plt.xlabel("Product", fontsize=12)
plt.ylabel("Quantity Sold", fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("outputs/products_chart.png")
plt.close()

plt.figure(figsize=(12, 8))
monthly_sales.plot(kind='line', marker='*')
plt.title("Monthly Sales", fontsize=16)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Revenue", fontsize=12)
plt.grid(True)
plt.tight_layout()
plt.savefig("outputs/monthly_sales.png")
plt.close()

df.to_csv("outputs/cleaned_data.csv", index=False)
revenue_per_product.to_csv("outputs/revenue_per_product.csv", index=True)

print(f"Best Product By Revenue: {best_product_revenue}")
print("\nRevenue per Product:")
print(revenue_per_product)