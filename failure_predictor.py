from ollama import Client

# Connect to local Ollama
client = Client(host='http://localhost:11434')

# Prompt for CI/CD prediction
prompt = """
<|System|>: You are a CI/CD pipeline prediction assistant. You will be given past build logs and a new build scenario. Predict whether the build will succeed or fail.
<|User|>: 
Historical Build Logs:
- Build 1: tests passed, lint passed, docker pushed → Success
- Build 2: tests failed, lint passed, docker pushed → Fail
- Build 3: tests passed, lint failed, docker not pushed → Fail

Current Build:
- tests passed: True
- lint passed: False
- docker pushed: True

Answer only with "Success" or "Fail" and explain why in one sentence.
<|Assistant|>:
"""

# Generate response using DeepSeek model
response = client.generate(
    model='llama2:7b-chat',
    prompt=prompt,
    stream=False
)

# Show prediction
print("🔮 Prediction:\n")
print(response['response'].strip())


