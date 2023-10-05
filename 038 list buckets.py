import boto3

s3 = boto3.client('s3')

response = s3.list_buckets()

# print(response)
# copy to json formatter, helps see how to parse by looking to keys, then :

# Extract the list of bucket dictionaries from the response using the 'Buckets' key
buckets = response['Buckets']

# Iterate through the list of bucket dictionaries to print the name and creation date
for bucket in buckets:
    print(bucket["Name"], bucket['CreationDate'])