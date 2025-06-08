from processor import summarize_document
from cli import start_parser
from ollama_helper import start_ollama, stop_ollama
import atexit


if __name__ == '__main__':
    args = start_parser()  # Get the command line args
    process = start_ollama(model=args.model)  # Start Ollama locally

    if args.keywords == "":
        keywords = [""]
    else:
        keywords = args.keywords.strip()
        keywords = keywords.replace(" ", "")
        keywords = keywords.split(",")

    if process:
        # If the process is terminated early, stop Ollama
        atexit.register(stop_ollama, process)

    print(f"{'-'*70}\nUsing the model: {args.model}\n{'-'*70}\nUsing the file: {args.filepath}\n{'-'*70}\nSaving to: {args.output}\n{'-'*70}")
    if keywords != [""]:
        print(f"Using the keywords: {','.join(keywords)}\n{'-'*70}")
    summarize_document(filepath=args.filepath, keywords=keywords, output_path=args.output, model=args.model)
    stop_ollama(process)
