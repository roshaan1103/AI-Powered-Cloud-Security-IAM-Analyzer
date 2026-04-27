# 🔐 AI-Powered Cloud Security & IAM Analyzer

A DevSecOps platform that detects AWS misconfigurations, analyzes IAM risks, and generates automated Terraform remediation using AI-assisted insights.

---

## 🚨 Problem

Most cloud security breaches are caused by:
- Over-permissive IAM policies
- Publicly exposed S3 buckets
- Lack of least privilege enforcement

Traditional tools:
- Detect issues ❌
- But don’t fix them automatically ❌

---

## 💡 Solution

This project provides an **end-to-end cloud security pipeline**:

→ Scan cloud resources  
→ Detect vulnerabilities  
→ Analyze risks (AI-assisted)  
→ Generate Terraform fixes  
→ Validate policies  
→ Enforce security in CI/CD  

---

## 🚀 Features

### 🔍 IAM Security Analysis
- Detects wildcard permissions (`*`, `s3:*`)
- Identifies over-permissive policies
- Flags privilege escalation risks (`iam:PassRole`, `sts:AssumeRole`)

---

### 🪣 S3 Security Scanner
- Detects public bucket exposure
- Checks encryption status
- Verifies versioning configuration

---

### 🧠 AI-Powered Risk Analysis
- Uses local LLM (Ollama)
- Generates contextual explanations
- Suggests remediation strategies

---

### ⚙️ Terraform Auto-Remediation
- Converts findings into `.tf` files
- Applies least-privilege fixes
- Supports IAM + S3

---

### 📊 Risk Scoring Engine
- Assigns severity-based scores
- Prioritizes critical issues

---

### 🔗 Attack Path Detection
- Builds IAM relationship graph
- Detects privilege escalation paths
- Identifies lateral movement risks

---

### 📜 CloudTrail Least Privilege Engine
- Analyzes real API usage
- Generates minimal IAM policies

---

### 🧪 IAM Policy Simulation
- Validates permissions before deployment
- Uses AWS simulation APIs

---

### 🚦 CI/CD Security Gate
- Integrated with GitHub Actions
- Fails pipeline on critical issues
- Enables shift-left security

---

## 🏗️ Architecture Diagram

---
## 🛠️ Tech Stack
- Language: Python
- Cloud: AWS (IAM, S3, CloudTrail)
- IaC: Terraform
- AI: Ollama (Local LLM)
- CI/CD: GitHub Actions

---

## ▶️ How to Run Locally
### 1. Clone repo
```bash
git clone https://github.com/roshaan1103/AI-Powered-Cloud-Security-IAM-Analyzer.git

cd ai-cloud-security-analyzer
```

### 2. Install dependencies
```bash 
pip install -r requirements.txt
```

### 3. Configure AWS
```bash
aws configure
```

### 4. (Optional) Start Ollama
```bash 
ollama run mistral
```

### 5. Run scanner
```bash
python -m cli.main
```
---

## 🎯 Key Learnings
- Built a multi-service cloud security analysis pipeline
- Implemented least privilege using CloudTrail logs
- Modeled IAM attack paths for privilege escalation detection
- Integrated AI into DevSecOps workflows without relying on it for core logic
- Automated infrastructure remediation using Terraform