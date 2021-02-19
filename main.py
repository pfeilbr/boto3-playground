import boto3
import json


def s3_client_example():
    client = boto3.client("s3")
    buckets = client.list_buckets()
    for bucket in buckets['Buckets']:
        print('Name: ' + bucket['Name'])


def s3_resource_example():
    s3 = boto3.resource('s3')
    for bucket in s3.buckets.all():
        print(bucket.name)


def dynamodb_client_example():
    db = boto3.client("dynamodb")
    tables_resp = db.list_tables()
    print(tables_resp['TableNames'])
    scan_resp = db.scan(TableName=tables_resp['TableNames'][0])
    print(scan_resp['Items'])

def glue_client_example():
    client = boto3.client('glue')
    databases_resp = client.get_databases()
    for database in databases_resp['DatabaseList']:
        database_name = database['Name']
        tables_resp = client.get_tables(DatabaseName=database_name)
        for table in tables_resp['TableList']:
            table_name = table['Name']
            table_resp = client.get_table(DatabaseName=database_name, Name=table_name)
            print(json.dumps(table_resp, indent=2, sort_keys=True, default=str))

def main():
    s3_client_example()
    s3_resource_example
    dynamodb_client_example()
    glue_client_example()


if __name__ == "__main__":
    main()
