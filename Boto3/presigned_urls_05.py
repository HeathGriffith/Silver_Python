import boto3
s3 = boto3.client('s3')

# find presigned_url in Boto3 documentation (search for code that can actually run in code examples)

response = s3.generate_presigned_url('get_object', 
                                     Params={'Bucket': 'hgriffith-boto3-10052023', 
                                                           'Key': 'https://hgriffith-boto3-10052023.s3.amazonaws.com/test_text.txt'}, 
                                                           ExpiresIn=300)

print(response)