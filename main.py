from processor import summarize_document
from cli import start_parser


if __name__ == '__main__':
    args = start_parser()
    print(f"Starting summary of {args.filepath}")
    summarize_document(args.filepath)