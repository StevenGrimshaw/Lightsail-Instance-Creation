import boto3, uuid
from decouple import config

client = boto3.client(
    'lightsail', 
    region_name='us-east-2',
    aws_access_key_id=config('access_key',default=''), 
    aws_secret_access_key=config('secret_key',default=''))

NUM_INSTANCES = 0
while True:
    inp = input("Enter the number of instances you would like to create: ")
    if not inp.isdigit() or int(inp) <= 0:
        print("ERROR: Input must be a positive integer")
        continue
    NUM_INSTANCES = int(inp)
    break

for i in range(0, NUM_INSTANCES):
    INSTANCE_NAME = 'GeneratedVPC-' + str(uuid.uuid4())
    client.create_instances_from_snapshot(
        instanceNames=[
            INSTANCE_NAME,
        ],
        availabilityZone='us-east-2a',
        instanceSnapshotName='syslink-Windows_Server_2019-1-1663276007',
        bundleId='nano_win_2_0'
    )
    print("Generated VPC (%s): %s" % ((i + 1), INSTANCE_NAME))
