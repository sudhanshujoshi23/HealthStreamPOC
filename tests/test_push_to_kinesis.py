import boto3
from moto import mock_aws
import json
import time
from utils.generate_health_data import simulate_health_data

@mock_aws
def test_push_vitals():
    
    # setup kinesis stream
    kinesis = boto3.client('kinesis', region_name='ap-south-1')
    stream_name = "health_data_stream"
    kinesis.create_stream(StreamName=stream_name, ShardCount=1)
    time.sleep(10)

    patient_id = "ch10001"
    data = simulate_health_data(patient_id)
    response = kinesis.put_record(
        StreamName = stream_name,
        Data = json.dumps(data),
        PartitionKey = "pid"
    )

    assert response['ResponseMetadata']['HTTPStatusCode'] == 200



