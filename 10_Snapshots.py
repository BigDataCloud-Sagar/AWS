#Snapshots for all volumes of all those Ec2 who has a tag name as Backup and its value is yes

import boto3
ec2=boto3.resource('ec2')
sns_client=boto3.client('sns')

myfilter=[
    {
        'Name': 'tag:Backup',
        'Values': ['yes']
    }
]

snapshot_ids=[]

for instance in ec2.instances.filter(Filters=myfilter):
    for vol in instance.volumes.all():
        snapshot=vol.create_snapshot(Description='By using Boto3')
        snapshot_ids.append(snapshot.snapshot_id)

sns_client.publish(
    TopicArn='arn:aws:sns:us-east-1:012413420184:snapshot',
    Subject='EBS Snapshots',
    Message=str(snapshot_ids)
)