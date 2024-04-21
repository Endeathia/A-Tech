import boto3
import json
secrets_manager_client = boto3.client('secretsmanager', region_name='us-west-1')
secret_name = 'TELEGRAM_TOKEN'
response = secrets_manager_client.get_secret_value(SecretId=secret_name)
secret_string = response['SecretString']
secret_dict = json.loads(secret_string)
TELEGRAM_TOKEN = secret_dict['TELEGRAM_TOKEN']
print(TELEGRAM_TOKEN)