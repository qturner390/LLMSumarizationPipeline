## Setup Steps
Note: Ollama will be used because all information remains completely private. No data will ever leave your device.
1. Download Ollama:
   1. https://ollama.com/download
2. Once Ollama is downloaded locally, run the following command in your terminal:
   1. ```ollama pull <model>``` e.g. llama3.2
   2. To view the models that are supported go to: https://ollama.com/search
3. Once this model is downloaded, the script can be run.

## Usage
1. Make sure that you can run Python files. You can use an IDE or CE of your choosing or just use the terminal.
2. Inside the folder ```LLMSummarizationPipeline```, run the following commands in the terminal:
   1. ```pip install -r requirements.txt```
      1. This will install all the dependencies to run the project.
3. Then, depending if you would rather use the command line or a graphical interface:

### Command Line
2. To run the code in the command line run: ```python main.py <inputFilepath> -o/--output <uutputFilepath> -m/--model <model> -k/--keywords <keyword1>,<keyword2>,...,<keywordn>```
   1. The input filepath is the only required parameter, the rest are optional.
   2. The default model if none is specified is ```llama3.2```
   3. The default output path is ```/summary.txt``` in the current folder.
   4. If keywords are provided, extraction is done, but otherwise, extraction will not run.
      1. *Note:* Extraction is buggy at the moment. Performance may be improved when using a larger and more capable model.

### Graphical Interface
1. To use a graphical interface instead of the command line, run the command:
   1. ```python gui.py```
   2. This will launch a separate window that allows you to select an input filepath, output filepath, and model.
   3. There will be two text boxes that show the parsed original text and the output text.

## Next Steps
- Batch processing of multiple PDFs at once.
- Configurable LLM parameters.
- Fine tuning to fit certain input/output file designs.
- Remember recent files and summaries on startup.
- Allow editing of the summary.txt
- Automatically extract certain tags from the input text for automatically filling output forms
