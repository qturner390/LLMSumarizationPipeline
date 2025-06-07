import requests

OLLAMA_URL = 'http://localhost:11434/api/chat'


def summarize_with_ollama(title: str, content: str, model: str) -> str:
    """
    Summarizes a given section of text.
    If there is a title, this is given to the model; If not, no title is used in the prompt.

    Args:
        title: Title of the section
        content: Text of the section
        model: Model to use for summarization

    Returns:
        Summary of the content. If there is an error, returns the error.
    """
    if title:
        added_text = f" titled '{title}'"
    else:
        added_text = ""

    payload = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": "You are an expert summarizer who outputs exclusively concise bulleted lists. You should only be extracting the most important and interesting information. Every bullet point you create should be a complete sentence using proper grammar. You should prefer shorter summaries, but in information-dense sections, it is ok to have a greater number of bullet points. Do not include any introductions or conclusions in any circumstance. Do not add any additional or outside information to the summaries."
            },
            {
                "role": "user",
                "content": f"Summarize the following section{added_text}:\n\n{content.strip()}"
            }
        ],
        "stream": False
    }
    response = requests.post(OLLAMA_URL, json=payload)

    if response.ok:
        return response.json()['message']['content'].strip()
    else:
        return f"Error: {response.status_code} - {response.text}"
