import boto3
client=boto3.client('ec2')

response = client.describe_instances(
    Filters=[
        {
            'Name': 'instance-state-name',
            'Values': ['running']
        }
    ]
)

for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        print("Instance is {}".format(instance['InstanceId']))
        print ("public DSN name is {}".format(instance['PublicDnsName']))

