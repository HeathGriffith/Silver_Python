# how to upload objects into boto3

import boto3

s3 = boto3.client('s3')
r'''
# boto3 documentation to get function. 
# Method (1)  Use put_object function in this case
# lots of options, search 'required': Bucket (string); Key(string) [where placing object in bucket]
# we need to send in object: Body(bytes or seeekable file-like object)

# to pass body to function, must load it in memory
# I put the path because of trouble finding the file, prefixing with *r* removed Python backslash function
# *open* function denotes which mode the file is opened in, *rb* stands for read binary, the correct mode...
#   for uploading files to s3

#with open(r'C:\Users\heath\OneDrive\Documents\VSCode\Python Learning\LUIT\Silver_Python\test_text.txt', 'rb') as f:
#    s3.put_object(Bucket='hgriffith-boto3-10052023', Key="test_text.txt", Body=f, ContentType='text/plain')

# Method (2) Instead of loading to memory, can *upload_file* instead of *put_object* (fewer parameters but can pass
#   in parameters needed in *ExtraArgs*. Added '_upload' to key to see the difference

s3.upload_file(r'C:\Users\heath\OneDrive\Documents\VSCode\Python Learning\LUIT\Silver_Python\test_text.txt', 
               'hgriffith-boto3-10052023', "test_text_upload.txt", ExtraArgs={'ContentType':'text/plain'})

# List the objects in your bucket
# For APIs, always use most up to date -- list_objects_v2; *Bucket* is required
response = s3.list_objects_v2(Bucket='hgriffith-boto3-10052023')

# Check if the 'Contents' key is present in the response (i.e., the bucket is not empty)
# Note: for loop would work without if-else lines
if 'Contents' in response:
    for item in response['Contents']:
        print(item['Key'], item['Size'])  # Print the name and size of each file
else:
    print('No objects found in bucket.')

# Search filters -- folder/folder_a, for example, (1) gives root and objects nested inside the folder
#   based on the prefix for the keys of the object:
   response = s3.list_objects_v2(Bucket='hgriffith-boto3-10052023', Prefix = 'folder/folder_a/')
'''
#   E.g., (2) file extension (Boto3 doesn't do natively). Iterate through
response = s3.list_objects_v2(Bucket='hgriffith-boto3-10052023')

for content in response["Contents"]:
    if('.txt' in content["Key"]):
        print(content["Key"])

# improve so that last four characters are '.txt':

for content in response["Contents"]:
    if('.txt' in content["Key"][-4:]):
        print(content["Key"])

# make it dynamic:

extension = '.txt'

for content in response["Contents"]:
    if(extension in content["Key"][-(len(extension)):]):
        print(content["Key"])

# make it a function
# pass in client because don't want global things, pass in extension
def filter_objects_extension(client, extension):
    keys = []
    response = client.list_objects_v2(Bucket='hgriffith-boto3-10052023')
    for content in response["Contents"]:
        if(extension in content["Key"][-(len(extension)):]):
            keys.append(content["Key"])

# Also must pass in bucket to prevent hard-coded values
def filter_objects_extension(client, bucket, extension):
    keys = []
    response = client.list_objects_v2(Bucket=bucket)
    for content in response["Contents"]:
        if(extension in content["Key"][-(len(extension)):]):
            keys.append(content["Key"])
    return keys

response = filter_objects_extension(s3, "hgriffith-boto3-10052023", ".txt.")
print(response)

# can change '.txt' to '/' because will pull back all folders

# Another simple function 

def list_object_keys(client, bucket, prefix = ""):
    keys = []
    response = client.list_objects_v2(Bucket=bucket, Prefix = prefix)
    for content in response["Contents"]:
        keys.append(content["Key"])
    return keys

response = list_object_keys(s3, "hgriffith-boto3-10052023", "/")
print(response)

response = filter_objects_extension(s3, "hgriffith-boto3-10052023", "/")
print(response)