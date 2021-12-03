import json
import boto3  

REGION="us-east-1"
dynamodb = boto3.resource('dynamodb',region_name=REGION)
table = dynamodb.Table('PhotoGallery')

def lambda_handler(event, context):
    photoID=event['body-json']['PhotoID']
    creationtime=event['body-json']['CreationTime']
    
    table.delete_item(
    Key={                        
            "PhotoID": photoID,
            "CreationTime": creationtime
            #"ExifData": ExifData
        }
    )
                
    return {
        "statusCode": 200,
        "body": json.dumps(photoID)
    }
    
    
    
