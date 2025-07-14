RDAMP Task 2 – Dimensional Modeling and Sales Dashboard
Submitted by: Ilias Prevyzis
Cohort: July 2025 – RealCare Tech RDAMP
Project: Ace Superstore BI System – Task 2

Overview
This project is part of Task 2 of the RDAMP program. It builds on Task 1's cleaned dataset to create a structured and scalable dimensional data model. Using SQL and best practices in data warehousing, I created reusable views and built a professional dashboard for business insights.

Although Power BI was recommended, I used Google Data Studio for visualizations due to driver installation issues on macOS (MySQL ODBC driver failed to install despite multiple attempts). Google Data Studio was used instead to meet all dashboard and visualization requirements.

Dimensional Model Overview
The data model follows a star schema format with one fact table and multiple dimensions. Foreign keys link dimension records to transactions in the fact_sales table.

Fact Table:

fact_sales: Contains total sales, cost, profit, discount amount, and quantity sold.

Dimension Tables:

dim_customer: Customer ID and segment

dim_product: Product name and ID

dim_category: Category and sub-category (segment)

dim_location: Region, city, country

dim_order_mode: Online or In-Store

dim_date: Order date, month, year, quarter

SQL Views Created
The following SQL views were created in MySQL to summarize core business metrics:

View Name	Description
vw_product_seasonality	Product sales trends over time (month-level granularity)
vw_discount_impact_analysis	Discount vs profit correlation
vw_customer_order_patterns	Segment-based order behavior
vw_channel_margin_report	Online vs In-store profit comparison
vw_region_category_rankings	Category performance rankings by region
vw_top_customers	Top customers by profit or revenue

Dashboard (Google Data Studio)
Due to macOS driver issues, I used Google Data Studio to build the required dashboard.
The dashboard includes all visualizations outlined in the brief.

📄 Full Report PDF:
Download Dashboard Report (PDF)

📷 Screenshots:
Chart Title	Screenshot
Category Profit by Region	
Customer Order Behavior	
Product Seasonality	
Profitability by Order Mode	
Sales vs Profit	

Key Insights
Online sales generated higher average margins than in-store.

High-discount products often delivered low profit.

"Professional" segment had the highest average order value.

West Midlands and London were top-performing regions.

A small group of customers (top 10) contributed a large portion of revenue.

SQL Folder Contents
Located in: task 2/sql/

create_tables.sql: All dimension and fact table creation scripts

populate_fact_table.sql: Data insertions into star schema tables

create_views.sql: SQL views used for reporting

queries.sql: 5 reusable SQL queries that join multiple tables for insights

Technologies Used
Tool	Purpose
Python	Data cleaning, new feature calculations (profit, total revenue, discount amount)
MySQL	Schema creation, data loading, SQL views
Google Sheets	Hosted CSV exports to bridge MySQL → Data Studio
Google Data Studio	Interactive dashboard design and publishing

Notes
All deliverables were completed according to RDAMP Task 2 brief.

Visualizations were created in Google Data Studio to meet all reporting and dashboard requirements.

Power BI/Tableau were not used due to compatibility issues with macOS and MySQL driver installation.

Author
Ilias Prevyzis
RDAMP July 2025
GitHub: github.com/iliasprev

