import boto3

import pandas as pd


s3_client = boto3.client('s3')


def partition(input_filepath: str, bucket: str):
    """Partition dataset based on the EC.SERIESQUOT.UNT column

    :param input_filepath: str
    :param bucket: str
    """
    df: pd.DataFrame = pd.read_csv(f'{bucket}/processed/Mon.csv')

    # Partition dataset based on the EC.SERIESQUOT.UNT column
    df_by_ec_seriesquot_unt: pd.DataFrame = df.groupby(by='EC.SERIESQUOT.UNT')
    for name, group in df_by_ec_seriesquot_unt:
        group.to_csv(name)
        s3_client.upload_file(name, bucket, f'partitioned/{name}')

