import json

def lambda_handler(event, context):
    name = event['name']
    message = f"Hello, {name}!"
    return {
      
    }
