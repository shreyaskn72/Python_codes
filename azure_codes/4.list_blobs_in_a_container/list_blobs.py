from azure.storage.blob import BlobServiceClient, ContainerClient

# Set your Azure Blob Storage account credentials
connection_string = "your_connection_string"
container_name = "your_container_name"

def list_blobs():
    try:
        # Create a ContainerClient
        container_client = ContainerClient.from_connection_string(conn_str=connection_string, container_name=container_name)

        # List blobs in the container
        blob_list = container_client.list_blobs()

        print("List of blobs:")
        for blob in blob_list:
            print(blob.name)

    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    list_blobs()
