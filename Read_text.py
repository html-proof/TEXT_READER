from tkinter import *
import PyPDF4
from tkinter import filedialog
import pyttsx3

root =Tk()
root.geometry("400x100")

txt1 =IntVar()

def open():
	file = filedialog.askopenfilename(title="Select a PDF", filetype=(("PDF    Files", "*.pdf"), ("All Files", "*.*")))
	if file:
			pdfReader = PyPDF4.PdfFileReader(file)

			# printing number of pages in pdf file
			print(pdfReader.numPages)

			# creating a page object
			pageObj = pdfReader.getPage(txt1.get())

			# extracting text from page
			txt3=pageObj.extractText()
			print(pageObj.extractText())

			txt =pyttsx3.init()
			txt.say(txt3)
			txt.runAndWait()


bt1_open =Button(root,text="Select the file and automatic speak",command =open)
lbl =Label(root,text="input the page to speak")
lbl2 =Entry(root,textvariable =txt1)
lbl.pack()
lbl2.pack()
bt1_open.pack()
root.mainloop()