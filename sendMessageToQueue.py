import boto3

#Function to send message to an existing queue
def send_message_to_queue(messageGID,MessageDId,queue_url,message_body):
	#Create SQS client
	sqs_client = boto3.client('sqs', region_name='us-east-2')                   	
	response=sqs_client.send_message(MessageGroupId=messageGID,MessageDeduplicationId=MessageDId,QueueUrl=queue_url,MessageBody=message_body)
	return response

#Main function
def main():
	queue_url="" #provide queue_url
	message_body='192.23.20.01'
	messageGrpID='Group1'
	MessageDId='1'
	message = send_message_to_queue(messageGrpID,MessageDId,queue_url, message_body)
	print('Message sent')

if __name__ == '__main__':
	main()
