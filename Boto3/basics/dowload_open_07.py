import boto3
import os

'''
s3 = boto3.client('s3')

# Specify your directory path
directory_path = "C:\\Users\\heath\\OneDrive\\Documents\\VSCode\\Python Learning\\LUIT\\Silver_Files"

# Join the directory path with the original filename
file_path = directory_path + "\\test_text_upload.txt"

s3.download_file('hgriffith-boto3-10052023', 'test_text_upload.txt', file_path)


# Function to download a single object:

s3 = boto3.client('s3')
bucket = 'hgriffith-boto3-10052023'
key = 'test_text_upload.txt'
filename = 'test_text_upload.txt'

def download_single_object(client, bucket, key, filename):
    client.download_file(bucket, key, filename)
    '''

    # Suppose we want to download all objects in the bucket. Create a function using documentation's terms
#   and *list_objects* command:

from 001_list_filter_objects import list_object_keys


def download_single_object(client, bucket, key, filename):
    client.download_file(bucket, key, filename)

if __name__ == '__main__':

    bucket = 'hgriffith-boto3-10052023'
    key = 'test_text_upload.txt'
    filename = 'test_text_upload.txt'

    s3 = boto3.client('s3')

    keys = list_object_keys(s3, bucket)
    
    for key in keys:
        if '/' == key[-1]:
            try:
                os.mkdir(key)
            else:
                download_single_object(client, bucket, key, key)