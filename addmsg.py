import boto3
import datetime as dt

sqs = boto3.resource('sqs')

count = 1 # Number of messages to add per queue
queues = ['Test1', 'Test2']

def send_msg(queue, body):
    response = queue.send_message(MessageBody=body)
    print('Message:', body)
    print('MessageId:', response.get('MessageId'))
    print('MD5OfMessageBody:', response.get('MD5OfMessageBody'))

for queue_name in queues:
    queue = sqs.get_queue_by_name(QueueName=queue_name)
    for index in range(count):
        send_msg(queue, '{0} Queue: Test SQS Message {1}!'.format(queue_name, dt.datetime.now()))
