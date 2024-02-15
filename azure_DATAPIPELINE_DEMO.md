# AZURE BLOB >>> AZURE DATA FACTORY >>> AZURE SQL DATABASE

## CREATE AZURE BLOB STORAGE ACCOUNT AND UPLOAD THE DATASET 
![AZUREBLOB](https://github.com/Crocsover/ETL-PIPELINES/assets/139344602/0e03c3d7-c5dc-4abd-a8af-b85cfed9df5e)

## CREATE AZURE DATA FACTORY ACCOUNT AND SET UP PIPELINE
![ADF](https://github.com/Crocsover/ETL-PIPELINES/assets/139344602/35daf751-a028-4266-b436-7a914edaae11)


## CREATE AZURE SQL DATABASE AND CREATE A TABLE USING QUERY TOOL
![AZURESQL](https://github.com/Crocsover/ETL-PIPELINES/assets/139344602/ad7bb25b-941d-4896-bee2-791330a01f47)

To move CSV files from Azure Blob Storage to Azure SQL Database using Azure Data Factory, you would typically follow these steps:

1. **Create Azure Blob Storage:** If you haven't already, create an Azure Blob Storage account where your CSV files are stored.

2. **Create Azure SQL Database:** Similarly, create an Azure SQL Database where you want to load the data from CSV files.

3. **Create Azure Data Factory:** Set up an Azure Data Factory instance if you haven't already. This is the service that orchestrates and automates the movement and transformation of data.

4. **Create Linked Services:**
   - Create a linked service to connect to your Azure Blob Storage account.
   - Create another linked service to connect to your Azure SQL Database.

5. **Create Datasets:**
   - Create a dataset representing the CSV files in your Azure Blob Storage.
   - Create a dataset representing the target table in your Azure SQL Database.

6. **Create Copy Activity:**
   - Create a pipeline in Azure Data Factory.
   - Add a Copy Activity to the pipeline.
   - Configure the source dataset to point to your CSV files in Azure Blob Storage and the sink dataset to point to your target table in Azure SQL Database.
   - Define the mapping between the source and sink data columns if necessary.

7. **Schedule or Trigger the Pipeline:** Decide if you want to run the pipeline on a schedule or trigger it manually.

8. **Monitor and Troubleshoot:** Monitor the pipeline's execution in Azure Data Factory to ensure the data is being copied successfully. If any issues arise, troubleshoot them accordingly.

9. **Optimization and Automation:** Consider optimization techniques such as parallelism, partitioning, or incremental data loading to improve performance and efficiency. Additionally, automate the process as much as possible for seamless data integration.

By following these steps, you can efficiently move CSV files from Azure Blob Storage to Azure SQL Database using Azure Data Factory.
