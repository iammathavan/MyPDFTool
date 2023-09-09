
# MyPDFTool

A graphical user interface (GUI) application built using the Tkinter library in Python. The application is titled "My PDF Tool" and serves as a tool for converting images to PDF and altering the order of pages in an existing PDF.

<img width="450" alt="image" src="https://github.com/iammathavan/MyPDFTool/assets/78320266/a5665407-dd6c-4c45-b6ba-45cd40e88c93">


## Features

* Convert multiple JPG images to a single PDF file.

* Rearrange the pages of an existing PDF file by specifying the order of pages.

* User-friendly GUI for easy interaction.


## How To Use


1. Clone the repository or download the code files.

2. Install the required libraries if you haven't already:

```
pip install -r requirements.txt
```

3. Run the script:

```
python app.py
```

4. The application window will open, allowing you to perform the following actions:

* **Select Images:** Click the "Select Images" button to choose multiple JPG images from your system. The selected image filenames will be displayed in the listbox below the button.

* **Select PDF:** an existing PDF file from your system. The selected PDF filename will be displayed as a relative path below the button.

* **Convert:** Click the "Convert" button to convert the selected JPG images into a single PDF file. A "Save As" dialog will appear, allowing you to specify the output PDF file's location and name.

* **Alter:** Enter page numbers in the format "1-3-5" in the entry widget and click the "Alter" button to rearrange the pages of the selected PDF file based on the specified order.






## Documentation

[tkinter library](https://docs.python.org/3/library/tkinter.html)

[image2pdf](https://pypi.org/project/img2pdf/)

[pyPDF2](https://pypi.org/project/PyPDF2/)


