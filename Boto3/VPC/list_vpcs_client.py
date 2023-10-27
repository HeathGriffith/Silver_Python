import boto3

def list_vpcs():
    ec2_client = boto3.client('ec2', region_name='us-east-1')
    response = ec2_client.describe_vpcs()
    
    for vpc in response['Vpcs']:
        vpc_id = vpc['VpcId']
        vpc_state = vpc['State']
        cidr_block = vpc['CidrBlock']
        print(f"VPC ID: {vpc_id}, State: {vpc_state}, CIDR Block: {cidr_block}")

if __name__ == "__main__":
    list_vpcs()
