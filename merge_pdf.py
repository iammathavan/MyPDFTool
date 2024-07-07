import tkinter as tk
from tkinter.font import Font
from tkinter import filedialog
import PyPDF2

NAVY = "#405D72"
GREY = "#758694"
BEIGE = "#F7E7DC"
WHITE = "#FFF8F3"

class MergePDFsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Merge PDFs")
        self.root.geometry("400x300")
        self.root.configure(bg=NAVY)
        
        self.selected_files = []
        
        # GUI setup
        self.label = tk.Label(root, text="Merge PDFs", font=Font(family="Helvetica", size=24, weight="bold"), bg=NAVY, fg=WHITE)
        self.label.pack(pady=10)
        
        self.select_button = tk.Button(root, text="Select PDFs", font=Font(family="Helvetica", size=16), command=self.select_pdfs)
        self.select_button.pack(pady=10)
        
        self.merge_button = tk.Button(root, text="Merge", font=Font(family="Helvetica", size=16), command=self.merge_pdfs)
        self.merge_button.pack(pady=10)
        
    def select_pdfs(self):
        files = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])
        self.selected_files = list(files)
    
    def merge_pdfs(self):
        if self.selected_files:
            pdf_writer = PyPDF2.PdfWriter()
            for pdf in self.selected_files:
                pdf_reader = PyPDF2.PdfReader(pdf)
                for page_num in range(len(pdf_reader.pages)):
                    page = pdf_reader.pages[page_num]
                    pdf_writer.add_page(page)
            
            save_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
            if save_path:
                with open(save_path, "wb") as out_file:
                    pdf_writer.write(out_file)
                tk.messagebox.showinfo("Success", "PDFs merged successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = MergePDFsApp(root)
    root.mainloop()
