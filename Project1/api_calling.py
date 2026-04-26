from google import genai
import os
from dotenv import load_dotenv

# loading the environment variable
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

# initializing the client
client = genai.Client(api_key=api_key)

# note generator
def note_generator(images):
    prompt = """Generate a concise summary of the notes in the images. Focus on key points, main ideas, and important details. The summary should be clear and easy to understand, capturing the essence of the content in a few sentences(100 words)."""
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[images, prompt]
    )
    return response.text