import argparse


def start_parser():
    """
    Sets up the command line interface parameters.

    Args:

    Returns:
        The command line arguments.
    """
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
    parser.add_argument(
        "-k", "--keywords",
        default="",
        help="Comma separated keywords."
    )
    args = parser.parse_args()
    return args
