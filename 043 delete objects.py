import boto3
s3 = boto3.client('s3')

# deleting objects in documentation: often just need bucket and key (again)

bucket = 
key = 'testing-a-bucket-321'

response = s3.delete_object(
    Bucket = bucket,
    Key = key
)

