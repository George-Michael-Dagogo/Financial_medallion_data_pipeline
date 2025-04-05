import requests

headers = {
    "User-Agent": "jo boulement jo@gmx.at",  # Set the User-Agent to identify the client
    "Accept-Encoding": "gzip, deflate"  # Accept gzip and deflate encodings
}

def generate_sec_urls(start_year=2009, start_quarter = 1):
    urls = []

    while True:
        url = f'https://www.sec.gov/files/dera/data/financial-statement-data-sets/{start_year}q{start_quarter}.zip'
        print(f'checking url:{url}')
        response = requests.get(url, headers = headers)
        print(response.status_code)
        if response.status_code == 200:
            urls.append(url)
            start_quarter += 1
            if start_quarter > 4:
                start_quarter = 1
                start_year += 1
        else:
            break

    return urls


valid_urls = generate_sec_urls()



import requests
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

connection_string = ''
container_name = 'rawdata'

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
    for url in valid_urls:
        blob_name = url.split('/')[-1]
        download_to_blob(url, blob_name)



if __name__ == "__main__":
    main()
