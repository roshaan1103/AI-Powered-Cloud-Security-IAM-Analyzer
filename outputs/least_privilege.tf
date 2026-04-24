
# Least Privilege Policy from CloudTrail
resource "aws_iam_policy" "least_privilege_policy" {
  name = "least_privilege_policy"

  policy = jsonencode({
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "*:GetAccountPlanState",
        "*:ListDelegatedAdministrators",
        "*:DescribeOrganization",
        "*:GetCostAndUsage",
        "*:GetPolicyVersion",
        "*:GetAccountInformation",
        "*:ListEnrollmentStatuses",
        "*:ListBuckets",
        "*:LookupEvents",
        "*:DescribeEventAggregates",
        "*:GetCostForecast",
        "*:ListPolicies",
        "*:ListManagedNotificationEvents",
        "*:GetAccountColor",
        "*:ConsoleLogin"
      ],
      "Resource": "*"
    }
  ]
})
}
