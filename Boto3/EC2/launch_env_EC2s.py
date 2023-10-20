import boto3
ec2_client = boto3.client('ec2', region_name='us-east-1')

# Function to launch instances 
def launch_instance(tag_value, image_id='ami-0df435f331839b2d6', instance_type='t2.micro'):
    try:
        instance = ec2_client.run_instances(
            ImageId=image_id,  
            MinCount=1, 
            MaxCount=1, 
            InstanceType=instance_type,
            TagSpecifications=[
                {
                    'ResourceType': 'instance',
                    'Tags': [
                        { 
                            'Key': 'Environment', 
                            'Value': tag_value 
                        }
                    ]
                }
            ]
        )
        return instance['Instances'][0]['InstanceId']
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Launch two 'Dev' instances
dev_instance_ids = []
for _ in range(2):
    instance_id = launch_instance('Dev')  
    dev_instance_ids.append(instance_id)
    print(f"Dev instance with ID '{instance_id}' has been created.")

# Launch one 'Prod' instance
prod_instance_id = launch_instance('Prod') 
print(f"Prod instance with ID '{prod_instance_id}' has been created.")

print("Dev Instances:", dev_instance_ids)
print("Prod Instance:", prod_instance_id)
