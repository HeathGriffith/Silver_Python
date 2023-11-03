import boto3

def create_sqs_queue(queue_name):  # Define a function to create an SQS queue with a specified name
   sqs = boto3.client('sqs')  # Initialize an SQS client using boto3
   response = sqs.create_queue(QueueName=queue_name)  # Create the queue and store the response
   queue_url = response['QueueUrl']  # Extract the queue URL from the response
   print(f'Queue URL: {queue_url}')  # Print the queue URL

if __name__ == "__main__":  # Check if this script is being run directly
   queue_name = "LUIT-queue"  # Set the name of the queue
   create_sqs_queue(queue_name)  # Call the function to create the queue
