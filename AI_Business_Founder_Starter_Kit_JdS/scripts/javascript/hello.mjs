import OpenAI from "openai";

if (!process.env.OPENAI_API_KEY) {
  throw new Error('Set OPENAI_API_KEY. In PowerShell: setx OPENAI_API_KEY "YOUR_KEY" then reopen terminal.');
}

const client = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });

const resp = await client.chat.completions.create({
  model: "gpt-4o-mini",
  messages: [{ role: "user", content: "Di hola en una frase y termina con 🚀" }],
});

console.log(resp.choices[0].message.content);
