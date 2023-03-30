def get_resource(requirements):
    print(requirements)
    """
    Returns a CloudFormation resource for an Elastic Load Balancer.
    """
    resource = {
        "Type": "AWS::ElasticLoadBalancing::LoadBalancer",
        "Properties": {
            "AvailabilityZones": requirements['availability_zones'],
            "Listeners": [
                {
                    "LoadBalancerPort": str(requirements['load_balancer']['port']),
                    "InstancePort": str(requirements['load_balancer']['instance_port']),
                    "Protocol": requirements['load_balancer']['protocol'].upper()
                }
            ],
            "HealthCheck": {
                "Target": requirements['load_balancer']['health_check_target'],
                "HealthyThreshold": str(requirements['load_balancer']['healthy_threshold']),
                "UnhealthyThreshold": str(requirements['load_balancer']['unhealthy_threshold']),
                "Interval": str(requirements['load_balancer']['health_check_interval']),
                "Timeout": str(requirements['load_balancer']['health_check_timeout'])
            }
        }
    }
    return resource
