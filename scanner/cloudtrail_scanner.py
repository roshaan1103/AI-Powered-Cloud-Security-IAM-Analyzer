import boto3

def get_cloudtrail_events():
    client = boto3.client('cloudtrail')

    events = client.lookup_events(
        MaxResults=50
    )

    extracted = []

    for event in events['Events']:
        extracted.append({
            "event_name": event.get("EventName"),
            "username": event.get("Username"),
            "resources": event.get("Resources", [])
        })

    return extracted