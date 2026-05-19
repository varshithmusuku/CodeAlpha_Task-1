import tkinter as tk 
from tkinter import ttk, messagebox 
from deep_translator import GoogleTranslator 
import pyperclip 
 
class TranslatorApp: 
    def __init__(self, root): 
        self.root = root 
        self.root.title("Language Translation Tool - CodeAlpha") 
        self.root.geometry("600x400") 
        self.root.configure(padx=20, pady=20) 
 
        # Get supported languages 
        self.languages = GoogleTranslator().get_supported_languages() 
         
        self.create_widgets() 
 
    def create_widgets(self): 
        # --- Source Text Section --- 
        tk.Label(self.root, text="Source Language:", font=("Arial", 10, "bold")).grid(row=0, 
column=0, sticky="w") 
        self.source_lang_combo = ttk.Combobox(self.root, values=["auto"] + self.languages, 
state="readonly") 
        self.source_lang_combo.set("auto") 
        self.source_lang_combo.grid(row=0, column=1, sticky="w", pady=5) 
 
        self.source_text = tk.Text(self.root, height=6, width=65) 
        self.source_text.grid(row=1, column=0, columnspan=2, pady=5) 
 
        # --- Target Text Section --- 
        tk.Label(self.root, text="Target Language:", font=("Arial", 10, "bold")).grid(row=2, column=0, 
sticky="w") 
        self.target_lang_combo = ttk.Combobox(self.root, values=self.languages, state="readonly") 
        self.target_lang_combo.set("spanish") # Default target 
        self.target_lang_combo.grid(row=2, column=1, sticky="w", pady=5) 
 
        self.target_text = tk.Text(self.root, height=6, width=65, state="disabled") 
        self.target_text.grid(row=3, column=0, columnspan=2, pady=5) 
 
        # --- Buttons --- 
        button_frame = tk.Frame(self.root) 
        button_frame.grid(row=4, column=0, columnspan=2, pady=10) 
 
        translate_btn = tk.Button(button_frame, text="Translate", command=self.translate, 
bg="#4CAF50", fg="white", font=("Arial", 10, "bold")) 
        translate_btn.pack(side="left", padx=10) 
 
        copy_btn = tk.Button(button_frame, text="Copy Translation", 
command=self.copy_to_clipboard, bg="#2196F3", fg="white", font=("Arial", 10, "bold")) 
        copy_btn.pack(side="left", padx=10) 
 
    def translate(self): 
        text_to_translate = self.source_text.get("1.0", tk.END).strip() 
        source_lang = self.source_lang_combo.get() 
        target_lang = self.target_lang_combo.get() 
 
        if not text_to_translate: 
            messagebox.showwarning("Warning", "Please enter text to translate.") 
            return 
 
        try: 
            # Perform translation 
            translator = GoogleTranslator(source=source_lang, target=target_lang) 
            translated_text = translator.translate(text_to_translate) 
 
            # Display result 
            self.target_text.config(state="normal") 
            self.target_text.delete("1.0", tk.END) 
            self.target_text.insert(tk.END, translated_text) 
            self.target_text.config(state="disabled") 
        except Exception as e: 
            messagebox.showerror("Error", f"Translation failed: {str(e)}") 
 
    def copy_to_clipboard(self): 
        translated_text = self.target_text.get("1.0", tk.END).strip() 
        if translated_text: 
            pyperclip.copy(translated_text) 
            messagebox.showinfo("Success", "Translation copied to clipboard!") 
 
if __name__ == "__main__": 
    root = tk.Tk() 
    app = TranslatorApp(root) 
    root.mainloop()
