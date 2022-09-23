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





