# aws-cloudwatch-alarm-cleanup
Perform cleanup of unused system health check alarms for terminated instances when such alarms are created as a trigger for perfoming a function within AWS.

#### Description

System health check alarms in AWS may be used to perform a triggered action based on instance health status, such a when a host becomes degraded, users may want the instance to terminate immediately. When such alarms are created using automation such as Cloud-Init scripts during instance start-up processes, the alarm will remain orphaned upon instance termination. This tool may be executed as a Lamda function to perform cleanups based on a pre-defined schedule such as once per week.

#### Intended Audience
* Devops

#### Pre-requisited
* Python v3.7.5 or greater
* Cloud Watch alarm names must match the pre-defined prefix, *EC2-SystemHealthCheck-Terminate* or, must be changed within the script for custom prefixes.

#### Usage
Specfiy the script with the correct version of Python. The script may be updated to accomodate different regions (currently set to us-east-1). The session in which the script is executed must be authenticated to the target AWS account or used within a Lambda function.

* aws-cloudwatch-alarm-cleanup.py

#### Examples

* Execute the script manually via an authenticated session
  * `aws-cloudwatch-alarm-cleanup.py` 
