from google import genai
import json
import os
from dotenv import load_dotenv

# .env file-ൽ നിന്ന് API key load ചെയ്യുക
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("[ERROR] API key not found! .env file check ചെയ്യുക.")
    exit()

client = genai.Client(api_key=api_key)


def analyze_scan(json_file):
    with open(json_file, 'r') as f:
        scan_data = json.load(f)

    prompt = f"""
You are a cybersecurity expert helping analyze a Nmap vulnerability scan.

Here is the scan result in JSON format:
{json.dumps(scan_data, indent=2)}

Please provide:
1. A summary of open ports and what risk each one poses
2. Which findings are HIGH, MEDIUM, or LOW severity
3. Simple remediation steps for each risk

Keep the explanation clear and beginner-friendly.
"""

    response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=prompt
)

    return response.text


if __name__ == "__main__":
    filename = input("Enter the JSON scan file name (e.g. scan_result_scanme_nmap_org.json): ")

    print("\n[+] Sending scan data to AI for analysis... please wait\n")
    analysis = analyze_scan(filename)

    print("--- AI SECURITY ANALYSIS ---\n")
    print(analysis)

    with open("ai_analysis_report.txt", "w", encoding="utf-8") as f:
        f.write(analysis)

    print("\n[+] Report saved to ai_analysis_report.txt")