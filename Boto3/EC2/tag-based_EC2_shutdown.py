import boto3

# Handle exceptions
def handle_exception(e, context):
    print(f"An error occurred in {context}: {e}")


# List the 'Dev' instances
def get_dev_instance_ids(ec2_client):
    dev_instance_ids = []
    try:
        response = ec2_client.describe_instances(
            Filters=[
                {
                    'Name': 'tag:Environment',
                    'Values': ['Dev']
                },
                {
                    'Name': 'instance-state-name',
                    'Values': ['running']
                }
            ]
        )
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                dev_instance_ids.append(instance['InstanceId'])
        return dev_instance_ids
    except Exception as e:
        handle_exception(e, "getting 'Dev' instances")
        return []


# Stop instances
def stop_select_instances(ec2_client, instance_ids):
    try:
        ec2_client.stop_instances(InstanceIds=instance_ids)
        print(f"Successfully stopped instances: {instance_ids}")
    except Exception as e:
        handle_exception(e, "stopping instances")


if __name__ == "__main__":
    ec2_client = boto3.client('ec2', region_name='us-east-1')
    dev_instance_ids = get_dev_instance_ids(ec2_client)
    if dev_instance_ids:
        stop_select_instances(ec2_client, dev_instance_ids)
    else:
        print("No 'Dev' instances to stop.")
