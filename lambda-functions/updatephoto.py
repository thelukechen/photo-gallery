import json
import boto3  

REGION="us-east-1"
dynamodb = boto3.resource('dynamodb',region_name=REGION)
table = dynamodb.Table('PhotoGallery')

def lambda_handler(event, context):
    photoID=event['body-json']['PhotoID']
    creationtime=event['body-json']['CreationTime']
    title=event['body-json']['title']
    description=event['body-json']['description']
    tags=event['body-json']['tags']
    
    table.update_item(
    Key={                        
            "PhotoID": photoID,
            "CreationTime": creationtime,
        },
        UpdateExpression="set Title=:t, Description=:d, Tags=:a",
        ExpressionAttributeValues={
            ':t': title,
            ':d': description,
            ':a': tags
        },
        ReturnValues="UPDATED_NEW"
    )
                
    return {
        "statusCode": 200,
        "body": json.dumps(photoID)
    }
    
    
    
