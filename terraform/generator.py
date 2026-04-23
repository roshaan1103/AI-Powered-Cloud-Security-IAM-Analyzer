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

        resource_name = f.get("resource", f"unknown_{i}")
        issue = f.get("issue", "unknown")

        # ================= IAM =================
        if f.get("type") == "IAM":

            actions = f.get("affected_actions", [])
            resources = f.get("affected_resources", ["*"])

            # fallback for unsafe actions
            if "*" in actions:
                actions = ["s3:ListBucket"]

            policy_doc = {
                "Version": "2012-10-17",
                "Statement": [{
                    "Effect": "Allow",
                    "Action": actions,
                    "Resource": resources
                }]
            }

            block = f"""
# Fix for IAM: {resource_name} - {issue}
resource "aws_iam_policy" "fixed_policy_{i}" {{
  name = "fixed_policy_{i}"

  policy = jsonencode({json.dumps(policy_doc, indent=2)})
}}
"""
            tf_blocks.append(block)

        # ================= S3 =================
        elif f.get("type") == "S3":

            if issue == "Public bucket access":
                block = f"""
# Fix for S3: {resource_name} - Public Access
resource "aws_s3_bucket_public_access_block" "block_{i}" {{
  bucket = "{resource_name}"

  block_public_acls   = true
  block_public_policy = true
}}
"""
                tf_blocks.append(block)

            elif issue == "No encryption enabled":
                block = f"""
# Fix for S3: {resource_name} - Encryption
resource "aws_s3_bucket_server_side_encryption_configuration" "enc_{i}" {{
  bucket = "{resource_name}"

  rule {{
    apply_server_side_encryption_by_default {{
      sse_algorithm = "AES256"
    }}
  }}
}}
"""
                tf_blocks.append(block)

            elif issue == "Versioning not enabled":
                block = f"""
# Fix for S3: {resource_name} - Versioning
resource "aws_s3_bucket_versioning" "ver_{i}" {{
  bucket = "{resource_name}"

  versioning_configuration {{
    status = "Enabled"
  }}
}}
"""
                tf_blocks.append(block)

    with open(OUTPUT_FILE, "w") as file:
        file.write("\n".join(tf_blocks))

    print(f"Terraform file generated at: {OUTPUT_FILE}")