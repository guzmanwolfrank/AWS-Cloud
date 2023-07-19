import boto3

# Get the AWS CLI configuration
config = boto3.config.Config(region_name="us-east-1")

# Create an EC2 client
ec2 = boto3.client("ec2", config=config)

# Get the VPC ID and subnet ID
vpc_id = ec2.describe_vpcs()["Vpcs"][0]["VpcId"]
subnet_id = ec2.describe_subnets(Filters=[{"Name": "Name", "Values": ["default"]}])[
    "Subnets"
][0]["SubnetId"]

# Get the AMI ID
ami_id = "ami-0123456789abcdef0"

# Create a security group
security_group_name = "my-security-group"
security_group_description = "A security group for my website"
ec2.create_security_group(GroupName=security_group_name, Description=security_group_description)

# Open ports 80 and 443 in the security group
ec2.authorize_security_group_ingress(
    GroupId=security_group_name,
    IpPermissions=[
        {
            "IpProtocol": "tcp",
            "FromPort": 80,
            "ToPort": 80,
            "IpRanges": [{"CidrIp": "0.0.0.0/0"}],
        },
        {
            "IpProtocol": "tcp",
            "FromPort": 443,
            "ToPort": 443,
            "IpRanges": [{"CidrIp": "0.0.0.0/0"}],
        },
    ],
)

# Create an SSH key pair
key_pair_name = "my-key-pair"
ec2.create_key_pair(KeyName=key_pair_name)

# Upload the website files
website_files = ["index.html", "style.css"]
with open("/tmp/website.zip", "w") as zipfile:
    for file in website_files:
        zipfile.write(file)

# Create an EC2 instance
instance_type = "t2.micro"
instance_count = 1
ec2.run_instances(
    ImageId=ami_id,
    MinCount=instance_count,
    MaxCount=instance_count,
    InstanceType=instance_type,
    KeyName=key_pair_name,
    VpcSubnetIds=[subnet_id],
    SecurityGroupIds=[security_group_name],
)

# Get the instance ID
instance_id = ec2.describe_instances()["Reservations"][0]["Instances"][0]["InstanceId"]

# Upload the website to the instance
ec2.upload_file(
    Filename="/tmp/website.zip",
    LocalPath=None,
    Dest="/home/ec2-user/website.zip",
    InstanceId=instance_id,
)

# Unzip the website files on the instance
ec2.run_command(
    Command=["unzip", "-q", "/home/ec2-user/website.zip"], InstanceId=instance_id
)

# Open a browser to the website
url = "http://" + ec2.describe_instances()["Reservations"][0]["Instances"][0]["PublicIpAddress"]
print("Your website is now live at: " + url)
