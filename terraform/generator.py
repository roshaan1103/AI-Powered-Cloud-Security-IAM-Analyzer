import os

OUTPUT_FILE = "outputs/fixes.tf"

def generate_terraform(findings):
    if not findings:
        print("No findings → no Terraform generated")
        return

    os.makedirs("outputs", exist_ok=True)

    tf_blocks = []

    for i, f in enumerate(findings):
        if f["issue"] == "Full admin access":
            block = f"""
# Fix {i}
resource "aws_iam_policy" "restricted_policy_{i}" {{
  name = "restricted_policy_{i}"

  policy = jsonencode({{
    Version = "2012-10-17",
    Statement = [{{
      Effect = "Allow",
      Action = ["s3:ListBucket"],
      Resource = "*"
    }}]
  }})
}}
"""
            tf_blocks.append(block)

    with open(OUTPUT_FILE, "w") as file:
        file.write("\n".join(tf_blocks))

    print(f"Terraform file generated at: {OUTPUT_FILE}")