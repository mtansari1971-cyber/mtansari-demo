from google import genai

client = genai.Client(api_key="YOUR_API_KEY")
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="explain to me how does a gemini api works in one sentence")

print(response.text)
    