# Search Performance Data ETL

This script automates the process of importing SEO performance data (exported as CSV files) into a local SQLite database. It is designed to handle exports from Google Search Console or similar SEO tools.

## Features

- **Automated Ingestion:** Iterates through a predefined list of CSV files.
- **Data Normalization:** Standardizes column and table names (snake_case) for better SQL queryability.
- **Encoding Handling:** Automatically handles standard UTF-8 and Latin1 encodings to prevent read errors.
- **Idempotency:** Replaces existing tables (`if_exists='replace'`) to ensure data freshness on re-runs.

## Prerequisites

- Python 3.x
- pandas library

### Installation

If you do not have pandas installed, run:

```bash
pip install pandas
