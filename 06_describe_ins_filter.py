from logging import Filter
from warnings import filters
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


print("Describing tagged EC2 Describing Filter Example Below")



# Added 1 tag like below - 
# Key = env
# Value= Prod
# in filter use like - # tag:key and value

response = client.describe_instances(
    Filters=[
        {
            'Name': 'tag:env',
            'Values': ['prod']
        }
    ]
)

for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        print("Instance is {}".format(instance['InstanceId']))
        print ("public DSN name is {}".format(instance['PublicDnsName']))





