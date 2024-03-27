from azure.storage.blob import ContainerClient



def create_container(connection_string, container_name):
    try:
        # Create a ContainerClient
        container_client = ContainerClient.from_connection_string(conn_str=connection_string, container_name=container_name)

        # Create the container
        container_client.create_container()

        print(f"Container '{container_name}' created successfully.")

    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    # Set your Azure Blob Storage account credentials
    connection_string = "your_connection_string"
    container_name = "your_container_name"
    create_container(connection_string, container_name)
