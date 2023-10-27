import boto3

def translate_text(text, source_language_code, target_language_code): # name the positional parameters
    client = boto3.client('translate')

     # replace the hard-coded parameters with positional arguments defined in the order of the parameters:
    response = client.translate_text(
        Text=text, 
        SourceLanguageCode=source_language_code, 
        TargetLanguageCode=target_language_code
    )
    print(response) 

# provide the value for the arguments when we call the function in the correct positional order.
def main():
    translate_text('I am learning to code in AWS','en','fr') 

if __name__=="__main__":
    main()