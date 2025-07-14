import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import os
os.makedirs('data', exist_ok=True)

import mysql.connector # type: ignore

# Connect to MySQL (same as phpMyAdmin)
conn = mysql.connector.connect(
    host="localhost",       # same as 127.0.0.1
    user="root",            # default user in phpMyAdmin
    password="",            # empty unless you set one
    database="ace_superstore"
)

cursor = conn.cursor()

# Show tables to test connection
cursor.execute("SHOW TABLES;")
tables = cursor.fetchall()

print(" Connected to MySQL! Tables found:")
for t in tables:
    print("-", t[0])



# Load dataset
file_path = 'Ace Superstore Retail Dataset.xlsx'
df = pd.read_excel(file_path, sheet_name='in')

# Clean and calculate
df.columns = df.columns.str.strip()

df['Total Revenue'] = df['Sales'] * df['Quantity']
df['Total Cost'] = df['Cost Price'] * df['Quantity']
df['Total Discount Value'] = df['Sales'] * df['Quantity'] * df['Discount']
df['Margin'] = df['Total Revenue'] - df['Total Cost']

dim_location = df[['City', 'Postal Code', 'Region', 'Country']].drop_duplicates().reset_index(drop=True)
dim_location.insert(0, 'Location ID', range(1, len(dim_location) + 1))


# 1. Sales Summary by Region & Order Mode
summary = df.groupby(['Region', 'Order Mode']).agg({
    'Sales': 'sum',
    'Total Revenue': 'sum',
    'Discount': 'mean'
}).reset_index()

print("\nSales Summary by Region and Order Mode:")
print(summary)

# 2. Top 5 Products by Revenue
top_products = df.groupby('Product Name')['Total Revenue'].sum().sort_values(ascending=False).head(5)
print("\nTop 5 Products by Revenue:")
print(top_products)

# 3. Bottom 5 Products by Revenue
bottom_products = df.groupby('Product Name')['Total Revenue'].sum().sort_values().head(5)
print("\nBottom 5 Products by Revenue:")
print(bottom_products)

# 4. Highest Margin Categories
category_margin = df.groupby('Category')['Margin'].sum().sort_values(ascending=False)
print("\nCategories with Highest Margins:")
print(category_margin)

# 5. Visualization – Sales by Order Mode
plt.figure(figsize=(6,4))
sns.barplot(data=df, x='Order Mode', y='Sales', estimator=sum, ci=None)
plt.title('Total Sales by Order Mode')
plt.tight_layout()
plt.savefig('sales_by_order_mode.png')
print("\nChart saved: sales_by_order_mode.png")

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
print("Chart saved: top_5_products.png")

top_margin = df.groupby('Category')['Margin'].sum().sort_values(ascending=False).head(10).reset_index()

plt.figure(figsize=(8, 5))
sns.barplot(data=top_margin, x='Margin', y='Category', palette='magma')
plt.title('Top 10 Categories by Margin')
plt.xlabel('Total Margin')
plt.ylabel('Category')
plt.tight_layout()
plt.savefig('top_margin_categories.png')
plt.close()
print("Chart saved: top_margin_categories.png")

def extract_segment(x):
    if isinstance(x, str):
        return x.split('-')[1].strip() if '-' in x else x.strip()
    return 'Unknown'  # or np.nan if preferred

df['Segment'] = df['Category'].apply(extract_segment)


# Dimension Tables

# dim_customer
dim_customer = df[['Customer ID', 'Segment']].drop_duplicates().reset_index(drop=True)

# dim_product
dim_product = df[['Product ID', 'Product Name', 'Sub-Category']].drop_duplicates().reset_index(drop=True)

# dim_category
dim_category = df[['Category', 'Segment']].drop_duplicates().reset_index(drop=True)

# dim_location
dim_location = df[['City', 'Postal Code', 'Region', 'Country']].drop_duplicates().reset_index(drop=True)

# dim_order_mode
dim_order_mode = df[['Order Mode']].drop_duplicates().reset_index(drop=True)
dim_order_mode['Order_Mode_ID'] = range(1, len(dim_order_mode) + 1)


# dim_date
df['Order Date'] = pd.to_datetime(df['Order Date'])
dim_date = df[['Order Date']].drop_duplicates().reset_index(drop=True)
dim_date['Year'] = dim_date['Order Date'].dt.year
dim_date['Month'] = dim_date['Order Date'].dt.month
dim_date['Quarter'] = dim_date['Order Date'].dt.quarter

# Fact Table
fact_sales = df[[
    'Order ID', 'Order Date', 'Customer ID', 'Product ID', 'City', 'Postal Code',
    'Order Mode', 'Quantity', 'Total Revenue', 'Total Cost', 'Margin', 'Discount', 'Total Discount Value'
]]
dim_customer.to_csv('data/dim_customer.csv', index=False)
dim_product.to_csv('data/dim_product.csv', index=False)
dim_category.to_csv('data/dim_category.csv', index=False)
dim_location.to_csv('data/dim_location.csv', index=False)
dim_order_mode.to_csv('data/dim_order_mode.csv', index=False)
dim_date.to_csv('data/dim_date.csv', index=False)
fact_sales.to_csv('data/fact_sales.csv', index=False)


