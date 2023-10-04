import boto3

# Initialize a session using Amazon S3
session = boto3.Session(profile_name='iamadmin-heath3')
s3 = session.client('s3')

# Create a new bucket
s3.create_bucket(Bucket='testing-a-bucket-321')

# List all buckets
response = s3.list_buckets()
buckets = [bucket['Name'] for bucket in response['Buckets']]
print(f'You have {len(buckets)} buckets: {", ".join(buckets)}')
