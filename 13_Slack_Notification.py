import requests
import json

slack_web_hook = 'https://hooks.slack.com/services/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'


def send_Slack(event, context):
    print(str(event))
    slack_message = {'text': 'EC2 Instance Stopped'}
    resp =requests.post(slack_web_hook,data=json.dumps(slack_message))
    return resp.text