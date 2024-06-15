import boto3
import json
import time
import push_to_influx

# Read Data from Kinesis Stream
kinesis = boto3.client('kinesis', region_name='ap-south-1')
stream_name = "health-data-stream"

def read_from_kinesis():
    response = kinesis.describe_stream(StreamName=stream_name)
    shard_id = response['StreamDescription']['Shards'][0]['ShardId']

    shard_iterator = kinesis.get_shard_iterator(
        StreamName=stream_name,
        ShardId=shard_id,
        ShardIteratorType='LATEST'
    )['ShardIterator']

    while True:
        records_resp = kinesis.get_records(ShardIterator=shard_iterator, Limit=100)
        records = records_resp['Records']
        for record in records:
            print(record)
            # push_to_influx.write_data(record)
        
        shard_iterator = records_resp['NextShardIterator']
        time.sleep(5)

if __name__ == "__main__":
    read_from_kinesis()