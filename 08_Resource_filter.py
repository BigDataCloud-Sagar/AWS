import boto3

ec2 = boto3.resource('ec2')

for instance in ec2.instances.filter(
Filters=[
        {
            'Name': 'tag:Name',
            'Values': ['Dev']
        }
    ]
):
    print("InstanceId is {} and instance type is {}".format(instance.instance_id, instance.instance_type))

print("Next Step")

for instance in ec2.instances.filter(
        Filters=[
            {
                'Name': 'availability-zone',
                'Values': ['us-east-1d']
            }
        ]
):
    print("InstanceId is {} and instance type is {}".format(instance.instance_id, instance.instance_type))





