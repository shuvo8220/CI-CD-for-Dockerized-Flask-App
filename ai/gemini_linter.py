import os
import sys
import google.generativeai as genai

# 1. Load API Key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise EnvironmentError("Missing GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-2.5-flash')

# 2. Get File Path
if len(sys.argv) < 2:
    print("Usage: python gemini_linter.py <file_path>")
    sys.exit(1)

file_path = sys.argv[1]
if not os.path.isfile(file_path):
    print(f"Error: File not found - {file_path}")
    sys.exit(1)

# 3. Read Code
with open(file_path, 'r') as f:
    code = f.read()

# Optional: Truncate if too long
MAX_TOKENS = 12000
if len(code) > MAX_TOKENS:
    code = code[:MAX_TOKENS]

# 4. Prompt
prompt = f"""
You are a senior Python reviewer. Review the following Flask application code:
- Check for security issues
- Performance optimization
- PEP8 style compliance
- Suggest improvements if any

Code:
{code}
"""

# 5. Generate Review
response = model.generate_content(prompt)

# 6. Show Output
print("\n--- Gemini Review Output ---\n")
print(response.text)
