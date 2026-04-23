def analyze_policies(policies):
    findings = []

    for policy in policies:
        doc = policy["Document"]

        for statement in doc.get("Statement", []):
            actions = statement.get("Action", [])
            resources = statement.get("Resource", [])

            # Normalize to list
            if isinstance(actions, str):
                actions = [actions]

            if isinstance(resources, str):
                resources = [resources]

            # 🔥 Rule 1: Full admin access
            if "*" in actions:
                findings.append({
                    "policy": policy["PolicyName"],
                    "issue": "Full admin access (*)",
                    "severity": "CRITICAL"
                })

            # 🔥 Rule 2: Wildcard service access (e.g., s3:*)
            for action in actions:
                if action.endswith(":*"):
                    findings.append({
                        "policy": policy["PolicyName"],
                        "issue": f"Wildcard service access ({action})",
                        "severity": "HIGH"
                    })

            # 🔥 Rule 3: Resource wildcard
            if "*" in resources:
                findings.append({
                    "policy": policy["PolicyName"],
                    "issue": "Resource wildcard (*)",
                    "severity": "MEDIUM"
                })

    return findings