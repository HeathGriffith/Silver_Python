import boto3

def create_sqs_queue(queue_name):
   sqs = boto3.client('sqs')
   response = sqs.create_queue(QueueName=queue_name)
   queue_url = response['QueueUrl']
   print(f'Queue URL: {queue_url}')

if __name__ == "__main__":
   queue_name = "LUIT-queue"
   create_sqs_queue(queue_name)