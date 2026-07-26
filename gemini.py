from config import GEMINI_API_KEY
import requests

FLAG_PROMPT = """
Identify words or phrases that are likely to interrupt a typical reader because their meaning is unfamiliar, technical, specialized, or unusually formal.

Do not judge whether the reader could infer the meaning from context.
Judge only whether the word or phrase itself is likely to require an explanation.

Flag based on term difficulty alone.
Do not consider reader background.

Flag:
- Technical terms and jargon
- Domain specific language
- Formal or uncommon words and phrases that are likely to interrupt comprehension
- Idiomatic or figurative expressions that are specific to a particular field 
  or industry and would not be understood without familiarity with that domain
  (example: "bull run" in finance, "boiling the ocean" in business)
- Acronyms unless universally known
  (skip USA, flag API, SDK, GPU)
- Prefer the smallest complete concept. Do not include surrounding descriptive words.

Do not flag:
- Common everyday English words
- Universally understood concepts
- Common idiomatic expressions understood in everyday conversation regardless of context
  (example: "rough patch", "pick up speed", "under pressure")

Do not:
- Flag duplicates, use first occurrence
- Explain, define, or rewrite anything
- Return anything except the JSON array

Output:
Return only a raw JSON array of strings.
Ordered by first appearance in text.

Do not wrap the JSON in Markdown.
Do not use ```json or ``` code fences.
Do not include any additional text.
"""

EXPLAIN_PROMPT = """
The user tapped a term while reading.
Explain only that term as it is used in the original text.

Rules:
- Explain only the selected term
- Use the surrounding context only to determine the intended meaning of the selected term
- Treat the selected term as the complete unit of explanation
- Do not include the meaning of neighboring words or phrases unless they are part of the selected term
- Assume neighboring technical terms may be selected and explained separately
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
# - The application communicates with the backend through a REST API using JSON payloads secured by JWT authentication.
# - The physician diagnosed the patient with chronic gastritis after an endoscopy revealed inflammation of the stomach lining. A proton pump inhibitor was prescribed to reduce acid production and relieve symptoms.

def request_gemini(system_instruction, user_input, id=None):
    URL = "https://generativelanguage.googleapis.com/v1beta/interactions"

    headers = {
        "x-goog-api-key": GEMINI_API_KEY,
        "Content-Type": "application/json"
    }

    body = {
        "model": "gemini-3.5-flash-lite",
        "system_instruction": system_instruction,
        "input": user_input,
        "generation_config": {
            "thinking_level": "low",
        }
    }

    if id is not None:
        body["previous_interaction_id"] = id

    try:
        response = requests.post(
            URL,
            headers=headers,
            json=body
        )
    except requests.exceptions.RequestException as e:
        print(e)
        return None

    data = response.json()

    if "error" in data:
        print("Request failed!")
        print(data["error"]["code"])
        print(data["error"]["message"])
        print(f"Status: {response.status_code}")
        return None

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

if flag_terms is None:
    exit()

previous_id = flag_terms["id"]

print(flag_terms["output_text"], "\n")

while True:
    term_define = input("Enter word to define: ")
    term_explanation = request_gemini(EXPLAIN_PROMPT, term_define, previous_id)

    if term_explanation is not None:
        print(term_explanation["output_text"], "\n")
