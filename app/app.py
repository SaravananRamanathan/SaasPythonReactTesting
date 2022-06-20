import os
from dotenv import load_dotenv
import openai
load_dotenv() 
openai.organization = "org-O3Iloxhc9IgMU9ToHnUg9f3d"
openai.api_key = os.environ.get("OPENAI_API_KEY")
print("testing")
subject = "Coffee"
prompt = f"Generate upbeat branding snippet for {subject}"
response = openai.Completion.create(model="text-davinci-002", prompt=prompt, temperature=0, max_tokens=32)
print(response)
#print(openai.Model.list())