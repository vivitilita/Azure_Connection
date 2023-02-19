# Import libraries
from azure.storage.blob import BlobClient
from dotenv import load_dotenv
import os

# Load the environment variables from the .env file
load_dotenv()

# Construct the blob URL with the SAS token
blob_url = os.getenv("blob_url")

# Create a BlobServiceClient using the blob URL
blob_client = BlobClient.from_blob_url(blob_url)

# Download the blob to a local file
local_file_path = "temp1_gapminder.csv"
with open(local_file_path, "wb") as data:
    download_stream = blob_client.download_blob()
    data.write(download_stream.readall())

# Modify the contents of the local file
with open(local_file_path, "r") as data:
    # Do something with the file contents
    print(data.read())

# Upload the modified file to Azure Blob Storage with a new file name
new_file_path = "new1_gapminder.csv"
with open(local_file_path, "rb") as data:
    blob_client.upload_blob(data, overwrite=True)
