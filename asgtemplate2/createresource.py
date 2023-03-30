import json
import yaml
from myresources import autoscalinggroup, loadbalancer,parameter
import sys

# Load requirements from YAML file
with open('asgtemplate2/autoscaling_requirements.yaml', 'r') as f:
    requirements = yaml.safe_load(f)
    print(requirements)
# Define CloudFormation template structure
# template = {
#     "Parameters" : parameter.get_resource(),
#     "Resources": {
#         "MyAutoScalingGroup": autoscalinggroup.get_resource(requirements),
#         "MyLaunchTemplate": autoscalinggroup.get_launch_configuration(requirements)
#     }
# }

template = {
    "Parameters" : sys.argv[1],
    "Resources": {
        "MyAutoScalingGroup": autoscalinggroup.get_resource(requirements),
        "MyLaunchTemplate": autoscalinggroup.get_launch_configuration(requirements)
    }
}

print(template)
# Add Elastic Load Balancer resource and update launch configuration
if requirements.get('load_balancer', {}).get('enabled', False):
    elb_resource = loadbalancer.get_resource(requirements)
    print(elb_resource)
    template['Resources']['ElasticLoadBalancer'] = elb_resource
    template['Resources']['MyLaunchTemplate']['Properties']['LoadBalancerNames'] = [{"Ref": "ElasticLoadBalancer"}]

# Save CloudFormation template as JSON file
with open('asgtemplate2/autoscaling_template.json', 'w') as f:
    json.dump(template, f)

# Output success message
print("CloudFormation template generated and saved as autoscaling_template.json")


