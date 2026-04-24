def generate_least_privilege(events):
    actions = set()

    for event in events:
        if event["event_name"]:
            actions.add(event["event_name"])

    # Convert to IAM-style actions
    iam_actions = []

    for action in actions:
        # Example mapping (simplified)
        iam_actions.append(f"*:{action}")

    return list(iam_actions)