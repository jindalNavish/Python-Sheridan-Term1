cat create_ec2.py 
import boto3
# variables
image='ami-026b57f3c383c2eec'
subnet='subnet-08edbb5de9da54fe4'
security_group='sg-00f5d76eac030dad0'
vm_name='VM-test-name'
user_data='''
#!/bin/bash
yum install httpd -y
var=$(curl -s http://169.254.169.254/latest/meta-data/placement/availability-zone)
echo "<html><body><h1> Hello from $(hostname -f) in $var </h1></body></html>" > /var/www/html/index.html
systemctl restart httpd
systemctl enable httpd
'''
target = boto3.client('ec2')
instance = target.run_instances(
    ImageId=image,
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
    KeyName='demokey',
    SubnetId=subnet,
    SecurityGroupIds=[security_group],
    UserData=user_data,
    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name','Value':vm_name}]}]
)