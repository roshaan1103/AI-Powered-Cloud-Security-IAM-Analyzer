
# Least Privilege Policy from CloudTrail
resource "aws_iam_policy" "least_privilege_policy" {
  name = "least_privilege_policy"

  policy = jsonencode({
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "*:ListPolicies",
        "*:ConsoleLogin",
        "*:GetAccountColor",
        "*:GetPolicyVersion",
        "*:ListEnrollmentStatuses",
        "*:ListDelegatedAdministrators",
        "*:ListManagedNotificationEvents",
        "*:GetAccountPlanState",
        "*:GetCostForecast",
        "*:GetCostAndUsage",
        "*:DescribeOrganization",
        "*:ListBuckets",
        "*:DescribeEventAggregates",
        "*:GetAccountInformation"
      ],
      "Resource": "*"
    }
  ]
})
}
