
import requests

def generate_image(prompt):
    response = requests.post(
        "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0",
        headers={"Authorization": "Bearer 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"},
        json={"inputs": prompt}
    )
    if response.ok:
        # Adjust this line based on actual return structure
        return response.json().get("generated_image_url", "Image generated.")
    return "Error generating image."
