# Extract, Transform, and Load Data Pipeline using Azure Databricks and Azure Data Factory

## Objective
Extract data from Azure Storage, transform it using Azure Databricks, and load it into Azure SQL Database.

## Prerequisites
- **Azure Subscription**: Access to Azure Portal.
- **Azure Storage Account**: Data source (e.g., CSV files).
- **Azure SQL Database**: Target database for transformed data.
- **Azure Databricks**: Workspace for data processing.
- **Azure Data Factory**: Orchestration tool for ETL pipelines.

## Setup Steps

### 1. Azure Databricks Setup
- **Create Azure Databricks Workspace**
  - Navigate to Azure Portal.
  - Create a new Databricks workspace.
  - Configure workspace settings.

- **Set Up Databricks Cluster**
  - Inside Databricks workspace, create a new cluster.
  - Choose instance types and configure auto-scaling.

- **Integration with Azure Storage**
  - Configure Databricks to access Azure Storage.
  - Use Service Principal or managed identities for authentication.

### 2. Azure Data Factory Setup
- **Create Azure Data Factory Instance**
  - Go to Azure Portal.
  - Create a new Azure Data Factory instance.
  - Connect it to your Azure Subscription.

- **Configure Linked Services**
  - Set up linked services for Azure Storage (input) and Azure SQL Database (output).
  - Configure Azure Databricks as a linked service.

- **Build Pipelines**
  - Create pipelines in Azure Data Factory.
  - Use Databricks Notebook Activity to trigger pipeline.

### 3. Implement ETL Process
- **Extract Data**
  - In Databricks notebooks, read data from Azure Storage.
  - Use Spark APIs to handle different file formats (e.g., CSV, Parquet).

- **Transform Data**
  - Perform data transformations using Spark DataFrame operations.
  - Clean data, perform aggregations, prepare for loading into Azure SQL Database.

- **Load Data**
  - Write transformed data into Azure SQL Database.
  - Use JDBC connection in Databricks to insert data into SQL tables.

### 4. Monitoring and Security
- **Monitor Performance**
  - Monitor Azure Databricks cluster performance.
  - Track Azure Data Factory pipeline executions using Azure Monitor.

- **Security and Permissions**
  - Ensure security measures are in place.
  - Use Azure Key Vault for storing sensitive data and credentials.

