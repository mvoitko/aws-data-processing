import json

from module.utils import logger
from module.partition import partition

def handler(event, _context):

    logger.log('Received event: %s', json.dumps(event, indent=2))

    s3_event = json.loads(event['Records'][0]['body'])
    bucket = s3_event['Records'][0]['s3']['bucket']['name']
    file = s3_event['Records'][0]['s3']['object']['key']

    return partition(file, bucket)
