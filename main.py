from processor import summarize_document
from cli import start_parser
from ollama_helper import start_ollama, stop_ollama
import atexit


if __name__ == '__main__':
    args = start_parser()
    process = start_ollama()
    if process:
        atexit.register(stop_ollama, process)
    print(f"Starting summary of {args.filepath}")
    summarize_document(filepath=args.filepath, output_path=args.output if args.output else None)
    stop_ollama(process)
