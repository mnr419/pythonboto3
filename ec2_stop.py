import boto3

# Create an ec2 client

ec2 = boto3.client('ec2')

# Stop the instance
instance_id = 'i-0b4c51b8dd01d748f'

ec2.terminate_instances(InstanceIds=[instance_id])

print(f'Terminated the instance {instance_id}')