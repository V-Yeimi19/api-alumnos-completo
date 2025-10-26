import boto3
from boto3.dynamodb.conditions import Key

def lambda_handler(event, context):
    # Entrada (json)
    tenant_id = event['body']['tenant_id']
    alumno_id = event['body']['alumno_id']
    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('t_alumnos')
    response = table.get_item(
        Key={
            'tenant_id': tenant_id,
            'alumno_id': alumno_id
        }
    )
    item = response.get('Item')
    # Salida (json)
    if item:
        return {
            'statusCode': 200,
            'alumno': item
        }
    else:
        return {
            'statusCode': 404,
            'message': 'Alumno no encontrado'
        }
