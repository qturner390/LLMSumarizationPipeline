import requests

OLLAMA_URL = 'http://localhost:11434/api/chat'


def extract_with_ollama(keywords: [str], content: str, model: str) -> str:
    """
    Extract entities from keywords in a given text.

    DOESN'T ALWAYS WORK AS INTENDED. BE VERY CAUTIOUS ABOUT USING ANY OF THESE.

    Args:
        keywords: list of keywords
        content: Text of the section
        model: Model to use for summarization

    Returns:
        Summary of the content. If there is an error, returns the error.
    """
    if not keywords:
        print("No keywords provided.")
        return ""
    else:
        keyword_text = ",\n".join(keywords)

    payload = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": "You are a professional information extractor. Given a list of keywords, you find the best entity or descriptor that fits the keyword in the provided text. If there is more than one option, then give both. Do not respond with any introduction or conclusion. Respond in the format <keyword>:<bestFit> for each keyword giving the keyword exactly as inputted. Do not make any assumptions or put any information that isn't present in the provided text. At the end of your response, very concisely explain any ambiguity or unsure decisions you made."
            },
            {
                "role": "user",
                "content": f"Your keywords are:\n {keyword_text}.\nFind the best fitting entities for each keyword in the following text:\n\n{content.strip()}"
            }
        ],
        "stream": False
    }
    response = requests.post(OLLAMA_URL, json=payload)

    if response.ok:
        return response.json()['message']['content'].strip()
    else:
        return f"Error: {response.status_code} - {response.text}"
