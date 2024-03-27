from azure.storage.blob import BlobServiceClient

# Set your Azure Blob Storage account credentials
connection_string = "your_connection_string"

def list_containers():
    try:
        # Create a BlobServiceClient
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)

        # List containers
        containers = blob_service_client.list_containers()

        print("List of containers:")
        for container in containers:
            print(container.name)

    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    list_containers()
