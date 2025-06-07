import argparse


def start_parser():
    parser = argparse.ArgumentParser(description="Summarize a document using Ollama.")
    parser.add_argument(
        'filepath',
        help="Path to the file"
    )
    parser.add_argument(
        "-o", "--output",
        default="Summaries/summary.txt",
        help="Path to the output file."
    )
    parser.add_argument(
        "-m", "--model",
        default="llama3.2",
        help="Name of the model to use for summarization."
    )
    args = parser.parse_args()
    return args
