from tkinter import *
from tkinter import tkk,messagebox
import googletrans
import textblob

root=Tk()
root.title("Google Translator")
root.geometry("1080x400")

#icon
image_icon=PhotoImage(file="google.png")
root.iconphoto(False,image_icon)

language=googletrans.LANGUAGES
languageV=list(language.values())
lang1=language.keys()

combo1=ttk.Combobox(root,values=languageV,font="Roboto 14",state="r")
combo1.place(x=110,y=20)
combo1.set("ENGLISH")

combo2=ttk.Combobox(root,values=languageV,font="Roboto 14",state="r")
combo2.place(x=350,y=20)
combo2.set("SELECT LANGUAGE")

Label2=Label(root,text="Enter Text",font="Roboto 15 bold",bg="white").place(x=20,y=100)
text1=Text(root,font="Roboto 20",wrap=WORD,relief=GROOVE,bd=2)
text1.place(x=20,y=140,width=450,height=210)
Label3=Label(root,text="Translated Text",font="Roboto 15 bold",bg="white").place(x=500,y=100)
text2=Text(root,font="Roboto 20",wrap=WORD,relief=GROOVE,bd=2)
text2.place(x=500,y=140,width=450,height=210)
def Translate():
    text_=text1.get(1.0,END)
    t1=googletrans.Translator()
    translation=t1.translate(text_,src=combo1.get(),dest=combo2.get())
    text2.delete(1.0,END)
    text2.insert(1.0,translation.text)



root.configure(bg="white")
root.mainloop()






