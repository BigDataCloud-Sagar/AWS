import boto3
client = boto3.client('ec2')
response = client.terminate_instances(
    InstanceIds=[
        'i-07e46e381cda3a017'
    ]
)

for instance in response['TerminatingInstances']:
    print ("The instance with id {} Terminated ".format(instance['InstanceId']))
