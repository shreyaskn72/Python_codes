# Azure Blob Storage SAS Token Generator

This Python script allows you to add a Shared Access Signature (SAS) token to a blob URL in Azure Blob Storage.

## Prerequisites

Before running this script, make sure you have the following:

- Python installed on your system
- An Azure Blob Storage account
- Azure Storage account key
- The blob URL for which you want to generate a SAS token

## Installation

1. Clone this repository:
```
git clone <repository_url>
```

2. Install the required dependencies:

```
pip install azure-storage-blob
```

## Usage

1. Replace the placeholders in the script with your Azure Blob Storage credentials and blob details:

   - `storage_account_name`: Your Azure Storage account name.
   - `container_name`: The name of the container containing the blob.
   - `blob_name`: The name of the blob for which you want to generate a SAS token.
   - `account_key`: Your Azure Storage account key.

2. Run the script:

```
python add_saas_to_blob_url.py
```

3. The script will add a SAS token to the blob URL and print the updated URL with the SAS token.

## Example

```python
# Replace these variables with your Azure Blob Storage credentials and blob details
storage_account_name = "your_storage_account_name"
container_name = "your_container_name"
blob_name = "your_blob_name"
account_key = "your_account_key"

# Add a SAS token to the blob URL
blob_url_with_sas = add_sas_to_blob_url(storage_account_name, container_name, blob_name, account_key)

print("Blob URL with SAS:", blob_url_with_sas)
```