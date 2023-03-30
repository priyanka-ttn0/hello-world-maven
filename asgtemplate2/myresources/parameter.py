def get_resource():
    """
    Returns a CloudFormation resource for parameter we need for app version.
    """
    param={
        
        "AppVersion" : {
          "Type" : "String",
          "Description" : "Takes version of application"
        }
    }
    return param
    