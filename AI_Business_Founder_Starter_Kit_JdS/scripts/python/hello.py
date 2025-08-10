from openai import OpenAI
import os

def main():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        # OJO: este mensaje está bien comillado; copia exacto.
        raise RuntimeError('OPENAI_API_KEY is not set. In PowerShell: setx OPENAI_API_KEY "YOUR_KEY" and reopen the terminal.')

    client = OpenAI(api_key=api_key)
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": "Di hola en una frase y termina con 🚀"}],
    )
    print(resp.choices[0].message.content)

if __name__ == "__main__":
    main()
