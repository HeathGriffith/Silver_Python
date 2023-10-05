# how to upload objects into boto3

import boto3

s3 = boto3.client('s3')
r'''
# boto3 documentation to get function. Use put_object function in this case
# lots of options, search 'required': Bucket (string); Key(string) [where placing object in bucket]
# we need to send in object: Body(bytes or seeekable file-like object)

# to pass body to function, must load it in memory
# I put the path because of trouble finding the file, prefixing with *r* removed Python backslash function
# *open* function denotes which mode the file is opened in, *rb* stands for read binary, the correct mode...
#   for uploading files to s3
with open(r'C:\Users\heath\OneDrive\Documents\VSCode\Python Learning\LUIT\Silver_Python\test_text.txt', 'rb') as f:
    s3.put_object(Bucket='hgriffith-boto3-10052023', Key="test_text.txt", Body=f)'''


# List the objects in your bucket
response = s3.list_objects_v2(Bucket='hgriffith-boto3-10052023')

# Check if the 'Contents' key is present in the response (i.e., the bucket is not empty)
if 'Contents' in response:
    for item in response['Contents']:
        print(item['Key'], item['Size'])  # Print the name and size of each file
else:
    print('No objects found in bucket.')
