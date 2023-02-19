# Azure Cloud Connection
=======
# Accessing Azure Blob Storage with Python

This repository contains two examples of how to interact with Azure Blob Storage using Python. The first example (`connection_string.py`) shows how to download and upload a file using the Azure Blob Storage Python SDK and a connection string. The second example (`sas_token.py`) shows how to download and upload a file using a shared access signature (SAS) token.

## Prerequisites

To run these examples, you need:

- An Azure subscription
- A storage account in Azure
- An environment with Python 3.x installed
- The following Python packages installed:
  - `azure-storage-blob`
  - `python-dotenv`

## Using Connection String

1. Set the following environment variables in a `.env` file:

- connection_string=<your_connection_string>
- container_name=<your_container_name>
- file_path=<your_file_path>

2. Run the code in `connection_string.py` to download the blob, modify it, and upload it to the container with a new file name.

- This code downloads the blob from the specified container and file path to a local file, `temp2_gapminder.csv`, modifies the contents of the file, and uploads it to the container with a new file name, `new2_gapminder.csv`.

## Using SAS Token

1. Set the following environment variable in a `.env` file:

- blob_url=<your_blob_url_with_sas_token>

2. Run the code in `sas_token.py` to download the blob, modify it, and upload it to the container with a new file name.

This code downloads the blob from the specified blob URL to a local file, `temp1_gapminder.csv`, modifies the contents of the file, and uploads it to the container with a new file name, `new1_gapminder.csv`.

## Further Reading

For more information on accessing Azure Blob Storage with Python, see the [Azure SDK for Python documentation](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-python).


## Note

This example script is for demonstration purposes only and is not intended for use in production environments. 

