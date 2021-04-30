""" 
Python Script to get Rubrik Oracle database ID
change the cluster and api_token
"""

import rubrik_cdm
import urllib3

# Disable certificate warnings and connect to Rubrik Cluster
urllib3.disable_warnings()

# Parameters used in the script
# set the cluster and token you would like to use 
cluster = "[YOUR CLUSTERNAME]"
api_token = "[YOUR TOKEN]"

# connect to the cluster
rubrik=rubrik_cdm.Connect(cluster, api_token=api_token)

# Provide input of database name and host name where database is located
print('What is the database name: ')
object_name = input()
# Object type is oracle database
object_type = 'oracle_db'
print(f'What is the host where {object_name} is located? ')
hostname = input()
#find Oracle ID
oracle_id = rubrik.object_id(object_name, object_type, hostname=hostname)

print(f'Oracle ID of database {object_name} is {oracle_id}')