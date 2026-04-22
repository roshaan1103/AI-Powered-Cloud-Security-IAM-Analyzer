import boto3
import json


def get_iam_policies():
    client = boto3.client('iam')

    policies = []
    response = client.list_policies(Scope='Local')

    for policy in response['Policies']:
        policy_version = client.get_policy_version(
            PolicyArn=policy['Arn'],
            VersionId=policy['DefaultVersionId']
        )

        policies.append({
            "PolicyName": policy['PolicyName'],
            "Document": policy_version['PolicyVersion']['Document']
        })

    return policies


if __name__ == "__main__":
    data = get_iam_policies()
    print(json.dumps(data, indent=2))