# Azure Blob Storage File Uploader

This Python script allows you to upload files to Azure Blob Storage.

## Prerequisites

Before running this script, make sure you have the following:

- Python installed on your system
- An Azure Blob Storage account
- Azure Storage connection string
- Azure Storage container created to store the uploaded files

## Installation

1. Clone this repository:

git clone <repository_url>

2. Install the required dependencies:

pip install azure-storage-blob


## Usage

1. Replace the placeholders in the script with your Azure Blob Storage credentials and file details:

   - `storage_connection_string`: Your Azure Storage connection string.
   - `container_name`: The name of the container in Azure Blob Storage where you want to upload the file.
   - `file_path`: The local file path of the file you want to upload.
   - `blob_name`: The desired name for the blob in Azure Blob Storage.

2. Run the script:

python upload_to_azure_blob.py


3. The script will upload the specified file to Azure Blob Storage. Once uploaded, it will display the URL of the uploaded blob and the blob name.

## Example

```python
# Replace these variables with your Azure Blob Storage credentials and file details
storage_connection_string = "your_storage_connection_string"
container_name = "your_container_name"
file_path = "path_to_your_file"
blob_name = "name_for_blob_in_storage"

# Call the function to upload the file
blob_url, blob_name = upload_to_azure_blob(storage_connection_string, container_name, file_path, blob_name)
print("Uploaded to:", blob_url)
print("Blob Name:", blob_name)


