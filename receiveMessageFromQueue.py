import boto3
# Create SQS client
sqs_client =  boto3.client('sqs', region_name='us-east-2')

# Function to receive message from SQS queue
def receive_most_recent_ip(queue_url,max_num_of_msgs):
	response = sqs_client.receive_message(QueueUrl=queue_url,MaxNumberOfMessages=max_num_of_msgs)
	return response['Messages'][-1]

#Main function
def main():
	queue_url="" #provide queue url here
	max_num_of_msgs=5
	message = receive_most_recent_ip(queue_url,max_num_of_msgs)
	receipt_handle = message['ReceiptHandle']
	#Delete received message from queue
	sqs_client.delete_message(QueueUrl=queue_url,ReceiptHandle=receipt_handle)
	#Print most recent available IP address
	print('most recently available IP Address: ',message['Body'])

if __name__ == '__main__':
	main()
