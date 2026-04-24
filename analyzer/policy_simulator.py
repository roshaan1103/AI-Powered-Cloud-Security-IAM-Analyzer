import boto3

def simulate_policy(principal_arn, action, resource="*"):
    client = boto3.client('iam')

    response = client.simulate_principal_policy(
        PolicySourceArn=principal_arn,
        ActionNames=[action],
        ResourceArns=[resource]
    )

    decision = response['EvaluationResults'][0]['EvalDecision']

    return decision