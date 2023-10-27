import boto3

def list_vpcs():
    ec2_resource = boto3.resource('ec2', region_name='us-east-1')
    for vpc in ec2_resource.vpcs.all():
        print(f"VPC ID: {vpc.id}, State: {vpc.state}, CIDR Block: {vpc.cidr_block}")

if __name__ == "__main__":
    list_vpcs()
