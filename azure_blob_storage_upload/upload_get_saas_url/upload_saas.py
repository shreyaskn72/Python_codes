from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, generate_blob_sas, BlobSasPermissions
from datetime import datetime, timedelta

def upload_to_azure_blob(storage_connection_string, container_name, file_path, blob_name):
    # Create a BlobServiceClient using the connection string
    blob_service_client = BlobServiceClient.from_connection_string(storage_connection_string)

    # Get a container client
    container_client = blob_service_client.get_container_client(container_name)

    # Create a blob client
    blob_client = container_client.get_blob_client(blob_name)

    # Upload the file to blob storage
    with open(file_path, "rb") as data:
        blob_client.upload_blob(data)

    # Get a SAS token for the blob (valid for 24 hours)
    token = generate_blob_sas(
        blob_client.account_name,
        container_name,
        blob_name,
        permission=BlobSasPermissions(read=True),
        expiry=datetime.utcnow() + timedelta(hours=24)
    )

    # Construct the URL for the blob with the SAS token
    blob_url = f"{blob_client.url}?{token}"

    return blob_url, blob_name

# Replace these variables with your Azure Blob Storage credentials and file details
storage_connection_string = "your_storage_connection_string"
container_name = "your_container_name"
file_path = "path_to_your_file"
blob_name = "name_for_blob_in_storage"

# Call the function to upload the file
blob_url, blob_name = upload_to_azure_blob(storage_connection_string, container_name, file_path, blob_name)
print("Uploaded to:", blob_url)
print("Blob Name:", blob_name)
