from docx2pdf import convert
from tkinter import *
from tkinter.filedialog import *

root = Tk()
filez = []
def openFile():
    global filez
    filez = askopenfilenames(title='Choose a file')
    if len(filez) != 0:
        for i in range(len(filez)):
            convert(filez[i])
    print('done')

def buttons_widget():
    myButton = Button(root, text="Import File", command=openFile)
    myButton.pack()


buttons_widget()



root.mainloop()


# convert("input.docx", "output.pdf")
# convert("my_docx_folder/")