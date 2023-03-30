def get_resource(requirements):
    """
    Returns a CloudFormation resource for an Auto Scaling Group.
    """
    resource = {
        "Type": "AWS::AutoScaling::AutoScalingGroup",
        "Properties": {
        "AvailabilityZones": requirements['availability_zones'],
        "MinSize": str(requirements['min_size']),
        "MaxSize": str(requirements['max_size']),
        "DesiredCapacity": str(requirements['desired_capacity']),
        "LaunchTemplate": {
          "LaunchTemplateId": { "Ref": "MyLaunchTemplate" },
          "Version": { "Fn::GetAtt": [ "MyLaunchTemplate", "LatestVersionNumber" ] }
        }
      }
    }
    return resource


def get_launch_configuration(requirements):
    """
    Returns a CloudFormation resource for a Launch Configuration.
    """
    resource = {
        "Type": "AWS::EC2::LaunchTemplate",
        "Properties": {
            "LaunchTemplateName":requirements["launchtemplatename"],
            "LaunchTemplateData":{
            "IamInstanceProfile":{
            "Arn":requirements["roleArn"]
            },
            "DisableApiTermination":requirements['DisableApiTermination'],
            "ImageId": requirements['ami_id'],
            "InstanceType": requirements['instance_type'],
            "KeyName": requirements['key_name'],
            "SecurityGroupIds":[
              "sg-018bf2f99e74da536"
            ],      
            "UserData": {"Fn::Base64": requirements['user_data']}
            }
        }
    }

    return resource
