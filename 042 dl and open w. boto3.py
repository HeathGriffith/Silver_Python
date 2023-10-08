import boto3

s3 = boto3.client('s3')

# Specify your directory path
directory_path = "C:\\Users\\heath\\OneDrive\\Documents\\VSCode\\Python Learning\\LUIT\\Silver_Files"

# Join the directory path with the original filename
file_path = directory_path + "\\test_text_upload.txt"

s3.download_file('hgriffith-boto3-10052023', 'test_text_upload.txt', file_path)
