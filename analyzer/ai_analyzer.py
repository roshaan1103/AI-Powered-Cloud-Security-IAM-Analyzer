import requests

def analyze_with_ai(findings):
    try:
        prompt = f"""
You are a cloud security expert.

Analyze these findings:
{findings}

Instructions:
- Prioritize CRITICAL issues first
- Explain risks clearly
- Suggest precise fixes
- Separate IAM and S3 issues

Be concise and technical.
"""

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "mistral",
                "prompt": prompt,
                "stream": False
            }
        )

        data = response.json()
        return data.get("response", "No AI response")

    except Exception as e:
        return f"AI failed: {str(e)}"