import boto3
ec2 = boto3.resource('ec2')


for instance in ec2.instances.all():
    print("InstanceId is {} and instance type is {}".format(instance.instance_id,instance.instance_type))

    
# ec2.instalce.all() -
# return type
# list(ec2.Instance) - list of ec2.instance objects
# on this Instance we can access its Properies like Instance id , instance type etc