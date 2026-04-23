from scanner.iam_scanner import get_iam_policies
from analyzer.rules_engine import analyze_policies
from analyzer.ai_analyzer import analyze_with_ai
from terraform.generator import generate_terraform
from analyzer.rules_engine import calculate_risk_score
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
    print("Findings:", findings)
    generate_terraform(findings)

    score = calculate_risk_score(findings)
    print(f"Overall Risk Score: {score}")

if __name__ == "__main__":
    main()