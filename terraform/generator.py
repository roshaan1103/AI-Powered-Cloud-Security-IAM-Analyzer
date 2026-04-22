def generate_terraform(findings):
    tf_code = ""

    for f in findings:
        if f["issue"] == "Full admin access":
            tf_code += """
# Restrict IAM policy
resource "aws_iam_policy" "restricted_policy" {
  name = "restricted_policy"

  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [{
      Effect = "Allow",
      Action = ["s3:ListBucket"],
      Resource = "*"
    }]
  })
}
"""

    with open("outputs/fixes.tf", "w") as f:
        f.write(tf_code)