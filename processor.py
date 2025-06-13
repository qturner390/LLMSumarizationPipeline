from file_utilities import read_file
from summarizer import summarize_markdown_sections
from extractor import extract_with_ollama


def summarize_document(filepath: str, keywords: [str], output_path: str = 'Summaries/summary.txt',  model='llama3.2') -> None:
    """
    Reads the text from a file at a given filepath and summarizes it.
    If keywords are provided, a keyword extraction will be done, which will be at the bottom of the output file.
    Args:
        filepath: path to the file to be summarized
        keywords: list of strings that are the keywords to extract from the text
        output_path: Path of the file to save the output to.
        model: Ollama model to use to run.

    Returns:
        None
    """
    text = read_file(filepath)
    print("Starting summarization...")
    summary = summarize_markdown_sections("", text, model)

    if keywords == [""]:
        print("No keywords provided, skipping extraction.")
    else:
        print("Starting keyword extraction...")
        extracted_words = extract_with_ollama(keywords, text, model)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(summary)
        if keywords != [""]:
            f.write("\n\nKEYWORDS:\n")
            f.write(extracted_words)

    print(f"Final summary saved to {output_path}.")
    return
