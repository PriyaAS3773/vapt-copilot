# VAPT-Copilot
 
**Vulnerability Assessment and Penetration Testing Copilot** — an AI-assisted security scanning tool that automates network scanning, analyzes findings using AI, and generates professional PDF security reports.
 
## About
 
VAPT-Copilot simplifies the vulnerability assessment process by combining traditional network scanning (Nmap) with AI-powered analysis (Google Gemini API). It automatically detects open ports and services on a target, explains associated security risks in plain language, and compiles everything into a structured PDF report.
 
## How It Works
 
1. **Scanning** — Uses Nmap to scan a target and detect open ports, running services, and versions
2. **Data Structuring** — Converts raw scan output into clean, structured JSON
3. **AI Analysis** — Sends scan data to Gemini AI to assess risk severity (High/Medium/Low) and suggest remediation steps
4. **Reporting** — Generates a professional PDF report combining scan results and AI analysis
 
## Tech Stack
 
- Python
- Nmap (via python-nmap)
- Google Gemini API (AI analysis)
- ReportLab (PDF generation)
 
## How to Run
 
1. Clone this repository
2. Create a virtual environment and activate it:
   python -m venv venv
   venv\\Scripts\\activate
3. Install dependencies:
   pip install python-nmap google-genai python-dotenv reportlab
4. Create a .env file with your Gemini API key:
   GEMINI_API_KEY=your_key_here
5. Run the scanner:
   python scanner.py
6. Run AI analysis:
   python ai_analyzer.py
7. Generate the PDF report:
   python report_generator.py
 
## Disclaimer
 
This tool is intended for authorized security testing only. Only scan systems and websites you own or have explicit permission to test. Unauthorized scanning may be illegal under applicable laws.
 
## Sample Output
 
Includes a sample VAPT_Report.pdf demonstrating a scan report with port details and AI-generated risk analysis.
 
Author: Priya A S
