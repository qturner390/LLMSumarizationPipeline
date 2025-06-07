import argparse


def start_parser():
    parser = argparse.ArgumentParser(description="Summarize a document using Ollama.")
    parser.add_argument(
        'filepath',
        help="Path to the file"
    )
    parser.add_argument(
        "-o", "--output",
        default="summary.txt",
        help="Path to the output file."
    )
    args = parser.parse_args()
    return args
