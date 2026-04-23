import requests

def analyze_with_ai(findings):
    prompt = f"""
    You are a cloud security expert.

    Analyze the following IAM findings:
    {findings}

    For each finding:
    1. Explain the exact risk
    2. Suggest a precise least-privilege fix
    3. Prioritize critical issues first

    Be concise and technical.
    """

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "mistral",
                "prompt": prompt,
                "stream": False
            }
        )

        data = response.json()

        if "response" not in data:
            print("AI ERROR:", data)
            return "AI analysis failed"

        return data["response"]

    except Exception as e:
        print("Connection Error:", str(e))
        return "AI not available"