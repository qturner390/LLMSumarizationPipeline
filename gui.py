import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText
from file_utilities import read_file
from summarizer import summarize_with_ollama
from ollama_helper import start_ollama, stop_ollama


def open_file(text_widget, path_label):
    filepath = filedialog.askopenfilename(filetypes=[('Text and PDF files', '*.txt *.pdf')])
    if not filepath:
        return ''
    text = read_file(filepath)
    text_widget.delete('1.0', tk.END)
    text_widget.insert(tk.END, text)
    path_label.config(text=f"Input: {filepath}")
    return filepath


def choose_output_file(path_label):
    filepath = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[('Text File', '*.txt')])
    if filepath:
        path_label.config(text=f"Output: {filepath}")
    return filepath


def show_summary_popup(summary: str, output_path_var, output_label):
    """Open a new window containing the summary text for editing."""
    popup = tk.Toplevel()
    popup.title('Summary')
    text_widget = ScrolledText(popup, width=80, height=30)
    text_widget.pack(fill='both', expand=True)
    text_widget.insert(tk.END, summary)
    tk.Button(popup, text='Save Summary',
              command=lambda: save_summary(text_widget, output_path_var, output_label)).pack(fill='x')
    return text_widget


def summarize(text_widget, summary_widget, model_entry, status_label,
              output_path_var, output_label):
    text = text_widget.get('1.0', tk.END).strip()
    if not text:
        messagebox.showwarning('No text', 'Please load a file to summarize.')
        return
    status_label.config(text='Summarizing...')
    model = model_entry.get().strip() or 'llama3.2'
    process = start_ollama(model=model)
    summary = summarize_with_ollama('', text, model)
    stop_ollama(process)
    summary_widget.config(state='normal')
    summary_widget.delete('1.0', tk.END)
    summary_widget.insert(tk.END, summary)
    summary_widget.focus_set()
    show_summary_popup(summary, output_path_var, output_label)
    status_label.config(text='Summary complete')


def save_summary(summary_widget, output_path_var, output_label):
    summary = summary_widget.get('1.0', tk.END).strip()
    if not summary:
        messagebox.showwarning('Empty summary', 'There is no text to save.')
        return
    output_path = output_path_var.get()
    if not output_path:
        output_path = choose_output_file(output_label)
        if not output_path:
            return
        output_path_var.set(output_path)
    else:
        output_label.config(text=f"Output: {output_path}")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(summary)
    messagebox.showinfo('Saved', f'Summary saved to {output_path}')


def main():
    root = tk.Tk()
    root.title('LLM Summarizer')

    input_text = ScrolledText(root, width=60, height=30)
    summary_text = ScrolledText(root, width=60, height=30)

    input_path = tk.StringVar()
    output_path = tk.StringVar()

    input_label = tk.Label(root, text='Input: none')
    input_label.pack(fill='x')
    output_label = tk.Label(root, text='Output: none')
    output_label.pack(fill='x')

    tk.Label(root, text='Model (must be downloaded locally from Ollama prior to running):').pack()
    model_entry = tk.Entry(root)
    model_entry.insert(0, 'llama3.2')
    model_entry.pack(fill='x')

    frame = tk.Frame(root)
    frame.pack(fill='both', expand=True)

    input_text.pack(in_=frame, side='left', fill='both', expand=True)
    summary_text.pack(in_=frame, side='right', fill='both', expand=True)

    status_label = tk.Label(root, text='Ready')
    status_label.pack(fill='x')

    btn_frame = tk.Frame(root)
    btn_frame.pack(fill='x')

    tk.Button(btn_frame, text='Open File', command=lambda: input_path.set(open_file(input_text, input_label))).pack(side='left')
    tk.Button(btn_frame, text='Choose Output', command=lambda: output_path.set(choose_output_file(output_label))).pack(side='left')
    tk.Button(
        btn_frame,
        text='Summarize',
        command=lambda: summarize(
            input_text,
            summary_text,
            model_entry,
            status_label,
            output_path,
            output_label,
        ),
    ).pack(side='left')
    tk.Button(btn_frame, text='Save Summary', command=lambda: save_summary(summary_text, output_path, output_label)).pack(side='left')

    root.mainloop()


if __name__ == '__main__':
    main()