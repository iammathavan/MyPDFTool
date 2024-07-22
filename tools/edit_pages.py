import tkinter as tk
from tkinter.font import Font
from tkinter import filedialog, messagebox
from PyPDF2 import PdfReader, PdfWriter
from PIL import Image, ImageTk

NAVY = "#405D72"
GREY = "#758694"
BEIGE = "#F7E7DC"
WHITE = "#FFF8F3"

class EditPages:
    def __init__(self, root):
        self.root = root
        self.root.title("Edit PDF Pages")
        self.root.geometry("600x450")
        self.root.configure(bg=NAVY)
        self.root.resizable(width=False, height=False)
        
        self.pdf_file = None
        self.pages = []

        # Load and resize images
        self.pdf_icon = Image.open("../MyPDFTool-main/images/pdf-file-top.png")
        self.pdf_icon = self.pdf_icon.resize((32, 32), Image.LANCZOS)
        self.pdf_icon = ImageTk.PhotoImage(self.pdf_icon)

        self.open_icon = Image.open("../MyPDFTool-main/images/open-folder.png")
        self.open_icon = self.open_icon.resize((32, 32), Image.LANCZOS)
        self.open_icon = ImageTk.PhotoImage(self.open_icon)

        self.save_icon = Image.open("../MyPDFTool-main/images/document.png")
        self.save_icon = self.save_icon.resize((32, 32), Image.LANCZOS)
        self.save_icon = ImageTk.PhotoImage(self.save_icon)
        
        self.up_icon = Image.open("../MyPDFTool-main/images/up-arrow.png")
        self.up_icon = self.up_icon.resize((32, 32), Image.LANCZOS)
        self.up_icon = ImageTk.PhotoImage(self.up_icon)

        self.down_icon = Image.open("../MyPDFTool-main/images/down-arrow.png")
        self.down_icon = self.down_icon.resize((32, 32), Image.LANCZOS)
        self.down_icon = ImageTk.PhotoImage(self.down_icon)

        self.delete_icon = Image.open("../MyPDFTool-main/images/delete.png")
        self.delete_icon = self.delete_icon.resize((32, 32), Image.LANCZOS)
        self.delete_icon = ImageTk.PhotoImage(self.delete_icon)

        # Top frame
        top_frame = tk.Frame(self.root, bg=WHITE, height=60)
        top_frame.pack(fill=tk.X)
        
        # Top frame widgets
        left_icon = tk.Label(top_frame, image=self.pdf_icon, bg=WHITE)
        left_icon.pack(side=tk.LEFT, padx=10)
        
        title = tk.Label(top_frame, text="Edit Pages", font=Font(family="Helvetica", size=24, weight="bold"), bg=WHITE)
        title.pack(side=tk.LEFT, padx=154)
        
        right_icon = tk.Label(top_frame, image=self.pdf_icon, bg=WHITE)
        right_icon.pack(side=tk.RIGHT, padx=10)
        
        # Label for displaying "Selected Pages:"
        selected_label = tk.Label(self.root, text="Selected Pages:", font=Font(family="Helvetica", size=16), bg=NAVY, fg=WHITE)
        selected_label.pack(pady=20)
        
        # Listbox for displaying pages
        self.pages_listbox = tk.Listbox(self.root, width=70, height=10, bg=GREY, fg=WHITE, font=Font(family="Helvetica", size=12))
        self.pages_listbox.pack(pady=2)
        
        # Button frame
        button_frame = tk.Frame(self.root, bg=NAVY)
        button_frame.pack(pady=20)
        
        # Buttons
        select_button = tk.Button(button_frame, text="Open", image=self.open_icon, compound=tk.RIGHT, bg=BEIGE, activebackground=GREY, activeforeground=BEIGE, font=Font(family="Helvetica", size=16), command=self.select_pdf)
        select_button.grid(row=0, column=0, padx=15, pady=10, ipadx=10)
        
        save_button = tk.Button(button_frame, text="Save", image=self.save_icon, compound=tk.RIGHT, bg=BEIGE, activebackground=GREY, activeforeground=BEIGE, font=Font(family="Helvetica", size=16), command=self.save_pdf)
        save_button.grid(row=0, column=1, padx=15, pady=10, ipadx=10)

        up_button = tk.Button(button_frame, image=self.up_icon, compound=tk.RIGHT, font=Font(family="Helvetica", size=16), bg=BEIGE, activebackground=GREY, activeforeground=BEIGE, command=self.move_up)
        up_button.grid(row=1, column=0, ipadx=1, sticky="sw")
        
        down_button = tk.Button(button_frame, image=self.down_icon, compound=tk.RIGHT, font=Font(family="Helvetica", size=16), bg=BEIGE, activebackground=GREY, activeforeground=BEIGE, command=self.move_down)
        down_button.grid(row=1, column=1, ipadx=1, sticky="sw")

        delete_button = tk.Button(button_frame, image=self.delete_icon, compound=tk.RIGHT, font=Font(family="Helvetica", size=16), bg=BEIGE, activebackground=GREY, activeforeground=BEIGE, command=self.delete_page)
        delete_button.grid(row=1, column=2, ipadx=1, sticky="ne")

    # This function will handle opening the PDF file once the user clicks open button
    def select_pdf(self):
        file = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if file:
            self.pdf_file = file
            self.load_pdf()

    # This function will load the PDF's pages into the listbox.
    def load_pdf(self):
        reader = PdfReader(self.pdf_file)
        self.pages = list(range(len(reader.pages)))
        self.update_pages_listbox()

    # This function will render the listbox depending on the pages changed.
    def update_pages_listbox(self):
        self.pages_listbox.delete(0, tk.END)
        for i, page in enumerate(self.pages):
            self.pages_listbox.insert(tk.END, f"Page {page + 1}")

    # This function will move the selected page in the listbox, up one place, once the user presses
    # the up arrow button. Basically will replace the currently selected one with one above, and the above
    # one with the selected one. 
    def move_up(self):
        selected_index = self.pages_listbox.curselection()
        if selected_index and selected_index[0] > 0:
            index = selected_index[0]
            temp = self.pages[index]
            self.pages[index] = self.pages[index - 1]
            self.pages[index - 1] = temp
            self.update_pages_listbox()
            self.pages_listbox.selection_set(index - 1)

    # This function will move the selected page in the listbox, down one place, once the user presses
    # the down arrow button. Basically will replace the currently selected one with one below, and the below
    # one with the selected one.
    def move_down(self):
        selected_index = self.pages_listbox.curselection()
        if selected_index and selected_index[0] < len(self.pages) - 1:
            index = selected_index[0]
            temp = self.pages[index]
            self.pages[index] = self.pages[index + 1]
            self.pages[index + 1] = temp
            self.update_pages_listbox()
            self.pages_listbox.selection_set(index + 1)
    
    # This function will delete the currently selected page.
    def delete_page(self):
        selected_index = self.pages_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.pages.pop(index)
            self.update_pages_listbox()

    # This function will create a new pdf file based on the pages in the listbox, displayed, in order. Then
    # asks the user to save as where in their folder location.
    def save_pdf(self):
        if self.pdf_file:
            save_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
            if save_path:
                writer = PdfWriter()
                reader = PdfReader(self.pdf_file)
                for page in self.pages:
                    writer.add_page(reader.pages[page])
                with open(save_path, "wb") as f:
                    writer.write(f)
                messagebox.showinfo("Success", "PDF pages rearranged and saved successfully!")
        else:
            messagebox.showwarning("Warning", "No PDF selected!")

if __name__ == "__main__":
    root = tk.Tk()
    app = EditPages(root)
    root.mainloop()
