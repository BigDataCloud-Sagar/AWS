import boto3
ec2 = boto3.resource('ec2')


for instance in ec2.instances.all():
    print("InstanceId is {} and instance type is {}".format(instance.instance_id,instance.instance_type))

    
