from django.shortcuts import render
import sys
import subprocess
import boto3
import json

region = 'eu-central-1'
ec2 = boto3.client('ec2', region_name=region)
# ec2_client = boto3.client('ec2')
# ec2_resource = boto3.resource('ec2')

# Get instance ID from metadata
def getInstanceId():
    cmd = ["curl", "http://169.254.169.254/latest/meta-data/instance-id"]
    instanceId, stderr = subprocess.Popen(cmd, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    return instanceId

# Get instance tag
def getInstanceTag(request):

    instance=ec2.instance(getInstanceId())
    response=instance.tags
  
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }
 
# Shutdown EC2 Instance
def shutdownInstance(request):
    instance_id = getInstanceId()

    print("STOPping your instance: " + str(instance_id))
    ec2.stop_instances(InstanceIds=instance_id)
    response = "Successfully stopped instances: " + str(instance_id)
        
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }
                                   
"""
# Shutdown EC2 Instance
def shutdownInstance(request):
    cmd = ["sudo", "shutdown", "+1"]
    stdout, stderr = subprocess.Popen(cmd, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        
    return {
        'statusCode': 200,
        'body': json.dumps("shutting down EC2 Instance")
    }
 """