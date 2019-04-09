import json

from module.utils import logger
from module.preprocess import preprocess_xlsx_files


def handler(event, _context):

    logger.log('Received event: %s', json.dumps(event, indent=2))

    s3_event = json.loads(event['Records'][0]['body'])
    bucket = s3_event['Records'][0]['s3']['bucket']['name']
    file = s3_event['Records'][0]['s3']['object']['key']

    return preprocess_xlsx_files(file, bucket)
