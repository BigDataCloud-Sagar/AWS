import boto3
client = boto3.client('ec2')
response = client.terminate_instances(
    InstanceIds=[
        'i-0c20aa1c9eb515fea'
    ]
)

for instance in response['TerminatingInstances']:
    print ("The instance with id {} Terminated ".format(instance['InstanceId']))

