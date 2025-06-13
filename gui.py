import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText

from file_utilities import read_file
from summarizer import summarize_markdown_sections
from ollama_helper import start_ollama, stop_ollama


class SummarizerGUI:
    """Simple interface for summarizing documents with Ollama."""

    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("LLM Summarizer")

        self.input_path = tk.StringVar(value="")
        self.output_path = tk.StringVar(value="")
        self.model_var = tk.StringVar(value="llama3.2")

        self._build_file_selectors()
        self._build_model_entry()
        self._build_text_areas()
        self._build_status_bar()
        self._build_buttons()

    # ------------------------------------------------------------------
    # UI setup helpers
    # ------------------------------------------------------------------
    def _build_file_selectors(self) -> None:
        input_frame = tk.Frame(self.root)
        input_frame.pack(fill="x", pady=2)

        tk.Label(input_frame, text="Input File:").pack(side="left")
        self.input_label = tk.Label(input_frame, text="None", anchor="w")
        self.input_label.pack(side="left", expand=True, fill="x", padx=2)
        tk.Button(input_frame, text="Browse...", command=self.open_file).pack(side="right")

        output_frame = tk.Frame(self.root)
        output_frame.pack(fill="x", pady=2)

        tk.Label(output_frame, text="Output File:").pack(side="left")
        self.output_label = tk.Label(output_frame, text="None", anchor="w")
        self.output_label.pack(side="left", expand=True, fill="x", padx=2)
        tk.Button(output_frame, text="Browse...", command=self.choose_output_file).pack(side="right")

    def _build_model_entry(self) -> None:
        model_frame = tk.Frame(self.root)
        model_frame.pack(fill="x", pady=2)
        tk.Label(model_frame, text="Model (installed in Ollama):").pack(side="left")
        self.model_entry = tk.Entry(model_frame, textvariable=self.model_var, width=20)
        self.model_entry.pack(side="left")

    def _build_text_areas(self) -> None:
        text_frame = tk.Frame(self.root)
        text_frame.pack(fill="both", expand=True)

        self.input_text = ScrolledText(text_frame, width=60, height=30)
        self.summary_text = ScrolledText(text_frame, width=60, height=30)
        self.input_text.pack(side="left", fill="both", expand=True)
        self.summary_text.pack(side="right", fill="both", expand=True)

    def _build_status_bar(self) -> None:
        self.status_label = tk.Label(self.root, text="Ready")
        self.status_label.pack(fill="x", pady=2)

    def _build_buttons(self) -> None:
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(fill="x")
        tk.Button(btn_frame, text="Summarize", command=self.summarize).pack(side="left")
        tk.Button(btn_frame, text="Save Summary", command=self.save_summary).pack(side="left")

    # ------------------------------------------------------------------
    # File operations
    # ------------------------------------------------------------------
    def open_file(self) -> None:
        filepath = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("PDF files", "*.pdf")])
        if not filepath:
            return
        text = read_file(filepath)
        self.input_text.delete("1.0", tk.END)
        self.input_text.insert(tk.END, text)
        self.input_path.set(filepath)
        self.input_label.config(text=filepath)

    def choose_output_file(self) -> str:
        filepath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text File", "*.txt")])
        if filepath:
            self.output_path.set(filepath)
            self.output_label.config(text=filepath)
        return filepath

    # ------------------------------------------------------------------
    # Summarization logic
    # ------------------------------------------------------------------
    def show_summary_popup(self, summary: str) -> ScrolledText:
        popup = tk.Toplevel(self.root)
        popup.title("Summary")
        text_widget = ScrolledText(popup, width=80, height=30)
        text_widget.pack(fill="both", expand=True)
        text_widget.insert(tk.END, summary)
        tk.Button(popup, text="Save Summary", command=lambda: self.save_summary(text_widget)).pack(fill="x")
        return text_widget

    def summarize(self) -> None:
        text = self.input_text.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning("No text", "Please load a file to summarize.")
            return

        self.status_label.config(text="Summarizing...")
        model = self.model_var.get().strip() or "llama3.2"
        process = start_ollama(model=model)
        summary = summarize_markdown_sections(text, model)
        stop_ollama(process)

        self.summary_text.config(state="normal")
        self.summary_text.delete("1.0", tk.END)
        self.summary_text.insert(tk.END, summary)
        self.summary_text.focus_set()
        self.show_summary_popup(summary)
        self.status_label.config(text="Summary complete")

    def save_summary(self, widget: any = None) -> None:
        text_widget = widget or self.summary_text
        summary = text_widget.get("1.0", tk.END).strip()
        if not summary:
            messagebox.showwarning("Empty summary", "There is no text to save.")
            return

        output_path = self.output_path.get()
        if not output_path:
            output_path = self.choose_output_file()
            if not output_path:
                return

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(summary)
        self.output_label.config(text=output_path)
        messagebox.showinfo("Saved", f"Summary saved to {output_path}")

    def run(self) -> None:
        self.root.mainloop()


def main() -> None:
    app = SummarizerGUI()
    app.run()


if __name__ == "__main__":
    main()