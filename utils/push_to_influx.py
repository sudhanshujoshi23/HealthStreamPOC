import json
import influxdb_client
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# InfluxDB settings
influxDB_config = {
    "bucket" : "health_data",
    "org" : "patients",
    "token" : "XXXXX",
    "url" : "http://localhost:8086/"
}

influx_host = influxDB_config['url']
influx_token = influxDB_config['token']
influx_org = influxDB_config['org']
influx_bucket = influxDB_config['bucket']

write_client = influxdb_client.InfluxDBClient(
            url=influx_host, 
            token=influx_token, 
            org=influx_org
            )

write_api = write_client.write_api(write_options=SYNCHRONOUS)

def write_data(health_record):
    data = json.loads(health_record['Data'].decode())
    point = (Point("health_metrics") \
        .tag("patient_id", str(data["patient_id"])) \
        .field("heart_rate", int(data["heart_rate"])) \
        .field("blood_pressure", str(data["blood_pressure"])) \
        .field("body_temperature", float(data["body_temperature"])) \
        .field("blood_SpO2", int(data["blood_SpO2"])) \
        # .time(data["time"], WritePrecision.NS)
    )
    try:
        write_api.write(bucket=influx_bucket, org=influx_org, record=point)
        print("Data successfully sent to Influx")
    except:
        print(f"Data could not be processed at InfluxDB.")
        print(health_record['Data'])
        # Need to think more about exception handling in case of failures

