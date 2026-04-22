def analyze_policies(policies):
    findings = []

    for policy in policies:
        doc = policy["Document"]

        for statement in doc.get("Statement", []):
            actions = statement.get("Action", [])
            resources = statement.get("Resource", [])

            if actions == "*" or "*:*" in actions:
                findings.append({
                    "policy": policy["PolicyName"],
                    "issue": "Full admin access",
                    "severity": "HIGH"
                })

    return findings