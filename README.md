# Data Warehouse ETL Project - E-commerce Simulation

## Description
This project implements a complete **ETL (Extract, Transform, Load)** pipeline and simulates the construction of a **data warehouse** using the public [DummyJSON API](https://DummyJSON.com/).  
The goal is to demonstrate how a data engineer can integrate multiple data sources, apply business rules, and design a dimensional model for analytics in the e-commerce domain.

## Project Objectives
- **Extract:**  
  - Download product, category, and user data from the DummyJSON API.  
  - Integrate external CSV files simulating sales transactions.  

- **Transform:**  
  - Validate and clean product prices and categories.  
  - Normalize data formats (currency, dates, IDs).  
  - Create **dimension tables** (products, customers, categories).  
  - Create a **fact table** (sales) with calculated metrics such as revenue and profit margin.  

- **Load:**  
  - Save transformed data into CSV files for portability.  
  - Load data into a **PostgreSQL database** following a **star schema** design.  

## Technologies Used
- **Python 3**  
- **Pandas** for data manipulation  
- **Requests** for API consumption  
- **PostgreSQL** for data warehouse storage  
- **SQL** for schema design and queries  

## Project Structure
- `extract.py` → scripts to download data from APIs and CSVs.  
- `transform.py` → data cleaning, normalization, and dimensional modeling.  
- `load.py` → load data into PostgreSQL and generate CSV outputs.  
- `warehouse_schema.sql` → SQL script to create star schema tables.  
- `README.md` → project documentation.  

## Expected Results
- A **PostgreSQL database** with dimension and fact tables ready for analytics.  
- A **clean CSV dataset** (`products.csv`, `users.csv`) for quick inspection.  
- Example queries to calculate KPIs such as total revenue per category, average margin, and top-selling products.  

## Next Steps
- Automate the pipeline with **Airflow** or **Prefect**.  
- Build a dashboard in **Power BI** or **Tableau** to visualize KPIs.  
- Extend the warehouse with additional data sources (e.g., weather, marketing campaigns).  

## Why This Project Matters
This project simulates a **real-world e-commerce data warehouse**, showing skills in:  
- ETL pipeline development.  
- Dimensional modeling (star schema).  
- SQL database integration.  
- Business-oriented data transformation.  

It is designed to demonstrate capabilities expected from a **Data Engineer focused on Data Warehousing**.
