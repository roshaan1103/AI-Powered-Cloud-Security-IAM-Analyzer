def build_iam_graph(policies):
    graph = []

    for policy in policies:
        for statement in policy["Document"].get("Statement", []):
            actions = statement.get("Action", [])
            resources = statement.get("Resource", [])

            if isinstance(actions, str):
                actions = [actions]
            if isinstance(resources, str):
                resources = [resources]

            for action in actions:
                for resource in resources:
                    graph.append({
                        "policy": policy["PolicyName"],
                        "action": action,
                        "resource": resource
                    })

    return graph

# Detecting dangerous patterns
def detect_attack_paths(graph):
    findings = []

    for edge in graph:
        action = edge["action"]

        # Privilege escalation patterns
        if "iam:PassRole" in action or "sts:AssumeRole" in action:
            findings.append({
                "type": "ATTACK_PATH",
                "issue": "Potential privilege escalation",
                "severity": "CRITICAL",
                "resource": edge["resource"],
                "recommendation": "Restrict role assumption permissions"
            })

        if action == "*" or action.endswith(":*"):
            findings.append({
                "type": "ATTACK_PATH",
                "issue": "Wildcard enables lateral movement",
                "severity": "HIGH",
                "resource": edge["resource"],
                "recommendation": "Limit actions"
            })

    return findings

