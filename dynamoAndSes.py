import json
import boto3
from urllib.parse import parse_qs
import time
import decimal
import base64

dynamodb = boto3.resource('dynamodb')
MAILFROM = 'ichikawa.fumiya@gmail.com'
def sendmail(to, subject, body):
    client = boto3.client('ses', region_name='us-east-1')
    
    response = client.send_email(
        Source=MAILFROM,
        ReplyToAddresses=[MAILFROM],
        Destination= {
            'ToAddresses': [to]
        },
        Message={
            'Subject':{
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

def next_seq(table, tablename):
    response = table.update_item(
        Key={
            'tablename': tablename
        },
        UpdateExpression="set seq = seq + :val",
        ExpressionAttributeValues= {
            ':val': 1
        },
        ReturnValues='UPDATED_NEW'
    )
    return response['Attributes']['seq']

def lambda_handler(event, context):
    try:
        seqtable = dynamodb.Table('sequence')
        nextseq = next_seq(seqtable, 'user')
        
        body = base64.b64decode( event['body'] )
        param = parse_qs(body.decode('utf-8'))
        print(param)

        username = param['username'][0]
        email = param['email'][0]
        
        host = event['requestContext']['http']['sourceIp']
        now = time.time()
        
        s3 = boto3.client('s3')
        url = s3.generate_presigned_url(
            ClientMethod = 'get_object',
            Params = {'Bucket': 'letitride-test', 'Key': '同意書.pdf'},
            ExpiresIn = 48 * 60 * 60,
            HttpMethod = 'GET'
        )

        usertable = dynamodb.Table("user")
        usertable.put_item(
            Item={
                'id': nextseq,
                'username': username,
                'email': email,
                'accepted_at': decimal.Decimal(str(now)),
                'host': host,
                'url': url
            }
        )
        
        mailbody = """
        {0}様
        
        ご登録ありがとうございました。
        下記のURLからダウンロードできます。
        
        {1}
        """.format(username, url)
        sendmail(email, "登録ありがとうございました", mailbody)
        body={'result': 1}
        return {
            'statusCode': 200,
            'headers': {
                'content-type': 'application/json',
                'access-control-allow-origin': 'https://takeoutmap.s3-ap-northeast-1.amazonaws.com'
            },
            'body': json.dumps(body)
        }
    except:
        import traceback
        traceback.print_exc()
        return {
            'statusCode': 500,
            'headers': {
                'content-type': 'text/html'
            },
            'body': '<!DOCTYPE html><html><head><meta charset="UTF-8"></head><body>内部エラーが発生しました。</body></html>'
        }