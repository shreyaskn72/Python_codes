from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

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

    # Construct the URL for the blob
    blob_url = f"https://{blob_service_client.account_name}.blob.core.windows.net/{container_name}/{blob_name}"

    return blob_url, blob_name

# Replace these variables with your Azure Blob Storage credentials and file details
storage_connection_string = "your_storage_connection_string"
container_name = "your_container_name"
file_path = "path_to_your_file"
blob_name = "name_for_blob_in_storage"

if __name__ == '__main__':
  # Call the function to upload the file
  blob_url, blob_name = upload_to_azure_blob(storage_connection_string, container_name, file_path, blob_name)
  print("Uploaded to:", blob_url)
  print("Blob Name:", blob_name)

