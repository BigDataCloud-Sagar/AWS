import boto3
client = boto3.client('ec2')
response = client.start_instances(
    InstanceIds=[
        'i-0c20aa1c9eb515fea'
    ]
)


