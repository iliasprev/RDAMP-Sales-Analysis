import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
file_path = 'Ace Superstore Retail Dataset.xlsx'
df = pd.read_excel(file_path, sheet_name='in')

# Clean and calculate
df.columns = df.columns.str.strip()
df['Total Revenue'] = df['Sales'] * df['Quantity']
df['Total Cost'] = df['Cost Price'] * df['Quantity']
df['Total Discount Value'] = df['Sales'] * df['Quantity'] * df['Discount']
df['Margin'] = df['Total Revenue'] - df['Total Cost']



# Add Margin column
df['Margin'] = df['Total Revenue'] - df['Total Cost']

# 1. Sales Summary by Region & Order Mode
summary = df.groupby(['Region', 'Order Mode']).agg({
    'Sales': 'sum',
    'Total Revenue': 'sum',
    'Discount': 'mean'
}).reset_index()

print("\n📊 Sales Summary by Region and Order Mode:")
print(summary)

# 2. Top 5 Products by Revenue
top_products = df.groupby('Product Name')['Total Revenue'].sum().sort_values(ascending=False).head(5)
print("\n🥇 Top 5 Products by Revenue:")
print(top_products)

# 3. Bottom 5 Products by Revenue
bottom_products = df.groupby('Product Name')['Total Revenue'].sum().sort_values().head(5)
print("\n🔻 Bottom 5 Products by Revenue:")
print(bottom_products)

# 4. Highest Margin Categories
category_margin = df.groupby('Category')['Margin'].sum().sort_values(ascending=False)
print("\n💰 Categories with Highest Margins:")
print(category_margin)

# 5. Visualization – Sales by Order Mode
plt.figure(figsize=(6,4))
sns.barplot(data=df, x='Order Mode', y='Sales', estimator=sum, ci=None)
plt.title('Total Sales by Order Mode')
plt.tight_layout()
plt.savefig('sales_by_order_mode.png')
print("\n✅ Chart saved: sales_by_order_mode.png")

# Top 5 Products Chart
top_5 = df.groupby('Product Name')['Total Revenue'].sum().sort_values(ascending=False).head(5).reset_index()

plt.figure(figsize=(8, 5))
sns.barplot(data=top_5, y='Product Name', x='Total Revenue', palette='viridis')
plt.title('Top 5 Products by Revenue')
plt.xlabel('Total Revenue')
plt.ylabel('Product Name')
plt.tight_layout()
plt.savefig('top_5_products.png')
plt.close()
print("✅ Chart saved: top_5_products.png")

top_margin = df.groupby('Category')['Margin'].sum().sort_values(ascending=False).head(10).reset_index()

plt.figure(figsize=(8, 5))
sns.barplot(data=top_margin, x='Margin', y='Category', palette='magma')
plt.title('Top 10 Categories by Margin')
plt.xlabel('Total Margin')
plt.ylabel('Category')
plt.tight_layout()
plt.savefig('top_margin_categories.png')
plt.close()
print("✅ Chart saved: top_margin_categories.png")



