import requests

def generate_outfits(descriptions, groq_api_key):
    prompt = "You are a fashion stylist. Given these clothing items:\n"
    prompt += "\n".join(f"- {desc}" for desc in descriptions)
    prompt += "\n\nSuggest 5 capsule wardrobe outfit combinations. For each:\n- Items used\n- Style name\n- Suggested occasion"

    headers = {
        "Authorization": f"Bearer {groq_api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama-3.3-70b-versatile",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7,
        "max_tokens": 600
    }

    response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=data)
    response.raise_for_status()
    return response.json()['choices'][0]['message']['content']
