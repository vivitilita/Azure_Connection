# Import libraries
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv
import os

# Load the environment variables from the .env file
load_dotenv()

# Retrieve the credentials from the environment variables
connection_string = os.getenv("connection_string")
container_name = os.getenv("container_name")
file_path = os.getenv("file_path")

blob_service_client = BlobServiceClient.from_connection_string(connection_string)
blob_client = blob_service_client.get_blob_client(container_name, file_path)

# Download the file to a local temporary directory
local_file_path = "temp2_gapminder.csv"
with open(local_file_path, "wb") as data:
    data.write(blob_client.download_blob().readall())

# Open the file for reading
with open(local_file_path, "r") as data:
    # Do something with the file contents
    print(data.read())

# Upload the modified file to Azure Blob Storage with a new file name
new_file_path = "new2_gapminder.csv"
with open(local_file_path, "rb") as data:
    blob_client = blob_service_client.get_blob_client(container_name, new_file_path)
    blob_client.upload_blob(data)

