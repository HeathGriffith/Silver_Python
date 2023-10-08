# find put acl in boto3 doc

import boto3
s3 = boto3.client('s3')

response = s3.put_object_acl(ACL='public-read', Bucket = 'hgriffith-boto3-10052023', Key = 'test_text.txt')
print(response)

# must turn off *block public access* on bucket