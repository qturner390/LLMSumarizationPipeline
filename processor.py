from file_utilities import read_file, split_into_sections
from summarizer import summarize_with_ollama


def summarize_document(filepath: str, output_path: str = 'summary.txt', sectionize: bool = False) -> None:
    if sectionize:
        """TODO: IMPLEMENT ONCE split_into_sections IS IMPLEMENTED"""

    text = read_file(filepath)
    summary = summarize_with_ollama("", text)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(summary)

    print(f"Final summary saved to {output_path}")
