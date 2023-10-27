import boto3

def translate_text(**kwargs): 

#initializing the variables makes API calls to what they hold and stores the results. 
    client = boto3.client('translate')
    response = client.translate_text(**kwargs)
    print(response) 

# The only change is below this line #

kwargs={
    "Text":"I am learning to code in AWS",
    "SourceLanguageCode":"en",
    "TargetLanguageCode":"fr"
    }

def main():
    translate_text(**kwargs)

if __name__=="__main__":
    main()