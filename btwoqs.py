import boto3
import threading
from time import sleep

sqs = boto3.resource('sqs')

# Read all available queues for the configured AWS Profile
def read_all_queues():
    for queue in sqs.queues.all():
        queue_name = queue.attributes['QueueArn'].split(':')[-1]
        for msg in queue.receive_messages(WaitTimeSeconds=0, MaxNumberOfMessages=2):
            print("Queue '{0}' has Message '{1}'".format(queue_name, msg.body))
            msg.delete()
        else:
            print("Found nothing in queue", queue_name)

class MyThread(object):
    def __init__(self, interval = 1): # C'tor
        self.interval = interval
        th = threading.Thread(target=self.run, args=())
        th.daemon = True
        th.start()

    def run(self):
        while True: # Runs forever until main exits.
            read_all_queues()
            sleep(self.interval) # Sleep a bit before polling again
            print('Press Enter to exit...\r')
                
def main():
    qthread = MyThread()
    input('Press Enter to exit...\r')
    print('Exiting process!\r')

if __name__ == '__main__':
    main()