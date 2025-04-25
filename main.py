### 🔥 Starter GPT bot pre seneckymlok 🔥
# Používa OpenAI API + CLI command handler + bezpečné .env

import openai
import os
from dotenv import load_dotenv

# 🛡️ Načítaj environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# 🤖 Funkcia na komunikáciu s GPT

def chat_with_gpt(prompt: str, system_msg: str = "You are a helpful assistant.", model: str = "gpt-3.5-turbo"):
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": system_msg},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ Error: {str(e)}"

# 🖥️ CLI Interface

def main():
    print("🔥 Senecký Mlok GPT bot ready. Type 'exit' to quit.")
    while True:
        user_input = input("You 🐍: ")
        if user_input.lower() in ["exit", "quit"]:
            print("👋 Zbohom, Mlok odchádza.")
            break
        reply = chat_with_gpt(user_input)
        print(f"MlokGPT 🤖: {reply}\n")

if __name__ == "__main__":
    main()
