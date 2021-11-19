import argparse
import os
import sys
import boto3


def main(args):
    try:
        access_key = os.environ["AWS_ACCESS_KEY"]
        secret_key = os.environ["AWS_SECRET_ACCESS_KEY"]
    except Exception as ex:
        print("Failed to retrieve the keys.")
        sys.exit()

    try:
        session = boto3.Session(
            aws_access_key_id=access_key, aws_secret_access_key=secret_key
        )
        s3 = session.resource("s3")
        s3.meta.client.upload_file(
            Filename=args.data_path, Bucket=args.bucket_name, Key="uploaded_data.csv"
        )
    except FileNotFoundError:
        print("File not found")
        sys.exit()
    except Exception as err:
        print("Failed to upload file, reason", err)
        sys.exit()


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Script for uploading a file to the S3"
    )
    parser.add_argument(
        "-p",
        "--data_path",
        type=str,
        required=True,
        help="Path for the data to be uploaded to S3",
    )
    parser.add_argument(
        "-bn",
        "--bucket_name",
        type=str,
        required=True,
        help="Name of the S3 bucket",
    )
    return parser.parse_args()


if __name__ == "__main__":
    main(parse_arguments())
