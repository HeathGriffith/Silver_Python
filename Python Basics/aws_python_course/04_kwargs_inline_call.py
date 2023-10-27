import boto3 

# **kwargs collects all keyword arguments into a dictionary 
def translate_text(**kwargs): 
#create client object to interact with AWS Translate service
	client = boto3.client('translate') 
# Unpacking the 'kwargs' dictionary to pass its key-value pairs as keyword arguments to 'client.translate_text'
	response = client.translate_text(**kwargs)
	print(response) 

def main(): 
# The order in which keyword arguments are passed doesn't matter because they're named. 
	translate_text(Text='I am learning to code in AWS', SourceLanguageCode='en', TargetLanguageCode='fr') 

if __name__ == "__main__": 
	main()