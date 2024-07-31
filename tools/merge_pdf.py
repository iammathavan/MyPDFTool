import tkinter as tk
from tkinter.font import Font
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import PyPDF2

NAVY = "#405D72"
GREY = "#758694"
BEIGE = "#F7E7DC"
WHITE = "#FFF8F3"

class MergePDFs:
    def __init__(self, root):
        self.root = root
        self.root.title("Merge PDFs")
        self.root.geometry("600x450")
        self.root.configure(bg=NAVY)
        self.root.resizable(width=False, height=False)
        
        self.selected_files = []

        
        # Load and resize images
        self.pdf_icon = Image.open("../MyPDFTool-main/images/pdf-file-top.png")
        self.pdf_icon = self.pdf_icon.resize((32, 32), Image.LANCZOS)
        self.pdf_icon = ImageTk.PhotoImage(self.pdf_icon)

        self.open_icon = Image.open("../MyPDFTool-main/images/open-folder.png")
        self.open_icon = self.open_icon.resize((32, 32), Image.LANCZOS)
        self.open_icon = ImageTk.PhotoImage(self.open_icon)

        self.merge_icon = Image.open("../MyPDFTool-main/images/file.png")
        self.merge_icon = self.merge_icon.resize((32, 32), Image.LANCZOS)
        self.merge_icon = ImageTk.PhotoImage(self.merge_icon)
        
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
        
        title = tk.Label(top_frame, text="Merge PDFs", font=Font(family="Helvetica", size=24, weight="bold"), bg=WHITE)
        title.pack(side=tk.LEFT, padx=154)
        
        right_icon = tk.Label(top_frame, image=self.pdf_icon, bg=WHITE)
        right_icon.pack(side=tk.RIGHT, padx=10)
        
        # Label for displaying "Selected PDFs:"
        selected_label = tk.Label(self.root, text="Selected PDFs:", font=Font(family="Helvetica", size=16), bg=NAVY, fg=WHITE)
        selected_label.pack(pady=20)
        
        # Listbox for displaying selected files
        self.file_listbox = tk.Listbox(self.root, width=70, height=10, bg=GREY, fg=WHITE, font=Font(family="Helvetica", size=12))
        self.file_listbox.pack(pady=2)
        
        # Button frame
        button_frame = tk.Frame(self.root, bg=NAVY)
        button_frame.pack(pady=20)
        
        # Buttons
        select_button = tk.Button(button_frame, text="Open", image=self.open_icon, compound=tk.RIGHT, bg=BEIGE, activebackground=GREY, activeforeground=BEIGE, font=Font(family="Helvetica", size=16), command=self.select_pdfs)
        select_button.grid(row=0, column=0, padx=15, pady=10, ipadx=10)
        
        merge_button = tk.Button(button_frame, text="Merge", image=self.merge_icon, compound=tk.RIGHT, bg=BEIGE, activebackground=GREY, activeforeground=BEIGE, font=Font(family="Helvetica", size=16), command=self.merge_pdfs)
        merge_button.grid(row=0, column=1, padx=15, pady=10, ipadx=10)

        up_button = tk.Button(button_frame, image=self.up_icon, compound=tk.RIGHT, font=Font(family="Helvetica", size=16), bg=BEIGE, activebackground=GREY, activeforeground=BEIGE, command=self.move_up)
        up_button.grid(row=1, column=0, ipadx=1, sticky="sw")
        
        down_button = tk.Button(button_frame, image=self.down_icon, compound=tk.RIGHT, font=Font(family="Helvetica", size=16), bg=BEIGE, activebackground=GREY, activeforeground=BEIGE, command=self.move_down)
        down_button.grid(row=1, column=1, ipadx=1, sticky="sw")

        delete_button = tk.Button(button_frame, image=self.delete_icon, compound=tk.RIGHT, font=Font(family="Helvetica", size=16), bg=BEIGE, activebackground=GREY, activeforeground=BEIGE, command=self.delete_file)
        delete_button.grid(row=1, column=2, ipadx=1, sticky="ne")
        
    # This function will handle opening the pdf files once the user clicks open button and 
    # then update the listbox.
    def select_pdfs(self):
        files = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])
        self.selected_files = list(files)
        self.update_file_listbox()
    
    # This function will clear the listbox and adds the PDF files based on the selected_files.
    def update_file_listbox(self):
        self.file_listbox.delete(0, tk.END)
        for file in self.selected_files:
            self.file_listbox.insert(tk.END, file)

    # This function will move the selected PDF file in the listbox, up one place, once the user presses
    # the up arrow button. Basically will replace the currently selected one with one above, and the above
    # one with the selected one. 
    def move_up(self):
        selected_index = self.file_listbox.curselection()
        if selected_index and selected_index[0] > 0:
            index = selected_index[0]
            temp = self.selected_files[index]
            self.selected_files[index] = self.selected_files[index - 1]
            self.selected_files[index - 1] = temp
            self.update_file_listbox()
            self.file_listbox.selection_set(index - 1)
    
    # This function will move the selected PDF file in the listbox, down one place, once the user presses
    # the down arrow button. Basically will replace the currently selected one with one below, and the below
    # one with the selected one.
    def move_down(self):
        selected_index = self.file_listbox.curselection()
        if selected_index and selected_index[0] < len(self.selected_files) - 1:
            index = selected_index[0]
            temp = self.selected_files[index] 
            self.selected_files[index] = self.selected_files[index + 1]
            self.selected_files[index + 1] = temp
            self.update_file_listbox()
            self.file_listbox.selection_set(index + 1)

    # This function will delete the currently selected PDF file.
    def delete_file(self):
        selected_index = self.file_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.selected_files.pop(index)
            self.update_file_listbox()
    
    # This function handles the merging of all selected PDF files. Using PyPDF2 library, it will
    # create a new pdf file with each page added in the order it is selected. Asks user where to 
    # save the newly created PDF. 
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
                messagebox.showinfo("Success", "PDFs merged successfully!")
        else:
            messagebox.showwarning("Warning", "No PDFs selected!")

if __name__ == "__main__":
    root = tk.Tk()
    app = MergePDFs(root)
    root.mainloop()
