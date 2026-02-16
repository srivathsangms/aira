from google import genai

def analyze_resume(api_key,input_text):
    client=genai.Client(api_key=api_key)
    prompt=input_text+"""
You are a professional resume analyser.

If the document is not a resume, reply strictly:
INVALID RESUME

If it is a resume, respond ONLY in this exact format:

RATING: X/10
SECTOR: <Sector Name>

ANALYSIS:
## Strengths
<list strengths>

## Weaknesses
<list weaknesses>

## Improvements
<advise on improvements>

## Interview Questions
<suggest 3-5 interview questions>
"""
    response=client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text
