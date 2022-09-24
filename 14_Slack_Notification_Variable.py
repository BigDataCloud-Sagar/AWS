import requests
import json
import os

# SLACK_WEBHOOK is an Env Variable at Lambda
slack_web_hook= os.environ['SLACK_WEBHOOK']

def send_Slack(event, context):
    print(str(event))
    slack_message = {'text': 'EC2 Instance Stopped'}
    resp =requests.post(slack_web_hook,data=json.dumps(slack_message))
    return resp.text