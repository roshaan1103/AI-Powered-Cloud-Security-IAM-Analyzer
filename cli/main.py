from scanner.iam_scanner import get_iam_policies
from analyzer.rules_engine import analyze_policies
from analyzer.ai_analyzer import analyze_with_ai
from terraform.generator import generate_terraform
from analyzer.rules_engine import calculate_risk_score
from scanner.s3_scanner import get_s3_buckets
from scanner.cloudtrail_scanner import get_cloudtrail_events
from analyzer.least_privilege import generate_least_privilege
from terraform.generator import generate_least_privilege_policy
from analyzer.rules_engine import analyze_s3
from analyzer.attack_path import build_iam_graph, detect_attack_paths
from analyzer.policy_simulator import simulate_policy
import sys
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

    print("Analyzing CloudTrail for least privilege...")
    events = get_cloudtrail_events()

    actions = generate_least_privilege(events)

    print("Derived Actions:", actions)

    generate_least_privilege_policy(actions)

    print("Building IAM attack graph...")
    graph = build_iam_graph(policies)

    print("Detecting attack paths...")
    attack_findings = detect_attack_paths(graph)
    print("Attack Path Findings:", attack_findings)

    findings.extend(attack_findings)


    critical_exists = any(f["severity"] == "CRITICAL" for f in findings)

    if critical_exists:
        print("Critical issues found! Failing pipeline.")
        #sys.exit(1)



    print("Simulating IAM policy...")
    decision = simulate_policy(
        policy_arn="arn:aws:iam::149160851666:user/AI-Powered-Cloud-Security-IAM-Analyzer",
        action="s3:DeleteBucket"
    )

    print("Simulation result:", decision)

if __name__ == "__main__":
    main()