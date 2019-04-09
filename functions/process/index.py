import json

from module.utils import logger
from module.utils import process


def handler(event, _context):
    if event.get('ramuda_action') == 'ping':
        return 'alive'

    logger.log('Received event: %s', json.dumps(event, indent=2))

    s3_event = json.loads(event['Records'][0]['body'])
    bucket = s3_event['Records'][0]['s3']['bucket']['name']
    key = s3_event['Records'][0]['s3']['object']['key']

    return process(file, bucket)
