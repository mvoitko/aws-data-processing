import boto3

import pandas as pd


s3_client = boto3.client('s3')


def preprocess_xlsx_files(input_filepath: str, output_bucket: str):
    """Save each sheets from xlsx file into separate csv file.
    Upload files to AWS S3 with `preprocessed` prefix.

    :param input_filepath: str
    :param bucket: str
    """
    pd.read_from_url(input_filepath)
    sheets = pd.ExcelFile(input_filepath)

    for name, sheet in sheets.items():
        sheet_df = pd.DataFrame(sheet)
        sheet_df.to_csv(name)
        s3_client.upload_file(name, output_bucket, f'preprocessed/{name}')
