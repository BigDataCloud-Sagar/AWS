# AWS #Python #Boto3
Boto3 is Amazon Web Services (AWS) Software Developmet kit (SDK) for Python.

This Project is Designed for Revising Python Boto3 for connecting AWS cloud 
and perform day to day requirment on Cloud Based Project.

For Using Boto3, we need to Perform below steps at the begining -

- Install python ( 3.6 ) and pip at local system ( mac )
    for pip - python3 get-pip.py
- Now install boto3
    for boto3 - pip3 install boto3
- pycharm nice edittor for Python 
- install AWS CLI at local system ( pip install aws-cli)
- Set Access key and Secret key in Laptop so that can connect to AWS from Local ( programatically )
    for this - aws configure ( and provide both values )


# About Lambda
Lambda can Trigger Based on Event thats y there is a event passed here.
if we dont pass anything in event thats also acceptable ( than Lambda will behave like normal func )

import json
def lambda_handler(event, context):
    # TODO implement
    res= 'Hello {} ! What are you doing here?'.format(event['name'])
    return res

Event while run -
{
  "name": "sagar"
}

Output - 
"Hello sagar ! What are you doing here?"


# Lambda Performance Tuning

Time out Increase 15 min
Memory Increased 128 MB

Note - it should be running in same VPC where resources are then only it can access those resources.

# Lambda Versions & Alias
Version & Alias in Lambda - by Cloudwatch rule to (Target) Lambda - but this does not look so nice.

# Lamda Notification on any event to teams / Slacks 
# Layers 
Useful.Adding the external Module Dependencies are Imp.
Adding it with Each fun and Zip did work but It is not good idea. 
What if each fun need same external Dependecies then external dependecies with Each zip is duplicated.

better way to manage is - layers
Example at Folder - Python_Layer

commands -
pip3 install -t python_layer requests
Now see in python_layer you can see dependecy of request module added.

Zip this folder for Creting layer.
zip -r dependency.zip .
this dependency.zip we will Upload and Create layer.

Note - 
lambda Run time enviornment will not have all Dependencies.
For External Dependencies we create Layars Like requests module is not part of AWS Lambda run time environment.
Lamda run time env will have python specific dependecies like boto3 but obviously not all external one.

Need to Add the Layer to Lambda and then Lambda Worked


# Passing Variable in lambda
My env Variables
In that we can set many imp things -
env - tst/prod
table1- xyz
anyothervariable - abc

# Encryption of Variables passed to lambda
Need to use some KMS keys
( not much imp see later )


# Find Ununsed Volume and send email ( make Program Later )
Read it later if needed
Basically ec2_client.describe_volumes()
this will retun multiple volume objects
then checked in loop for which volume, attachment lengh is 0 it means that is not in use.
use all those volume id put it in array 
create email body
create SNS topic and attache to 1 email 
and then Sns_client.publish ;)


# event handling ( Json to Dynamodb)
json file uploaded to S3 , a lambda Trigger and that Store Data at Dynambodb.
best way - S3 file upload Trigger a SNS that SNS output go to SQS and than trigger a Lambda and that Lambda can Trigger a Step fun and all.

# CSV to Dynamodb 
Looks Json are better for Inserting at Dynamodb
for CSV we need to use split a lot 
check code.

# Scheduling start and stop EC2 instances ( imp Automation )
cloudwatch Schedule target Lambda

# Removing Unused AMI's ( Custom AMI's)-
not that imp check code later
in this Example - Nice thing how to remove duplicates in list
abc=[]
for ami in amis:
    if ami not in abc:
        abc.appen(ami)

# Email Notification - Ec2 instance Stopped in prod
I can do it ;)

# Dynamodb 
No sql Database
primary key or partition key.( this is mendatory field rest are options. At run time we can add multiple attributes to the tables as Dynamodb support Dynamic Schema )

Data Distribution - in  Multinode case, Dynamodb calculate the hash value of each primary key and based on this
data sits on different different nodes.

Relation Database -
Records , columns

at Dynamodb
items , Attributes

Put item, get item , delete item
Batch writes

# S3 
create_bucket
put_object
delete_object
list_objects
list_bucket

# S3
Fetching Partial Info from file and put it in Dynamodb or Redshift
S3 select
Read it Later

# Find Elastic Ip's List and email it via simple email Service ( SES)
CHeck SES its nice.













