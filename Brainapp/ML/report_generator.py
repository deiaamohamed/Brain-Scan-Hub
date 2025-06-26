from openai import OpenAI


FREE_API_KEY = "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"
LARGE_API_KEY = "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"

OPENROUTER_HEADERS = {
    "HTTP-Referer": "http://127.0.0.1:8000",
    "X-Title": "Brain Scan Hub"
}

free_model_client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=FREE_API_KEY,
    default_headers=OPENROUTER_HEADERS,
)

large_model_client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=LARGE_API_KEY,
    default_headers=OPENROUTER_HEADERS,
)

def generate_medical_report(caption: str) -> str:
    prompt = (
        "You are an experienced radiologist. Based on the following high-level observation, "
        "generate a concise, professional, and medically accurate radiology report. "
        "Do not mention image format, colors, overlays, or patient information like name or age.\n\n"
        f"Observation: {caption}\n\n"
        "Radiology Report:"
    )

    try:
        response = large_model_client.chat.completions.create(
            model="mistralai/mistral-7b-instruct",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300,
            temperature=0.4,
        )
        return "[mistral-7b-instruct]\n" + response.choices[0].message.content.strip()
    except Exception as e:
        print("Large model failed, falling back to free model:", e)
        response = free_model_client.chat.completions.create(
            model="mistralai/devstral-small:free",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=200,
            temperature=0.3,
        )
        return "[devstral-small:free]\n" + response.choices[0].message.content.strip()
