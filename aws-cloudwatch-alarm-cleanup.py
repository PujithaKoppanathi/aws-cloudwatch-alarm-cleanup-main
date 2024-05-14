#!/usr/bin/env python3

import boto3

cloudwatch = boto3.client('cloudwatch', region_name = 'us-east-1')
ec2 = boto3.client('ec2', region_name = 'us-east-1')

responseCW = cloudwatch.describe_alarms(
    AlarmNamePrefix='EC2-SystemHealthCheck-Terminate'
)

responseEC2 = ec2.describe_instances(
    Filters=[
        {
            'Name': 'instance-state-name',
            'Values': ['running', 'pending', 'stopped'
            ]
        }
    ]
)

counterEC2 = len(responseEC2['Reservations'])
ec2List = []
while counterEC2 > 0:
    ec2List.append(responseEC2['Reservations'][counterEC2-1]['Instances'][0]['InstanceId'])
    counterEC2 -= 1

counter = len(responseCW['MetricAlarms'])
alarmDict={}
while counter > 0:
    alarmDict[(responseCW['MetricAlarms'][counter-1]['Dimensions'][0]['Value'])]=(responseCW['MetricAlarms'][counter-1]['AlarmName'])
    counter -= 1

inactiveEC2List = []
for i in (list(alarmDict.keys())):
    if i not in ec2List:
        inactiveEC2List.append(i)

inactiveEC2List = set(inactiveEC2List)

deleteList = []
for i in list(inactiveEC2List):
    deleteList.append(alarmDict[i])

responseDeleteArms = cloudwatch.delete_alarms(
    AlarmNames=deleteList
)

print(responseDeleteArms['ResponseMetadata']['HTTPStatusCode'])
