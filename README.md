This project will provide a local application that summarizes PDF files using an LLM model served through Ollama. 
The summary will be written to a `.txt` file and displayed alongside the original document in a simple GUI. 

## Setup Steps
Note: Ollama will be used because all information remains completely private. No sensitive data will ever leave your device.
1. Download Ollama:
   1. https://ollama.com/download
2. Once Ollama is downloaded locally, run the following command in your terminal:
   1. ```ollama pull <model> e.g. llama3.2```
   2. To view the models that are supported go to: https://ollama.com/search
3. Once this model is downloaded, the script can be run.

## Usage
1. Run Ollama locally using the command:
   1. ```ollama run <model>```
   2. Use the model that was pulled earlier.
   3. You will see that the command line says: ```>>> Send a message (/? for help)```
      1. You can ignore this, but leave it running
      2. When you are done using the summarization tool, you can quit by putting ```/bye``` into the command line.
2. Next, go to the

### Quick start
For development and testing you can run the CLI wrapper directly:

```bash
pip install -r requirements.txt
python summarize_pdf.py <your-file.pdf>
```

This will produce a `<your-file>_summary.txt` file in the same folder.

## Development plan

### Core features
- **PDF to text extraction**
  - Use a Python PDF library such as `pdfminer` or `PyPDF2` to parse the file.
- **Local LLM integration**
  - Connect to the Ollama runtime and send the extracted text for summarization.
  - Provide a way to adjust the desired summary length.
- **Output management**
  - Save the summary to a `.txt` file in the same folder as the original PDF.
  - Optionally keep a summary history for quick reference.

### GUI
- **Upload interface**
  - Build a simple window (e.g. using Tkinter or PySimpleGUI) with an upload button and drag-and-drop area.
  - Show progress while processing the PDF.
- **Side-by-side viewer**
  - Display the original PDF text or pages on the left.
  - Display the generated summary on the right for fact checking.
- **Export options**
  - Add a "Save Summary" button to write the `.txt` file.
  - Allow opening the output folder directly from the GUI.

### Packaging
- **Command-line wrapper**
  - Provide a small CLI for power users to run summarization without the GUI.
- **Create an executable**
  - Use a tool like `PyInstaller` to package the application and its dependencies into a standalone `.exe` file for Windows users.

### Nice-to-have enhancements
- Batch processing of multiple PDFs at once.
- Configurable LLM parameters (temperature, model choice if multiple models are available).
- Remember recent files and summaries on startup.