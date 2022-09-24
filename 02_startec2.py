import boto3
client = boto3.client('ec2')
response = client.start_instances(
    InstanceIds=[
        'i-07e46e381cda3a017'
    ]
)




