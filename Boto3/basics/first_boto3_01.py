import boto3

# (1) 
session = boto3.Session(profile_name='iamadmin-heath3')

# (2) 
s3 = session.client('s3')

# (3) 
s3 = boto3.resource('s3') 

# (4)
s3.create_bucket(Bucket='testing-a-bucket-321')

# List all buckets
response = s3.list_buckets()
buckets = [bucket['Name'] for bucket in response['Buckets']]

# or as a *for* loop:
''' 
buckets = []

for bucket in response['Buckets']:
    buckets.append(bucket['Name'])
'''

print(f'You have {len(buckets)} buckets: {", ".join(buckets)}')
