import random
import json
import time
import boto3
from generate_health_data import simulate_health_data

kinesis = boto3.client('kinesis', region_name='ap-south-1')
stream_name = "health-data-stream"
patient_ids = ['ch-1000', 'ch-1001', 'ch-1002']

def push_vitals():
    # pick a random patient id
    patient_id = random.choice(patient_ids)

    # generate health data payload to be sent to kinesis
    payload = simulate_health_data(patient_id)

    print(payload)

    # send to kinesis and get a response
    response = kinesis.put_record(
        StreamName = stream_name,
        Data = json.dumps(payload),
        PartitionKey = "pid"
    )

    print("Data sent to Kinesis:", response['SequenceNumber'])
    time.sleep(5)
    

if __name__ == "__main__":
    push_vitals()