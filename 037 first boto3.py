import boto3

# AWS Boto3 documatation: only required parameter to create bucket is *Bucket* (string)
# construct a call to AWS using Boto 3:
# Can delete all but bucket (but using variable 's3' instead of 'client'):

s3 = boto3.client('s3')

response = s3.create_bucket(
    Bucket = 'hgriffith-boto3-10052023'
)

print(response)

# paste response to a json formatter for readability