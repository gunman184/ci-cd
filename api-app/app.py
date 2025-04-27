import json
import boto3
from botocore.exceptions import ClientError

# DynamoDB client
dynamodb = boto3.client('dynamodb')

# Table name
table_name = 'WebsiteVisits'
def lambda_handler(event, context):
    try:
        #http_method = event['requestContext']['http']['method']
        http_method = event['httpMethod']
        
        if http_method == 'POST':
            # Increment visit count
            response = dynamodb.update_item(
                TableName=table_name,
                Key={'id': {'S': 'website_visits'}},
                UpdateExpression="SET visits = if_not_exists(visits, :start) + :incr",
                ExpressionAttributeValues={
                    ':incr': {'N': '1'},
                    ':start': {'N': '0'}
                },
                ReturnValues="UPDATED_NEW"
            )
            
            return {
                'statusCode': 200,
                'body': json.dumps({
                    'message': 'Visit count updated successfully :)',
                    'visit_count': int(response['Attributes']['visits']['N'])
                })
            }

        elif http_method == 'GET':
            # Retrieve visit count
            response = dynamodb.get_item(
                TableName=table_name,
                Key={'id': {'S': 'website_visits'}}
            )
            
            if 'Item' in response:
                visit_count = int(response['Item']['visits']['N'])
                return {
                    'statusCode': 200,
                    'body': json.dumps({'visit_count': visit_count})
                }
            else:
                return {
                    'statusCode': 404,
                    'body': json.dumps({'message': 'Visit count not found'})
                }
        
        else:
            return {
                'statusCode': 405,
                'body': json.dumps({'message': 'Method not allowed'})
            }

    except ClientError as e:
        # Log error and return it
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Internal Server Error :3', 'error': str(e)})
        }
    except Exception as e:
        # Log general error
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Internal Server Error', 'error': str(e)})
        }
