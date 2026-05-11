from tkinter import *
from tkinter import ttk, messagebox
import googletrans

root = Tk()
root.title("Google Translator")
root.geometry("1080x450")
root.configure(bg="white")

# Icon (optional - won't crash if file is missing)
try:
    image_icon = PhotoImage(file="google.png")
    root.iconphoto(False, image_icon)
except Exception:
    pass

# Language data
language = googletrans.LANGUAGES                  # {code: name, ...}
languageV = [name.capitalize() for name in language.values()]
languageK = list(language.keys())

def get_lang_code(name):
    """Return the language code matching the given display name."""
    name_lower = name.lower()
    for code, lang_name in language.items():
        if lang_name.lower() == name_lower:
            return code
    return "auto"

# ── Top bar ──────────────────────────────────────────────────────────────────
Label(root, text="From:", font="Roboto 12 bold", bg="white").place(x=20, y=22)

combo1 = ttk.Combobox(root, values=languageV, font="Roboto 13", state="readonly", width=22)
combo1.place(x=70, y=20)
combo1.set("English")

# Swap button
def swap_languages():
    src = combo1.get()
    dst = combo2.get()
    combo1.set(dst)
    combo2.set(src)
    # Also swap the text boxes
    t1 = text1.get("1.0", END).strip()
    t2 = text2.get("1.0", END).strip()
    text1.delete("1.0", END)
    text1.insert("1.0", t2)
    text2.delete("1.0", END)
    text2.insert("1.0", t1)

btn_swap = Button(root, text="⇄", font="Roboto 14 bold", bg="#4285F4", fg="white",
                  relief=FLAT, cursor="hand2", command=swap_languages, padx=8)
btn_swap.place(x=310, y=16)

Label(root, text="To:", font="Roboto 12 bold", bg="white").place(x=365, y=22)

combo2 = ttk.Combobox(root, values=languageV, font="Roboto 13", state="readonly", width=22)
combo2.place(x=395, y=20)
combo2.set("Select language")

# ── Text areas ────────────────────────────────────────────────────────────────
Label(root, text="Enter Text", font="Roboto 13 bold", bg="white", fg="#333").place(x=20, y=65)

text1 = Text(root, font="Roboto 14", wrap=WORD, relief=GROOVE, bd=2, undo=True)
text1.place(x=20, y=90, width=490, height=270)

# Scrollbar for input
sb1 = Scrollbar(root, command=text1.yview)
sb1.place(x=510, y=90, height=270)
text1.config(yscrollcommand=sb1.set)

Label(root, text="Translated Text", font="Roboto 13 bold", bg="white", fg="#333").place(x=560, y=65)

text2 = Text(root, font="Roboto 14", wrap=WORD, relief=GROOVE, bd=2, state=DISABLED, bg="#f9f9f9")
text2.place(x=560, y=90, width=490, height=270)

# Scrollbar for output
sb2 = Scrollbar(root, command=text2.yview)
sb2.place(x=1050, y=90, height=270)
text2.config(yscrollcommand=sb2.set)

# ── Translate logic ───────────────────────────────────────────────────────────
def Translate():
    src_name = combo1.get()
    dst_name = combo2.get()

    if dst_name.lower() in ("select language", ""):
        messagebox.showwarning("Select Language", "Please select a destination language.")
        return

    text_ = text1.get("1.0", END).strip()
    if not text_:
        messagebox.showwarning("Empty Input", "Please enter some text to translate.")
        return

    src_code = get_lang_code(src_name)
    dst_code = get_lang_code(dst_name)

    try:
        translator = googletrans.Translator()
        translation = translator.translate(text_, src=src_code, dest=dst_code)
        text2.config(state=NORMAL)
        text2.delete("1.0", END)
        text2.insert("1.0", translation.text)
        text2.config(state=DISABLED)

        # Show detected source language if "auto"
        if src_code == "auto" and translation.src:
            detected = language.get(translation.src, translation.src).capitalize()
            combo1.set(detected)
    except Exception as e:
        messagebox.showerror("Translation Error", f"Could not translate.\n\n{e}")

def clear_all():
    text1.delete("1.0", END)
    text2.config(state=NORMAL)
    text2.delete("1.0", END)
    text2.config(state=DISABLED)

def copy_translation():
    result = text2.get("1.0", END).strip()
    if result:
        root.clipboard_clear()
        root.clipboard_append(result)
        messagebox.showinfo("Copied", "Translation copied to clipboard!")

# ── Buttons ───────────────────────────────────────────────────────────────────
btn_translate = Button(root, text="Translate", font="Roboto 13 bold",
                       bg="#4285F4", fg="white", relief=FLAT,
                       cursor="hand2", command=Translate, padx=20, pady=6)
btn_translate.place(x=20, y=380)

btn_clear = Button(root, text="Clear", font="Roboto 13",
                   bg="#EA4335", fg="white", relief=FLAT,
                   cursor="hand2", command=clear_all, padx=20, pady=6)
btn_clear.place(x=160, y=380)

btn_copy = Button(root, text="Copy Result", font="Roboto 13",
                  bg="#34A853", fg="white", relief=FLAT,
                  cursor="hand2", command=copy_translation, padx=20, pady=6)
btn_copy.place(x=280, y=380)

# Keyboard shortcut: Ctrl+Enter to translate
root.bind("<Control-Return>", lambda e: Translate())

root.mainloop()