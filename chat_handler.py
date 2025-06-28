
import openai

openai.api_key = "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"

def ask_ai(prompt):
    res = openai.ChatCompletion.create(
        model="mistralai/mixtral-8x7b",
        messages=[{"role": "user", "content": prompt}]
    )
    return res['choices'][0]['message']['content']
