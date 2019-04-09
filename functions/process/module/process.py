from datetime import datetime

import boto3
import pandas as pd


s3_client = boto3.client('s3')


def process_files(input_filepath: str, bucket: str):
    """Process CSV file.
    Construct a final file for the data with the same frequency

    :param input_filepath: str
    :param bucket: str
    """
    monthly_df: pd.DataFrame = pd.read_csv(f'{bucket}/preprocessed/Mon.csv')
    quarter_df: pd.DataFrame = pd.read_csv(f'{bucket}/preprocessed/Quarter.csv')

    quarter_df['Name'] = f'{int(quarter_df["Name"][1:2])*3}/15/{quarter_df["Name"][-2:]}'

    united_df: pd.DataFrame = monthly_df.merge(quarter_df)
    united_df.fillna(method='ffill', inplace=True)
    timestamp = str(datetime.now().strftime('%m/%d/%Y %H:%M:%S'))
    united_df.to_csv(timestamp)
    s3_client.upload_file(timestamp, bucket, f'processed/{timestamp}')
