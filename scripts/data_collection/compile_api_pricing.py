import pandas as pd

openai_models = [
    {"Provider": "OpenAI", "Model": "gpt-5", "Type": "text", "Price_per_1k_tokens_or_generation": 1.25, "Max_tokens_or_resolution": None, "Notes": "input: $1.25/1M tokens, output: $10.00/1M tokens", "Link": "https://openai.com"},
    {"Provider": "OpenAI", "Model": "gpt-5-mini", "Type": "text", "Price_per_1k_tokens_or_generation": 0.25, "Max_tokens_or_resolution": None, "Notes": "input: $0.25/1M tokens, output: $2.00/1M tokens", "Link": "https://openai.com"},
    {"Provider": "OpenAI", "Model": "gpt-5-nano", "Type": "text", "Price_per_1k_tokens_or_generation": 0.05, "Max_tokens_or_resolution": None, "Notes": "input: $0.05/1M tokens, output: $0.40/1M tokens", "Link": "https://openai.com"},
    {"Provider": "OpenAI", "Model": "gpt-4-turbo", "Type": "text", "Price_per_1k_tokens_or_generation": 0.03, "Max_tokens_or_resolution": 8192, "Notes": "prompt + completion", "Link": "https://openai.com"},
    {"Provider": "OpenAI", "Model": "gpt-3.5-turbo", "Type": "text", "Price_per_1k_tokens_or_generation": 0.002, "Max_tokens_or_resolution": 4096, "Notes": "prompt + completion", "Link": "https://openai.com"},
    {"Provider": "OpenAI", "Model": "text-embedding-ada-002", "Type": "embedding", "Price_per_1k_tokens_or_generation": 0.0004, "Max_tokens_or_resolution": None, "Notes": "", "Link": "https://openai.com"},
    {"Provider": "OpenAI", "Model": "DALL·E 3", "Type": "image", "Price_per_1k_tokens_or_generation": 0.02, "Max_tokens_or_resolution": "1024x1024", "Notes": "image generation", "Link": "https://openai.com"},
    {"Provider": "OpenAI", "Model": "Whisper", "Type": "audio", "Price_per_1k_tokens_or_generation": 0.006, "Max_tokens_or_resolution": None, "Notes": "audio transcription", "Link": "https://openai.com"}
]

gemini_models = [
    {"Provider": "Gemini", "Model": "gemini-2.5-pro", "Type": "text", "Price_per_1k_tokens_or_generation": 0.025, "Max_tokens_or_resolution": 8000, "Notes": "", "Link": "https://developers.deepmind.com/"},
    {"Provider": "Gemini", "Model": "gemini-image-gen", "Type": "image", "Price_per_1k_tokens_or_generation": 0.02, "Max_tokens_or_resolution": "1024x1024", "Notes": "", "Link": "https://developers.deepmind.com/"},
    {"Provider": "Gemini", "Model": "gemini-video-gen", "Type": "video", "Price_per_1k_tokens_or_generation": 0.05, "Max_tokens_or_resolution": "480p/30s", "Notes": "", "Link": "https://developers.deepmind.com/"}
]

all_data = openai_models + gemini_models
df = pd.DataFrame(all_data)

df.to_csv("../../data/raw/openai_gemini_models.csv", index=False)
