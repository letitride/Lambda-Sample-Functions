import json
import boto3

sqs = boto3.resource('sqs')
queue = sqs.get_queue_by_name(QueueName="mailsendqueue000")

sns = boto3.resource('sns')
topic = sns.Topic('arn:aws:sns:ap-northeast-1:865823437905:sendmail-notifications')

def lambda_handler(event, context):
    n = queue.attributes['ApproximateNumberOfMessages']
    for i in range(int((int(n) + 9) / 10)):
        print(i)
        topic.publish(
            Message='mailsendqueue000'
        )