import boto3
client = boto3.client('ec2')
resp = client.run_instances(
    ImageId='ami-467ca739',
    InstanceType='t2.micro',
    MaxCount = 1,
    MinCount = 1
)

for instance in resp['Instances']:
    print(instance['InstanceId'])

# Inside AWS lambda I have tested this is Working ( only for Request we have added Layer for boto3 no layer 
# needed it is available in Lambda RunTime-

# import json
# import requests
# import boto3
# client = boto3.client('ec2')
# def lambda_handler(event, context):
#     resp = client.run_instances(
#     ImageId='ami-467ca739',
#     InstanceType='t2.micro',
#     MaxCount = 1,
#     MinCount = 1)


