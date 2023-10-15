import boto3
ec2_client = boto3.client('ec2', region_name='us-east-1')
# - parameters: **service_name** (_string_) – The name of a service; **region_name** (_string_) – The name of the region associated with the client. A client is associated with a single region.


# Function to launch instances 
def launch_instance(tag_value, image_id='ami-', instance_type='t2.micro', key_name='key-pair'):
	try: # to prevent a crash (IAM issue, invalid AMI ID, invalid key name, invalid parameters, limits exceeded, etc. )
		instance = ec2_client.run_instances( 
			ImageId=image_id, 
			MinCount=1, 
			MaxCount=1, 
			InstanceType=instance_type, 
			KeyName=key_name, 
			TagSpecifications=[ 
				{
					'ResourceType': 'instance', #  When you specify a tag, you must specify the resource type to tag, otherwise the request will fail.
					'Tags': [ # list of tags to apply to resource
						{ 
							'Key': 'Environment', # describes tag						
							'Value': tag_value # value of tag 
						} 
					] 
				} 
			] 
		) 
		return instance['Instances'][0]['InstanceId'] # the variable 'instance' has the response from the 'run_instances' method. The first (and in this case, only) dictionary (element[0]) from the list for dictionaries that represent the instances (['Instances']) is isolated, and the value of its key 'InstanceId' is returned as the output of the function 
	except Exception as e: # catches the error and stores it in the variable 'e'
		print(f"An error occurred: {e}") 
		return None # good practice to alwasy include 'return None' in except blocks to facilitate debugging and program flow control

# Launch two 'dev' instances
dev_instance_ids = [] # creating a list for the Dev instance IDs is valuable for programattic tracking and performance of bulk operations. 
for _ in range(2):
    instance_id = launch_instance('Dev') # the string 'Dev' is passed the an argument for the launch_instances function, which will apply it as the value of the environment tag for the instances created. 
    dev_instance_ids.append(instance_id) # the output of the function, each instance id, is added to the list 'dev_instance_ids'
    print(f"Dev instance with ID '{instance_id}' has been created.") # for each instance launched, this print statement is issued.

# Launch one 'prod' instance
prod_instance_id = launch_instance('Prod')
print(f"Prod instance with ID '{prod_instance_id}' has been created.")

print("Dev Instances:", dev_instance_ids)
print("Prod Instance:", prod_instance_id)