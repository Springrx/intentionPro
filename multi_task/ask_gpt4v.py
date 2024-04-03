import requests
configs={
    "OPENAI_API_KEY": "sk-<your-openai-api-key>",
    "OPENAI_API_MODEL": "gpt-4-vision-preview",
    "TEMPERATURE": 0.0,
    "MAX_TOKENS": 4000,
    "OPENAI_API_BASE": "https://api.openai.com/v1/chat/completions",
}
def ask_gpt4v(content):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {configs['OPENAI_API_KEY']}"
    }
    payload = {
        "model": configs["OPENAI_API_MODEL"],
        "messages": [
            {
                "role": "user",
                "content": content
            }
        ],
        "temperature": configs["TEMPERATURE"],
        "max_tokens": configs["MAX_TOKENS"]
    }
    response = requests.post(configs["OPENAI_API_BASE"], headers=headers, json=payload)
    if "error" not in response.json():
        usage = response.json()["usage"]
        prompt_tokens = usage["prompt_tokens"]
        completion_tokens = usage["completion_tokens"]
        # print_with_color(f"Request cost is "
        #                  f"${'{0:.2f}'.format(prompt_tokens / 1000 * 0.01 + completion_tokens / 1000 * 0.03)}",
        #                  "yellow")
    return response.json()