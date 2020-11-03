#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pprint
import boto3

pp = pprint.PrettyPrinter(indent=4)

client = boto3.client("s3")
buckets = client.list_buckets()
    
for bucket in buckets['Buckets']:
    print('Name: ' + bucket['Name'])


# In[23]:



# pagination example
cwl = boto3.client("logs")

paginator = cwl.get_paginator('describe_log_groups')
page_iterator = paginator.paginate(logGroupNamePrefix="/aws",
PaginationConfig={
        'MaxItems': 10000,
        'PageSize': 20
    })

page_iterations_count=0
log_groups_count=0
for page in page_iterator:
    page_iterations_count+=1
    log_groups_count += len(page['logGroups'])

print(f"page_iterations_count: {page_iterations_count}, log_groups_count: {log_groups_count}")
    

