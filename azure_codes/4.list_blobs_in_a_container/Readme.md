# Azure Blob Storage Blob Listing

This Python script allows you to list all blobs in a container of your Microsoft Azure Blob Storage account.

## Prerequisites

- Python 3.x installed on your machine
- Azure Storage SDK for Python (`azure-storage-blob`) installed. You can install it using pip:
```
pip install azure-storage-blob
```

## Usage

1. Set up your Azure Blob Storage account and obtain the connection string.
2. Replace `"your_connection_string"` in the script with your Azure Blob Storage account connection string.
3. Replace `"your_container_name"` with the name of the container whose blobs you want to list.
4. Run the script using the following command:
```
python list_blobs.py
```

## Script Explanation

- `list_blobs.py`: Python script that lists all blobs in a container of the Azure Blob Storage account.
