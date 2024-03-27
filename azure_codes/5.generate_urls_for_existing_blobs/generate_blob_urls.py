from azure.storage.blob import BlobServiceClient, generate_blob_sas, BlobSasPermissions
from datetime import datetime, timedelta

# Set your Azure Blob Storage account credentials
connection_string = "your_connection_string"
container_name = "your_container_name"
blob_name = "your_blob_name"

def generate_blob_urls():
    try:
        # Create a BlobServiceClient
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)

        # Get the container client
        container_client = blob_service_client.get_container_client(container_name)

        # Get the blob client
        blob_client = container_client.get_blob_client(blob_name)

        # Construct the normal URL for the blob
        blob_url = blob_client.url

        # Define the start time and expiry time for the SAS token
        start_time = datetime.utcnow()
        expiry_time = start_time + timedelta(hours=1)  # SAS token will be valid for 1 hour

        # Generate the SAS token for the blob
        sas_token = generate_blob_sas(
            blob_client.account_name,
            container_name,
            blob_name,
            account_key=blob_client.credential.account_key,
            permission=BlobSasPermissions(read=True),
            expiry=expiry_time
        )

        # Construct the signed URL for the blob
        blob_url_with_sas = f"{blob_url}?{sas_token}"

        return blob_url, blob_url_with_sas

    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    normal_url, signed_url = generate_blob_urls()
    print("Normal URL for the blob:", normal_url)
    print("Signed URL for the blob:", signed_url)
