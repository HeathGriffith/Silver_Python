
# Three boto3 interfaces (ways boto3 communicates with AWS)::

# (1) Session Object: 
Connect directly to AWS. Pass in keys as starting point. Initialize a session using Amazon S3



# (2) Client Interface (specific service) 
can call directly from session
can also call directly from boto3 [most of time]: s3 = boto3.client('s3')

# (3) Resource Interface: 
can also be directly called from session: s3 = session.resource('s3') 


# Client vs. Resource
client gives more API-type responses; 
resource, more Pythonic.

# (4)
The `create_bucket` method is called on the `s3` client object, 


# List all buckets
response = s3.list_buckets()
buckets = [bucket['Name'] for bucket in response['Buckets']]
''' or as a basic *for* loop:
buckets = []

for bucket in response['Buckets']:
    buckets.append(bucket['Name'])
'''
print(f'You have {len(buckets)} buckets: {", ".join(buckets)}')