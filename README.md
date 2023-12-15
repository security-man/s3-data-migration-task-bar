# s3-data-migration-task-bar
A simple and unelegant python script to poll S3 data using AWS profiles with AWS SDK to produce a status bar to assist data migration operations.

# Installation
Simply clone the repo and execute the python script!

# Inputs
The script will take 3 fields of user input:

1) AWS profile name (this input requires a correctly-configure AWS CLI using profiles, configured within the .aws/config file)

	    Enter AWS IAM profile name from local .aws/config file: 

Simply enter the profile name for the AWS account in question, as listed in .aws/config file

2) AWS S3 bucket name. Fairly self-explanatory

	    Enter bucket name: 

3) Total number of objects expected. The script will continue to execute until the bucket in question contains this many objects, so be careful not to overstate this value, or else you will be waiting in an infinite loop!

	    Enter total final objects expected: 

# Outputs
Once the script executes, you'll be presented with a helpful progress bar. The progress bar updates as quickly as it can and this frequency is dictated by how many objects the bucket contains at the time of polling. Expect ~ 1 minute frequency updates for a bucket containing 100,000 objects!

Once the progress bar reaches 100%, the script finishes. 

Excellent!
