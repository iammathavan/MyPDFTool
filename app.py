import tkinter as tk
import tkinter.font as tkFont
from tkinter import filedialog
import img2pdf
from tkinter import messagebox
import os
import PyPDF2

class App:
    def __init__(self, root):
        #Setting the title
        root.title("My PDF Tool")
        #Setting the window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        root.configure(background="#272829")

        #Store the order of the pages that the user entered in the entry. I.E. 2-1-4-3
        self.pages = tk.StringVar()

        # The Main label at the top of the application
        mainLabel=tk.Label(root)
        mainLabel["activebackground"] = "#272829"
        mainLabel["activeforeground"] = "#272829"
        ft = tkFont.Font(family='Helvetica',size=20, weight='bold')
        mainLabel["font"] = ft
        mainLabel["fg"] = "#FFF6E0"
        mainLabel["bg"] = "#272829"
        mainLabel["justify"] = "center"
        mainLabel["text"] = "Image to PDF"
        mainLabel.place(x=210,y=10,width=206,height=71)

        # The Listbox that displays all the images that were selected to convert into PDF (in order)
        self.displayImages = tk.Listbox(root)
        ft = tkFont.Font(family='Helvetica',size=10)
        self.displayImages["font"] = ft
        self.displayImages["fg"] = "#FFF6E0"
        self.displayImages["bg"] = "#272829"
        self.displayImages["justify"] = "left"
        self.displayImages.insert(1, "Images: None Selected")
        self.displayImages.place(x=100,y=100,width=400,height=50)

        # Select Images Button 
        selImageBtn=tk.Button(root)
        ft = tkFont.Font(family='Helvetica',size=12)
        selImageBtn["font"] = ft
        selImageBtn["fg"] = "#FFF6E0"
        selImageBtn["bg"] = "#61677A"
        selImageBtn["justify"] = "center"
        selImageBtn["text"] = "Select Images"
        selImageBtn.place(x=150,y=225,width=150,height=50)
        selImageBtn["command"] = self.selImageBtn_command

        # Label that displays the selected PDF
        self.displayPDF=tk.Label(root)
        ft = tkFont.Font(family='Helvetica',size=10)
        self.displayPDF["font"] = ft
        self.displayPDF["fg"] = "#FFF6E0"
        self.displayPDF["bg"] = "#272829"
        self.displayPDF["justify"] = "left"
        self.displayPDF["text"] = "PDF: None Selected"
        self.displayPDF.place(x=100,y=170,width=400,height=30)

        # Button that will convert Images to PDF
        convertBtn=tk.Button(root)
        ft = tkFont.Font(family='Helvetica',size=12)
        convertBtn["font"] = ft
        convertBtn["fg"] = "#272829"
        convertBtn["bg"] = "#D8D9DA"
        convertBtn["justify"] = "center"
        convertBtn["text"] = "Convert"
        convertBtn.place(x=325,y=225,width=150,height=50)
        convertBtn["command"] = self.convertBtn_command

        # Entry to get the user's order in which they want to alter the pages into
        pagesEntry=tk.Entry(root)
        pagesEntry["borderwidth"] = "2px"
        ft = tkFont.Font(family='Helvetica',size=14)
        pagesEntry["font"] = ft
        pagesEntry["fg"] = "#61677A"
        pagesEntry["bg"] = "#D8D9DA"
        pagesEntry["justify"] = "left"
        pagesEntry["text"] = "Entry"
        pagesEntry["textvariable"] = self.pages
        pagesEntry.place(x=150,y=310,width=250,height=60)
        pagesEntry.insert(0, 'E.G 1-2-3-4')

        # Button to select the PDF they want to alter the order of
        selPDFBtn=tk.Button(root)
        ft = tkFont.Font(family='Helvetica',size=10)
        selPDFBtn["font"] = ft
        selPDFBtn["fg"] = "#FFF6E0"
        selPDFBtn["bg"] = "#61677A"
        selPDFBtn["justify"] = "center"
        selPDFBtn["text"] = "Select PDF"
        selPDFBtn.place(x=400,y=310,width=75,height=30)
        selPDFBtn["command"] = self.selPDFBtn_command

        # Button to alter the order of pages of the selected PDF
        alterBtn=tk.Button(root)
        ft = tkFont.Font(family='Helvetica',size=10)
        alterBtn["font"] = ft
        alterBtn["fg"] = "#272829"
        alterBtn["bg"] = "#D8D9DA"
        alterBtn["justify"] = "center"
        alterBtn["text"] = "Alter"
        alterBtn.place(x=400,y=340,width=75,height=30)
        alterBtn["command"] = self.alterBtn_command

    # This function will get the relative path of an absolute path.
    @staticmethod
    def getRelativePath(absolutePath):
        curDirectory = os.getcwd()
        relativePath = os.path.relpath(absolutePath, curDirectory)
        return relativePath

    # This function will open the images in file, store it in a global variable imgNames,
    # reset the displayImages Listbox, and then diplay the new images in displayImages Listbox
    def selImageBtn_command(self):
        global imgNames
        imgNames = filedialog.askopenfilenames(initialdir="images", title="Select Images", filetypes=[('jpg images', '*.jpg')])
        self.displayImages.delete(0, tk.END)
        count = 1
        for i in imgNames:
            self.displayImages.insert(count, i)
            count += 1

    # This function will convert the images to a single pdf, and will ask the user to where 
    # to save the newly created pdf 
    def convertBtn_command(self):
        try:
            saveFile = filedialog.asksaveasfilename(initialdir="./", title="Save File", filetypes=[('PDF Files', '*.pdf')])
            if not saveFile.endswith(".pdf"):
                saveFile += ".pdf"
            with open(saveFile, "wb") as pdf:
                pdf.write(img2pdf.convert(imgNames))
            pdf.close()
        except:
            messagebox.showerror("File Opening Error", "Make sure to select the correct images before converting")

    # This function ask the user to select a pdf that they want to alter the order of the pages,
    # save the pdf in a global variable called pdfName, get the relative path of the pdf so it
    # will be displayed on the displayPDF Label in a short form. 
    def selPDFBtn_command(self):
        try:
            global pdfName
            pdfName = filedialog.askopenfilenames(initialdir="./", title="Select PDF", filetypes=[('pdf file', '*.pdf')])
            self.displayPDF.config(text="PDF: " + self.getRelativePath(pdfName[0]))
        except:
            messagebox.showerror("File Opening Error", "Make sure to select the correct pdf before altering the order")

    # This function get the list of pages from the Entry, clean up the formatted numbers, create a new pdf 
    # with the order specified, ask the user where and what to save as the newly created pdf
    def alterBtn_command(self):
        try:
            thePages = list(self.pages.get())
            pagesExtracted = []
            for c in thePages:
                if c != '-' and c.isnumeric():
                    pagesExtracted.append(c)
            merger = PyPDF2.PdfWriter()
            pdfFile = open(pdfName[0], "rb")
            pdfReader = PyPDF2.PdfReader(pdfFile)
            if len(pdfReader.pages) == len(pagesExtracted):
                for i in range(len(pagesExtracted)):
                    merger.merge(position=i+1, fileobj=pdfFile, pages=(int(pagesExtracted[i]) - 1,  int(pagesExtracted[i])))
                saveFile = filedialog.asksaveasfilename(initialdir="./", title="Save File", filetypes=[('PDF Files', '*.pdf')])
                if not saveFile.endswith(".pdf"):
                    saveFile += ".pdf"
                outPut = open(saveFile, "wb")
                merger.write(outPut)
                outPut.close()
            else:
                messagebox.showerror("Input error", "Your input do not match the number of pages on the PDF")
            merger.close()
            pdfFile.close()
        except:
            messagebox.showerror("File re-ordering error", "Make sure to select the correct PDF before altering the order")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
