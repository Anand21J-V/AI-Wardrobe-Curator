import requests
import base64

def analyze_image(image_bytes, groq_api_key):
    # Encode image to base64 string
    img_b64 = base64.b64encode(image_bytes).decode("utf-8")
    
    headers = {
        "Authorization": f"Bearer {groq_api_key}",
        "Content-Type": "application/json"
    }

    # Adjust payload to send base64 image directly
    data = {
        "model": "llama-3.2-11b-vision-preview",
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Describe the clothing item in this image."},
                    {"type": "image_base64", "image_base64": img_b64}
                ]
            }
        ],
        "temperature": 0.5,
        "max_tokens": 100
    }

    response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=data)
    response.raise_for_status()
    return response.json()['choices'][0]['message']['content']
