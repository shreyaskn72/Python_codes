from azure.storage.blob import BlobClient

# Set your Azure Blob Storage account credentials
connection_string = "your_connection_string"
container_name = "your_container_name"
blob_name = "your_blob_name"
download_file_path = "downloaded_blob.txt"  # Path where the blob will be downloaded

def download_blob():
    try:
        # Create a BlobClient
        blob_client = BlobClient.from_connection_string(conn_str=connection_string, container_name=container_name, blob_name=blob_name)

        # Download the blob data
        with open(download_file_path, "wb") as download_file:
            download_file.write(blob_client.download_blob().readall())

        print(f"Blob '{blob_name}' downloaded successfully.")

    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    download_blob()
