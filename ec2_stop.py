import boto3

# Create an ec2 client

ec2 = boto3.client('ec2')

# Stop the instance
instance_id = 'i-08c2f7cd1efe994c8'

ec2.terminate_instances(InstanceIds=[instance_id])

print(f'Stopped the instance {instance_id}')