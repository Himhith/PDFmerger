import tkinter as tk
from tkinter import filedialog, Text, Toplevel, StringVar
import tkinter.ttk
from tkinter.ttk import Label
import PyPDF2
from pathlib import Path

##TODO: 
## MAYBE: Choose what exact  pages to stich 
## layout more everything nicely 

WIDTH = 400
HEIGHT = 300
WINDOW_DIMENSIONS = f"{WIDTH}x{HEIGHT}"
BG_COLOR = "grey"
FRAME_BG = "white"
FONT_COLOR = "black"
MARGIN = 25
 
def find_pdf(listframe):
    filename= filedialog.askopenfilename(initialdir=".",
     title="Select a PDF",
     filetypes=(("pdf","*.pdf",),("all files","*.*")))  ##store and open last opend dir??
    label=tk.Label(listframe, text=Path(filename).stem)
    label.pack()
    pdfs.append(filename) ##filename is given with path 
    print(pdfs)

def merge_pdf(name='merged.pdf'):
    if not name.endswith('.pdf'):
        name += '.pdf'
    with open (name,'wb') as out_file:
        merger= PyPDF2.PdfFileMerger()
        for pdf in pdfs:
            with open (pdf,'rb') as p1:
                merger.append(PyPDF2.PdfFileReader(p1))     
        merger.write(out_file)

def open_new_window():  
    new_window_ = Toplevel(root) 
    new_window_.title("Name merged file")  
    new_window_.geometry("200x400") 
    merged_pdf_name = StringVar()
    name = tk.Entry(new_window_, textvariable=merged_pdf_name)
    name.pack()
    Label(new_window_,  
          text = name.get()).pack()
    button_test_name = tk.Button(new_window_, text="check",
        command = lambda: print(name.get())).pack()
    merge_pdf_button = tk.Button(new_window_, text="MERGE",fg=FONT_COLOR,
    command =lambda: merge_pdf(name.get()))
    merge_pdf_button.pack()


 


root = tk.Tk() ## initialization
pdfs = [] ##Array of PDFS PATHS

root.geometry(WINDOW_DIMENSIONS)


master_frame = tk.Frame(root,bg=BG_COLOR)
master_frame.place(width=WIDTH, height=HEIGHT)
optionframe = tk.Frame(master_frame,bg=FRAME_BG)
optionframe.place(width=WIDTH/3 , height=HEIGHT/1.5, x= MARGIN, rely=0.05)
frame = tk.Frame(master_frame,bg=FRAME_BG)
frame.place(width=WIDTH/2 , height=HEIGHT/2, x= WIDTH/2 - MARGIN , rely=0.05)
Label(
    optionframe,
    text =" Actions ").pack()
Label(
    frame,  
    text ="Files Choosen:").pack()
add_file_button= tk.Button(
    optionframe,
    text="Add a PDF",fg=FONT_COLOR,
    command= lambda: find_pdf(frame))
add_file_button.pack()
new_window_button = tk.Button(
    optionframe,
    text="MERGE PDFS",
    fg=FONT_COLOR,
    command=open_new_window)

new_window_button.pack()


root.mainloop() 



