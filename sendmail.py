import json
import boto3

sqs = boto3.resource('sqs')
s3 = boto3.resource('s3')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('mailaddress')

client = boto3.client('ses', region_name='us-east-1')
MAILFROM = 'ichikawa.fumiya@gmail.com'

def lambda_handler(event, context):
    # SNSの通知はeventから運ばれる
    for rec in event['Records']:
        snsmessage = rec['Sns']['Message']
        #取得するqueue box
        queue = sqs.get_queue_by_name(QueueName=snsmessage)
        print(queue)
        #queueの取得
        messages = queue.receive_messages(
            MessageAttributeNames=['All'],
            MaxNumberOfMessages=10
        )
        print(messages)
        for m in messages:
            email = m.body
            if m.message_attributes is not None:
                print("Sending...")
                username = m.message_attributes.get('username').get('StringValue')
                backetname = m.message_attributes.get('backetname').get('StringValue')
                filename = m.message_attributes.get('filename').get('StringValue')
                
                print(backetname)
                print(filename)
                print(username)
                print(email)
                
                obj = s3.Object(backetname, filename)
                response = obj.get()
                maildata = response['Body'].read().decode('utf-8')
                datas = maildata.split("\n", 3)
                subject = datas[0]
                body = datas[2]
                
                print(subject)
                print(body)
                
                response = table.update_item(
                    Key = {
                        'email': email
                    },
                    UpdateExpression = 'set issend=:val',
                    ExpressionAttributeValues = {
                        ':val': 1
                    },
                    ReturnValues = 'UPDATED_OLD'
                )
                
                if response['Attributes']['issend'] == 0:
                    response = client.send_email(
                        Source=MAILFROM,
                        ReplyToAddresses=[MAILFROM],
                        Destination={
                            'ToAddresses':[
                                email
                            ]
                        },
                        Message={
                            'Subject': {
                                'Data': subject,
                                'Charset': 'UTF-8'
                            },
                            'Body': {
                                'Text': {
                                    'Data': body,
                                    'Charset': 'UTF-8'
                                }
                            }
                        }
                    )
                else:
                    print("Resend Skip")
                    
                print("Send To" + email)
            else:
                print("Message None")
            
            m.delete()