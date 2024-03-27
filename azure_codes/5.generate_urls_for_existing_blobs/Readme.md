# Azure Blob Storage Blob URL Generator

This Python function allows you to generate both a normal URL without a SAS token and a signed URL with a SAS token for a blob in your Microsoft Azure Blob Storage account.

## Prerequisites

- Python 3.x installed on your machine
- Azure Storage SDK for Python (`azure-storage-blob`) installed. You can install it using pip:

pip install azure-storage-blob



## Usage

1. Set up your Azure Blob Storage account and obtain the connection string.
2. Replace `"your_connection_string"` in the script with your Azure Blob Storage account connection string.
3. Replace `"your_container_name"` with the name of the container containing the blob.
4. Replace `"your_blob_name"` with the name of the blob for which you want to generate the URLs.
5. Run the script using the following command:

python generate_blob_urls.py


## Function Explanation

The function `generate_blob_urls()` returns both a normal URL without a SAS token and a signed URL with a SAS token for the specified blob.

## Example Output

- Normal URL for the blob: https://your_storage_account.blob.core.windows.net/your_container_name/your_blob_name
- Signed URL for the blob: https://your_storage_account.blob.core.windows.net/your_container_name/your_blob_name?your_sas_token



## Documentation

- [Azure Blob Storage Documentation](https://docs.microsoft.com/en-us/azure/storage/blobs/)
