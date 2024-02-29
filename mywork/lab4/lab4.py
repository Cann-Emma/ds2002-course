#!/c/Users/Emmanuella/AppData/Local/Microsoft/WindowsApps/python3


import boto3

s3= boto3.client('s3', region_name= 'us-east-1')
bucket_name='ds2002-zgb8ts'
object_name='minion.gif'
expires_in= 604800

response= s3.generate_presigned_url('get_object', 
Params={'Bucket':bucket_name,'Key':object_name},
ExpiresIn=expires_in)

print(response)
#Output: https://ds2002-zgb8ts.s3.amazonaws.com/minion.gif?AWSAccessKeyId=%16ASIAYS2NRLWOUZYWE6N4&Signature=Ps6vAhmgzV0WMdkvZADjBvtzCN8%3D&x-amz-security-token=FwoGZXIvYXdzEDQaDGtDIv5Zi71SQ1%2FOwyLEAUjszHa90YsURVHJLctZ%2Fq5%2FjnRMfvrim5KaamZtLNT9Ifk%2B7XlBCIY6qQncRhKgIA%2BNg94aITJ49PHyNePNZYNjQ5NK7PyK2qFm0J51w%2FxJLC20KPUc0ayQAw6UPxsS4MwJ%2FUrwj56KvHFLxrfN9TjQBQi4%2FuYZ233IqRPEQf%2BHlUB298oZjzAF2gIMmtViOJMhuHZTo%2FqDFbHBpsHBYGrmDjQL%2FXVdg35P6Tef4uNMh%2FY%2B7gd49ux%2FSFD%2B23jabjwlHqoolZKDrwYyLcgLeZ446K%2BpXjmopI3KLkCZYGO%2FujDg9IpDPWFmTXxg3Avze7WBwDpfAPKnRw%3D%3D&Expires=1709838892
