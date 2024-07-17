import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
from PIL import Image, ImageTk
import subprocess


NAVY = "#405D72"
GREY = "#758694"
BEIGE = "#F7E7DC"
WHITE = "#FFF8F3"

class myPDFTool:
    def __init__(self, root):
        # Set the main frame
        self.root = root
        self.root.title("MyPDF Tools")
        self.root.geometry("600x400")
        self.root.configure(bg=NAVY)
        self.root.resizable(width=False, height=False)
        
        # Load and resize images
        self.pdf_icon = Image.open("./images/pdf-file-top.png")
        self.pdf_icon = self.pdf_icon.resize((32, 32), Image.LANCZOS)
        self.pdf_icon = ImageTk.PhotoImage(self.pdf_icon)

        self.merge_icon = Image.open("./images/file.png")
        self.merge_icon = self.merge_icon.resize((32, 32), Image.LANCZOS)
        self.merge_icon = ImageTk.PhotoImage(self.merge_icon)
                    

        self.pdf_to_image_icon = Image.open("./images/photo.png")
        self.pdf_to_image_icon = self.pdf_to_image_icon.resize((32, 32), Image.LANCZOS)
        self.pdf_to_image_icon = ImageTk.PhotoImage(self.pdf_to_image_icon)

        self.image_to_pdf_icon = Image.open("./images/pdf-file.png")
        self.image_to_pdf_icon = self.image_to_pdf_icon.resize((32, 32), Image.LANCZOS)
        self.image_to_pdf_icon = ImageTk.PhotoImage(self.image_to_pdf_icon)

        self.alter_icon = Image.open("./images/document.png")
        self.alter_icon = self.alter_icon.resize((32, 32), Image.LANCZOS)
        self.alter_icon = ImageTk.PhotoImage(self.alter_icon)
        
        # Top frame
        top_frame = tk.Frame(self.root, bg=WHITE, height=60)
        top_frame.pack(fill=tk.X)
        
        # Top frame widgets
        left_icon = tk.Label(top_frame, image=self.pdf_icon, bg=WHITE)
        left_icon.pack(side=tk.LEFT, padx=10)
        
        title = tk.Label(top_frame, text="MyPDF Tools", font=Font(family="Helvetica", size=24, weight="bold"), bg=WHITE)
        title.pack(side=tk.LEFT, padx=136)
        
        right_icon = tk.Label(top_frame, image=self.pdf_icon, bg=WHITE)
        right_icon.pack(side=tk.RIGHT, padx=10)
        
        # Button frame
        button_frame = tk.Frame(self.root, bg=NAVY)
        button_frame.pack(pady=20)
        
        # Buttons
        merge_btn = tk.Button(button_frame, text="Merge PDFs", image=self.merge_icon, compound=tk.RIGHT, font=Font(family="Helvetica", size=16), bg=BEIGE, activebackground=GREY, activeforeground=BEIGE, command=self.merge_pdfs, padx=10)
        merge_btn.pack(pady=10, ipadx=10, ipady=10, fill=tk.X)
        
        pdf_to_image_btn = tk.Button(button_frame, text="PDFs To Images", image=self.pdf_to_image_icon, compound=tk.RIGHT, padx=10, font=Font(family="Helvetica", size=16), bg=BEIGE, activebackground=GREY, activeforeground=BEIGE, command=self.pdf_to_image)
        pdf_to_image_btn.pack(pady=10, ipadx=10, ipady=10, fill=tk.X)
        
        image_to_pdf_btn = tk.Button(button_frame, text="Image To PDF", image=self.image_to_pdf_icon, compound=tk.RIGHT, padx=10, font=Font(family="Helvetica", size=16), bg=BEIGE, activebackground=GREY, activeforeground=BEIGE, command=self.image_to_pdf)
        image_to_pdf_btn.pack(pady=10, ipadx=10, ipady=10, fill=tk.X)
        
        alter_btn = tk.Button(button_frame, text="Alter Pages", image=self.alter_icon, compound=tk.RIGHT, padx=10, font=Font(family="Helvetica", size=16), bg=BEIGE, activebackground=GREY, activeforeground=BEIGE, command=self.alter_pages)
        alter_btn.pack(pady=10, ipadx=10, ipady=10, fill=tk.X)
        
    def merge_pdfs(self):
        subprocess.Popen(["python", "./tools/merge_pdf.py"])

    def pdf_to_image(self):
        subprocess.Popen(["python", "./tools/pdf2img.py"])

    def image_to_pdf(self):
        # Image to PDF functionality
        pass

    def alter_pages(self):
        # Alter pages functionality
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = myPDFTool(root)
    root.mainloop()
