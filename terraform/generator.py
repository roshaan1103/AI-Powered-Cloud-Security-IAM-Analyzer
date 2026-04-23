import os
import json

OUTPUT_FILE = "outputs/fixes.tf"

def generate_terraform(findings):
    if not findings:
        print("No findings → no Terraform generated")
        return

    os.makedirs("outputs", exist_ok=True)

    tf_blocks = []

    for i, f in enumerate(findings):
        safe_actions = []

        # 🔥 Generate least-privilege fallback
        if "*" in f["affected_actions"]:
            safe_actions = ["s3:ListBucket"]  # minimal example
        else:
            safe_actions = f["affected_actions"]

        policy_doc = {
            "Version": "2012-10-17",
            "Statement": [{
                "Effect": "Allow",
                "Action": safe_actions,
                "Resource": f["affected_resources"]
            }]
        }

        block = f"""
# Fix for {f['policy']} - {f['issue']}
resource "aws_iam_policy" "fixed_policy_{i}" {{
  name = "fixed_policy_{i}"

  policy = jsonencode({json.dumps(policy_doc, indent=2)})
}}
"""
        tf_blocks.append(block)

    with open(OUTPUT_FILE, "w") as file:
        file.write("\n".join(tf_blocks))

    print(f"Terraform file generated at: {OUTPUT_FILE}")