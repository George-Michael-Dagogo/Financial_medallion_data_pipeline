# SEC Data Pipeline to Azure Blob Storage, Databricks, and Snowflake

This repository contains the code for a comprehensive data pipeline that:

1. Scrapes financial statement datasets from the **U.S. SEC website**.
2. Downloads the datasets as **ZIP files**.
3. Uploads these datasets to **Azure Blob Storage**.
4. Processes the data in **Databricks** using **Delta Lake** for optimized storage.
5. Transfers the processed data to **Snowflake** for further analysis and reporting.

---

## 🚀 Project Overview

The goal of this project is to create an automated pipeline that extracts, processes, and uploads SEC financial data. The key steps include:

1. **Scraping SEC Website**: The SEC's website is scraped for links to downloadable ZIP files containing the financial statement datasets.
   
2. **Downloading Files**: These ZIP files are then downloaded locally using Python’s `requests` library.

3. **Uploading to Azure Blob Storage**: After the files are downloaded, they are uploaded to **Azure Blob Storage** to serve as a central storage point.

4. **Processing in Databricks**: The files are loaded into **Databricks** using **Delta Lake**, providing a scalable and efficient way to process and query large datasets.

5. **Loading into Snowflake**: Finally, the processed data is transferred from Databricks to **Snowflake** for advanced analytics, querying, and reporting.

---

## 🛠️ Prerequisites

Before running the project, ensure you have the following:

- **Python 3.x**
- **Libraries**:
  - `requests`
  - `beautifulsoup4`
  - `azure-storage-blob`
  - `pyspark` (for Databricks)
- **Azure Blob Storage**: An Azure account and a container to store the downloaded files.
- **Databricks Workspace**: A Databricks account and a cluster for processing the data.
- **Snowflake Account**: A Snowflake account and the necessary credentials to load the data.

You can install the required Python packages using `pip`:

```bash
pip install requests beautifulsoup4 azure-storage-blob pyspark
