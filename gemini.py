from config import GEMINI_API_KEY
import requests

FLAG_PROMPT = """
Identify terms in the given text that are 
inherently technical, specialized, or 
uncommon enough that many readers would 
not immediately understand them.

Flag based on term difficulty alone.
Do not consider reader background.

Flag:
- Technical terms and jargon
- Domain specific language
- Uncommon phrases
- Acronyms unless universally known
  (skip USA, flag API, SDK, GPU)
- Prefer the smallest complete concept. Do not include surrounding descriptive words.

Do not flag:
- Common everyday English words
- Universally understood concepts

Do not:
- Flag duplicates, use first occurrence
- Explain, define, or rewrite anything
- Return anything except the JSON array

Output:
Valid JSON array of strings only.
Ordered by first appearance in text.
"""

EXPLAIN_PROMPT = """
The user tapped a term while reading.
Explain only that term as it is used in the original text.

Rules:
- Explain only the selected term
- Use the surrounding context from the original text
- Explain the selected term in the context of the original text, 
  not as a standalone dictionary definition.
- Prefer simple, everyday English
- Avoid introducing new technical or specialized terms
  unless necessary
- Keep the explanation to 1 or 2 short sentences
- Do not rewrite or summarize the original text
- Do not explain anything beyond the selected term
- No bullets, headings, formatting, or quotation marks
  around the explanation

Goal:
Give just enough context so the reader can immediately
continue reading without losing the flow.
"""

# example text:
# - The aforementioned party shall hereby indemnify the aggrieved party against any consequential damages arising from the breach of contract.
# - The patient presented with acute dyspnea, mild contusions, and elevated readings indicating hypertension. We advised rest and follow-up.

def request_gemini(system_instruction, user_input, id=None):
    URL = "https://generativelanguage.googleapis.com/v1beta/interactions"

    headers = {
        "x-goog-api-key": GEMINI_API_KEY,
        "Content-Type": "application/json"
    }

    body = {
        "model": "gemini-3.6-flash",
        "system_instruction": system_instruction,
        "input": user_input,
        "generation_config": {
            "thinking_level": "minimal",
            "seed": 42
        }
    }

    if id is not None:
        body["previous_interaction_id"] = id

    response = requests.post(
        URL,
        headers=headers,
        json=body
    )

    data = response.json()

    return {
        "id": data["id"],
        "output_text": data["steps"][-1]["content"][0]["text"],
        "usage": {
            "total_tokens": data["usage"]["total_tokens"],
            "input_tokens": data["usage"]["total_input_tokens"],
            "output_tokens": data["usage"]["total_output_tokens"],
            "thought_tokens": data["usage"]["total_thought_tokens"]
        }
    }

text = input("Enter text: ")

flag_terms = request_gemini(FLAG_PROMPT, text)
previous_id = flag_terms["id"]

print(flag_terms["output_text"], "\n")

while True:
    term_define = input("Enter word to define: ")
    term_explanation = request_gemini(EXPLAIN_PROMPT, term_define, previous_id)
    print(term_explanation["output_text"], "\n")