import os
import google.generativeai as genai
import sys

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise EnvironmentError("Missing GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-pro')

file_path = sys.argv[1]
with open(file_path, 'r') as f:
    code = f.read()

prompt = f"Please review this Python Flask code and suggest improvements:\n\n{code}"
response = model.generate_content(prompt)
print("\n--- Gemini Review Output ---\n")
print(response.text)