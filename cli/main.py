from scanner.iam_scanner import get_iam_policies
from analyzer.rules_engine import analyze_policies
from analyzer.ai_analyzer import analyze_with_ai
from terraform.generator import generate_terraform
from analyzer.rules_engine import calculate_risk_score
from scanner.s3_scanner import get_s3_buckets

from analyzer.rules_engine import analyze_s3
import json

def main():
    print("Scanning IAM...")
    policies = get_iam_policies()

    print("Running IAM analysis...")
    findings = analyze_policies(policies)

    print("Scanning S3...")
    buckets = get_s3_buckets()


    print("Running S3 analysis...")
    s3_findings = analyze_s3(buckets)

    # Merge
    findings.extend(s3_findings)

    print("Findings:", findings)

    # AI must come AFTER merge
    print("Running AI analysis...")
    ai_output = analyze_with_ai(findings)
    print(ai_output)

    # Terraform LAST
    print("Generating Terraform fixes...")
    generate_terraform(findings)


    score = calculate_risk_score(findings)
    print(f"Overall Risk Score: {score}")

if __name__ == "__main__":
    main()