import boto3

# main three boto3 interfaces (ways boto3 communicates with AWS):


# (1) Session object to connect directly to AWS. Pass in keys as starting point. Initialize a session using Amazon S3
session = boto3.Session(profile_name='iamadmin-heath3')

# (2) client interface: talk about specific service, 
# can call directly from session
s3 = session.client('s3')
#can also call directly from boto3 [most of time]: s3 = boto3.client('s3')

# (3) resource interface: s3 = boto3.resource('s3') 
# can also be directly called from session: s3 = session.resource('s3') 
#   [things come back like an api, similar to Python classes]
#  can be directly called from session as well

# client gives more API type responses; resource, more Python way: we'll be using client

# The `create_bucket` method is called on the `s3` client object, 
s3.create_bucket(Bucket='testing-a-bucket-321')

# List all buckets
response = s3.list_buckets()
buckets = [bucket['Name'] for bucket in response['Buckets']]
''' or as a basic *for* loop:
buckets = []

for bucket in response['Buckets']:
    buckets.append(bucket['Name'])
'''
print(f'You have {len(buckets)} buckets: {", ".join(buckets)}')
