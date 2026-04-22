import requests

def analyze_with_ai(findings):
    prompt = f"""
    Analyze these cloud security findings:
    {findings}

    Explain risks and suggest fixes.
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