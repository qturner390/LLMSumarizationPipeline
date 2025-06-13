import requests
import re

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


def _split_markdown_sections(text: str) -> list[tuple[str, str]]:
    """Return (header, content) tuples for markdown sections."""
    pattern = re.compile(r"^(#{1,6}\s+.*)$", re.MULTILINE)
    matches = list(pattern.finditer(text))

    if not matches:
        return [("", text.strip())]

    sections: list[tuple[str, str]] = []

    if matches[0].start() > 0:
        pre_content = text[: matches[0].start()].strip()
        if pre_content:
            sections.append(("", pre_content))

    for i, match in enumerate(matches):
        header_line = match.group(1).strip()
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        content = text[start:end].strip()
        sections.append((header_line, content))

    return sections


def summarize_markdown_sections(text: str, model: str) -> str:
    """Summarize each markdown section individually and join the results."""
    sections = _split_markdown_sections(text)
    summaries = []
    for header, content in sections:
        title = header.split(None, 1)[1] if header else ""
        section_summary = summarize_with_ollama(title, content, model)
        if header:
            summaries.append(f"{header}\n{section_summary}")
        else:
            summaries.append(section_summary)

    return "\n\n".join(summaries).strip()
