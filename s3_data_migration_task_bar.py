import boto3
import botocore
import time

# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()

# Input IAM profile to access bucket
profile_name = input('Enter AWS IAM profile name from local .aws/config file: ')
# Input bucket name
bucket_name = input('Enter bucket name: ')
# A List of Items
total_objects = int(input('Enter total final objects expected: '))

# Initial call to print 0% progress
printProgressBar(0, total_objects, prefix = 'Progress:', suffix = 'Complete', length = 50)

# Configure boto3 session details to retrieve S3 object details
session = boto3.Session(profile_name=profile_name)
s3_client = session.client('s3')
s3_resource = session.resource('s3')
s3_bucket = s3_resource.Bucket(bucket_name)

# Initial count for summing total objects currently present in bucket
interim_count = 0
# Loop until bucket is deemed 'full'
while interim_count <= total_objects:
    try:
        # Count current objects
        interim_count = sum([page['KeyCount'] for page in s3_client.get_paginator('list_objects_v2').paginate(Bucket=bucket_name)])
    
    # Exception handling
    except botocore.exceptions.ParamValidationError as error:
        raise ValueError('The parameters you provided are incorrect: {}'.format(error))

    # Update progress bar
    printProgressBar(interim_count, total_objects, prefix = 'Progress:', suffix = 'Complete', length = 50)

# Once finished, print ascii art to console! 
final_display = open ('final_display.txt','r')
print('')
print(''.join([line for line in final_display]))