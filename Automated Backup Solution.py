import boto3, os
from datetime import datetime


def back_up(source_file_name, source_file_loc='', bucket_name=""):  # add your aws s3 bucket name where the files will be uploaded.
    source_file = os.path.join(source_file_loc, source_file_name)
    today = datetime.now()
    formatted_date = today.strftime("%d/%m/%Y")
    formatted_time = today.strftime("%H:%M:%S")
    formatted_date_time = today.strftime("%Y-%m-%d_%H-%M-%S")

    if not os.path.exists(source_file):
        print("********************----Report-----***********************")
        print("Subject :: Failure                  ")
        print("Date : " + formatted_date)
        print("Time: " + formatted_time)
        return f"Error: Source file '{source_file_name}' not found at '{source_file}'"

    session = boto3.Session(aws_access_key_id="",
                             aws_secret_access_key="") # add acess key id and aws secret key from your aws account.

    s3_client = session.client('s3')

    dest_file_name = f"{formatted_date_time}_{source_file_name}"

    try:
        s3_client.upload_file(source_file, bucket_name, dest_file_name)  

        print("********************----Report-----***********************")
        print("Subject :: Successfull               ")
        print("Date : " + formatted_date)
        print("Time:  " + formatted_time)
        return f"Backup successful: '{source_file}' uploaded to S3 bucket '{bucket_name}' with filename '{dest_file_name}'"
    except Exception as e:
        print("********************----Report-----***********************")
        print("Subject :: Failure                  ")
        print("Date : " + formatted_date)
        print("Time:  " + formatted_time)
        return f"Error during backup: {e}"


source_file_name = "" #source file name
source_file_loc = r"" # source file locarion
result = back_up(source_file_name, source_file_loc=source_file_loc)
print(result)
