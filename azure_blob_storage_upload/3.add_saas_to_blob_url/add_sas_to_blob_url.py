from azure.storage.blob import BlobServiceClient, BlobClient, generate_blob_sas, BlobSasPermissions
from datetime import datetime, timedelta

def add_sas_to_blob_url(storage_account_name, container_name, blob_name, account_key, duration_hours=1):
    # Create a BlobClient for the blob
    blob_client = BlobClient(account_url=f"https://{storage_account_name}.blob.core.windows.net",
                              container_name=container_name,
                              blob_name=blob_name,
                              credential=account_key)

    # Set the expiry time for the SAS token
    expiry = datetime.utcnow() + timedelta(hours=duration_hours)

    # Generate a SAS token for the blob
    sas_token = generate_blob_sas(
        account_name=storage_account_name,
        container_name=container_name,
        blob_name=blob_name,
        account_key=account_key,
        permission=BlobSasPermissions(read=True),
        expiry=expiry
    )

    # Construct the URL for the blob with the SAS token
    blob_url_with_sas = f"{blob_client.url}?{sas_token}"

    return blob_url_with_sas

# Replace these variables with your Azure Blob Storage credentials and file details
storage_account_name = "your_storage_account_name"
container_name = "your_container_name"
blob_name = "your_blob_name"
account_key = "your_account_key"

if __name__ == '__main__':
    # Add a SAS token to the blob URL
    blob_url_with_sas = add_sas_to_blob_url(storage_account_name, container_name, blob_name, account_key)

    print("Blob URL with SAS:", blob_url_with_sas)

