This project will provide a local application that summarizes PDF files using an LLM model served through Ollama. 
The summary will be written to a `.txt` file and displayed alongside the original document in a simple GUI. 

## Setup Steps
Note: Ollama will be used because all information remains completely private. No sensitive data will ever leave your device.
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
   2. ```python main.py <inputFilepath> -o/--output <uutputFilepath> -m/--model <model> -k/--keywords <keyword1>,<keyword2>,...,<keywordn>```
      1. The input filepath is the only required parameter, the rest are optional.
      2. The default model if none is specified is ```llama3.2```
      3. The default output path is ```/summary.txt``` in the current folder.
      4. If keywords are provided, extraction is done, but otherwise, extraction will not run.
         1. *Note:* Extraction is buggy at the moment. Performance may be improved when using a larger and more capable model.

### Core features
- **PDF to text extraction**
  - Extracting the text from a .pdf or .txt file and turns this into text formatted using Markdown.
- **Local LLM integration**
  - Using Ollama (```llama3.2``` by default) to summarize the input text.
  - Gives a bulleted list summary.
  - Extracts keywords from a text.
- **Output management**
  - Save the summary to a `.txt` file.

### GUI
- **Upload interface**
  - Build a simple window with an upload button and drag-and-drop area.
  - Show progress while processing the PDF.
- **Side-by-side viewer**
  - Display the original PDF text or pages on the left.
  - Display the generated summary on the right for fact checking.
- **Export options**
  - Add a "Save Summary" button to write the `.txt` file.
  - Allow opening the output folder directly from the GUI.

### Nice-to-have enhancements
- Batch processing of multiple PDFs at once.
- Configurable LLM parameters.
- Fine tuning to fit certain input/output file designs.
- Remember recent files and summaries on startup.
- Allow editing of the summary.txt
- Automatically extract certain tags from the input text for automatically filling output forms
