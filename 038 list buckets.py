import boto3

s3 = boto3.client('s3')

response = s3.list_buckets()

# print(response)
# copy to json formatter: see how to parse by looking to keys, then :

# (1) Extract the list of bucket dictionaries from the response using the 'Buckets' key
buckets = response['Buckets']

# (2) Iterate through the list of bucket dictionaries to print the name and creation date
for bucket in buckets:
    print(bucket["Name"], bucket['CreationDate'])