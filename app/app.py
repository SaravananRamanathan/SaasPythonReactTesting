from ast import keyword
import os
from unittest import result
from dotenv import load_dotenv
import openai
import argparse
import re
load_dotenv() 
MAX_INPUT_LENGTH=32
def main():
    print("running app")
    parser = argparse.ArgumentParser()
    parser.add_argument("--input","-i",type=str, required=True)
    args=parser.parse_args()
    user_input = args.input
    print(f"user input is: {user_input}")
    if validate_length(user_input):
        results = generate_branding_snippet(user_input)
        keywords_results = generate_keywords(user_input)
        
    else:
        ""
        raise ValueError(f"Input length is too long, must me under {MAX_INPUT_LENGTH}. Submitted input is {user_input}")

def validate_length(prompt:str):
    ""
    return len(prompt)<=MAX_INPUT_LENGTH

def generate_branding_snippet(subject):
    openai.organization = "org-O3Iloxhc9IgMU9ToHnUg9f3d"
    openai.api_key = os.environ.get("OPENAI_API_KEY")
    prompt = f"Generate upbeat branding snippet for {subject}"
    print(prompt)
    response = openai.Completion.create(model="text-davinci-002", prompt=prompt, temperature=1, max_tokens=32)

    #extract text
    branding_text:str=response["choices"][0]["text"]
    branding_text= branding_text.strip()
    if branding_text[-1] not in {".","!","?"}:
        branding_text+="..."

    print(f"Branding Text: {branding_text}")

    #print(f"branding text: {branding_text}")
    return branding_text

def generate_keywords(subject):
    openai.organization = "org-O3Iloxhc9IgMU9ToHnUg9f3d"
    openai.api_key = os.environ.get("OPENAI_API_KEY")
    prompt = f"Generate related branding keywords for {subject}"
    print(prompt)
    response = openai.Completion.create(model="text-davinci-002", prompt=prompt, temperature=1, max_tokens=32)

    #extract text
    keyword_text:str=response["choices"][0]["text"]
    keyword_text= keyword_text.strip()

    keywords_array = re.split(',|\n|;|-',keyword_text)
    keywords_array = [k.lower().strip() for k in keywords_array if len(k)>0]

    
    print(f"Keywords: {keywords_array}")
    return keywords_array

if __name__ == "__main__":
    main()