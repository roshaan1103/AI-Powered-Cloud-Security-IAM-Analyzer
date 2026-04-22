from scanner.iam_scanner import get_iam_policies
from analyzer.rules_engine import analyze_policies
from analyzer.ai_analyzer import analyze_with_ai
from terraform.generator import generate_terraform
import json

def main():
    print("Scanning IAM...")
    policies = get_iam_policies()

    print("Running analysis...")
    findings = analyze_policies(policies)

    with open("outputs/findings.json", "w") as f:
        json.dump(findings, f, indent=2)

    print("Running AI analysis...")
    ai_output = analyze_with_ai(findings)
    print(ai_output)

    print("Generating Terraform fixes...")
    generate_terraform(findings)

if __name__ == "__main__":
    main()