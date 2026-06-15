# E-commerce Analytics Platform

End-to-end Data Engineering project built using AWS S3, Databricks, Delta Lake, dbt and Mage.ai.

## Architecture

```text
CSV Files
    ↓
AWS S3
    ↓
Databricks Bronze
    ↓
Databricks Silver
    ↓
Databricks Gold
    ↓
dbt
    ↓
Mage.ai
    ↓
Dashboard Analytics
```

## Technologies

* AWS S3
* Databricks
* Delta Lake
* PySpark
* SQL
* dbt
* Mage.ai
* DuckDB

## Features

### Bronze Layer

* Raw data ingestion
* Delta Lake storage

### Silver Layer

* Data cleansing
* Data standardization
* Business transformations

### Gold Layer

* Revenue by Category
* Top Products
* Active Customers
* Executive KPIs

### Data Quality

* Null validation
* Duplicate detection
* Referential integrity checks

### Incremental Processing

* MERGE INTO implementation
* Delta Lake upserts

### Analytics

* Interactive dashboard
* Executive KPIs

## Project Results

* Total Revenue: 12.27M
* Active Customers: 488
* Revenue by Category Dashboard
* Top Products Dashboard

## Author

Igor Elipechuk Neves
