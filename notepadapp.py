from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

def newFile():
    global file
    root.title("Untitle - Notepad")
    file = None
    TextArea.delete(1.0, END)
def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()

def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
        if file =="":
            file = None

        else:
            #Save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()

def exitFile():
    root.destroy()


def cutFile():
    TextArea.event_generate(("<<Cut>>"))
    

def copyFile():
    TextArea.event_generate(("<<Copy>>"))

def pasteFile():
    TextArea.event_generate(("<<Paste>>"))



def about():
    showinfo("Notepad","Notepad Done By Dhrumil Panchal")

if __name__ == '__main__':
    
    #Basic tkinter setup
    root = Tk()
    root.title("Untitled - Notepad")
    root.geometry("700x400")

    #Adding text area
    TextArea = Text(root,font="lucida 13")
    file = None
    TextArea.pack(expand=TRUE,fill=BOTH)

    #Let create menubar
    MenuBar = Menu(root)
    FileMenu = Menu(MenuBar, tearoff=0)
    #To oopen new file
    FileMenu.add_command(label="New", command=newFile)
    #To open already existing file
    FileMenu.add_command(label="Open", command=openFile)
    #To save current file
    FileMenu.add_command(label="Save", command=saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit", command=exitFile)
    MenuBar.add_cascade(label="File", menu=FileMenu)


    #Edit menu start
    EditMenu = Menu(MenuBar, tearoff=0)
    #TO feature of cut
    EditMenu.add_command(label="cut", command=cutFile)
    #To feature of copy
    EditMenu.add_command(label="copy", command=copyFile)
    #To feature of paste
    EditMenu.add_command(label="paste", command=pasteFile)
    MenuBar.add_cascade(label="Edit",menu=EditMenu)

    #Help Menu start
    HelpMenu = Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label="About Notepad", command=about)
    MenuBar.add_cascade(label="Help", menu=HelpMenu)

    root.config(menu=MenuBar)

    #Adding Scrollbar
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT,fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)

    root.mainloop()
  