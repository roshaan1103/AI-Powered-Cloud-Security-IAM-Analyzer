def analyze_policies(policies):
    findings = []

    for policy in policies:
        doc = policy["Document"]

        for statement in doc.get("Statement", []):
            actions = statement.get("Action", [])
            resources = statement.get("Resource", [])

            if isinstance(actions, str):
                actions = [actions]

            if isinstance(resources, str):
                resources = [resources]

            # Full admin
            if "*" in actions:
                findings.append({
                    "policy": policy["PolicyName"],
                    "issue": "Full admin access (*)",
                    "severity": "CRITICAL",
                    "affected_actions": actions,
                    "affected_resources": resources,
                    "recommendation": "Replace * with specific actions"
                })

            # Wildcard service
            for action in actions:
                if action.endswith(":*"):
                    findings.append({
                        "policy": policy["PolicyName"],
                        "issue": f"Wildcard service access ({action})",
                        "severity": "HIGH",
                        "affected_actions": actions,
                        "affected_resources": resources,
                        "recommendation": "Limit actions to required operations only"
                    })

    return findings


def analyze_s3(buckets):
    findings = []

    for bucket in buckets:

        if bucket["Public"]:
            findings.append({
                "type": "S3",
                "resource": bucket["Name"],
                "issue": "Public bucket access",
                "severity": "CRITICAL",
                "affected_actions": [],
                "affected_resources": [bucket["Name"]],
                "recommendation": "Block public access"
            })

        if not bucket["Encryption"]:
            findings.append({
                "type": "S3",
                "resource": bucket["Name"],
                "issue": "No encryption enabled",
                "severity": "HIGH",
                "affected_actions": [],
                "affected_resources": [bucket["Name"]],
                "recommendation": "Enable encryption"
            })

        if not bucket["Versioning"]:
            findings.append({
                "type": "S3",
                "resource": bucket["Name"],
                "issue": "Versioning not enabled",
                "severity": "MEDIUM",
                "affected_actions": [],
                "affected_resources": [bucket["Name"]],
                "recommendation": "Enable versioning"
            })

    return findings

def calculate_risk_score(findings):
    score_map = {
        "CRITICAL": 10,
        "HIGH": 7,
        "MEDIUM": 5,
        "LOW": 2
    }

    total_score = sum(score_map.get(f["severity"], 0) for f in findings)

    return total_score
