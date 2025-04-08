import requests
from bs4 import BeautifulSoup

from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import re


url = 'https://www.sec.gov/data-research/sec-markets-data/financial-statement-data-sets'

headers = {
    "User-Agent": "jo boulement jo@gmx.at",  # Set the User-Agent to identify the client
    "Accept-Encoding": "gzip, deflate"  # Accept gzip and deflate encodings
}

response = requests.get(url, headers = headers)

soup = BeautifulSoup(response.content, 'html.parser')


zip_links = []

for link in soup.find_all('a', href=True):
    href = link['href']
    if href.endswith('.zip'):
        zip_links.append('https://www.sec.gov'+ href)

zip_links


connection_string = ''
container_name = 'bronzelayer'

blob_service_client =  BlobServiceClient.from_connection_string(connection_string)

def download_to_blob(url, blob_name):
    response = requests.get(url, headers = headers)
    if response.status_code == 200:
        blob_client = blob_service_client.get_blob_client(container = container_name, blob = blob_name)
        blob_client.upload_blob(response.content, overwrite = True)
        print(f'file{blob_name} uploaded successfully')
    else:
        print('failed to upload')


def main():
    for url in zip_links:
        blob_name = url.split('/')[-1]
        download_to_blob(url, blob_name)



if __name__ == "__main__":
    main()
