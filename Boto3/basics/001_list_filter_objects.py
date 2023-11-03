'''


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
'''

# list objects

def list_object_keys(client, bucket, prefix = ""):
    keys = []
    response = client.list_objects_v2(Bucket = bucket, Prefix = prefix)
    for content in response["Contents"]:
        keys.append(content["Key"])
    return keys

# no folder, leaving off prefix parameter 

if __name__ == '__main__':
    s3 = boto3.client('s3')

response = list_object_keys(s3, 'hgriffith-boto3-10052023')
print(response)
