import tkinter as tk
from tkinter import filedialog, Text
from tkinter import * 
from tkinter.ttk import *
from pathlib import Path
import PyPDF2

##TODO 
## MAYBE: Choose what pages to stich 
##layout everything nicely 
##mayke try blocks and idiotproof

root=tk.Tk() ## like Head for html 
pdfs = [] ##Array of PDFS PATHS
root.geometry("350x300")

def addPdf(listframe):
	filename= filedialog.askopenfilename(initialdir=".",
	 title="Select a PDF",
	 filetypes=(("pdf","*.pdf",),("all files","*.*")))  ##store and open last opend dir??
	label=tk.Label(listframe, text=Path(filename).stem)
	label.pack()
	pdfs.append(filename) ##filename is given with path 
	print(pdfs)
def mergePDF(name='merged.pdf'):
	with open (name,'wb') as out_file:
		merger= PyPDF2.PdfFileMerger()
		for pdf in pdfs:
			with open (pdf,'rb') as p1:
				merger.append(PyPDF2.PdfFileReader(p1))		
		merger.write(out_file)
def openNewWindow(): 
      
    newWindow = Toplevel(root) 
    newWindow.title("Name merged file")  
    newWindow.geometry("200x400") 
    MergedPdfName = StringVar()
    name = tk.Entry(newWindow, textvariable=MergedPdfName)
    name.pack()
    Label(newWindow,  
          text =name.get()).pack()
    buttonTestName=tk.Button(newWindow, text="check",
    	command= lambda: print(name.get())).pack()
    mergePDFButton= tk.Button(newWindow, text="MERGE",fg="green",
    command=lambda: mergePDF(name.get()))
    mergePDFButton.pack()

# canvas = tk.Canvas(root, relheight=1, relwidth=1, bg="white")
# canvas.pack()
masterFrame=tk.Frame(root,bg="grey")
masterFrame.place(width=350, height=300)
optionframe= tk.Frame(masterFrame,bg="white")
optionframe.place(width=100 , height=200,x=25, rely=0.05)
frame= tk.Frame(masterFrame,bg="white")
frame.place(width=175 , height=200, x= 150 , rely=0.05)
Label(optionframe,  
          text =" Actions ").pack()
Label(frame,  
          text ="Files Choosen:").pack()
addFileButton= tk.Button(optionframe, text="Add a PDF",fg="green",
 command= lambda: addPdf(frame))
addFileButton.pack()
newWindowButton= tk.Button(optionframe, text="MERGE PDFS",fg="green",
 command=openNewWindow)
newWindowButton.pack()
#mergePDFButton.pack()
root.mainloop() 


