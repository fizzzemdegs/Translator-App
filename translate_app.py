from pathlib import Path
from tkinter import *
from googletrans import Translator

translator = Translator()
lang={'af': 'afrikaans', 'sq': 'albanian', 'am': 'amharic', 'ar': 'arabic', 'hy': 'armenian', 'az': 'azerbaijani', 'eu': 'basque', 'be': 'belarusian', 'bn': 'bengali', 'bs': 'bosnian', 'bg': 'bulgarian', 'ca': 'catalan', 'ceb': 'cebuano', 'ny': 'chichewa', 'zh-cn': 'chinese (simplified)', 'zh-tw': 'chinese (traditional)', 'co': 'corsican', 'hr': 'croatian', 'cs': 'czech', 'da': 'danish', 'nl': 'dutch', 'en': 'english', 'eo': 'esperanto', 'et': 'estonian', 'tl': 'filipino', 'fi': 'finnish', 'fr': 'french', 'fy': 'frisian', 'gl': 'galician', 'ka': 'georgian', 'de': 'german', 'el': 'greek', 'gu': 'gujarati', 'ht': 'haitian creole', 'ha': 'hausa', 'haw': 'hawaiian', 'iw': 'hebrew', 'he': 'hebrew', 'hi': 'hindi', 'hmn': 'hmong', 'hu': 'hungarian', 'is': 'icelandic', 'ig': 'igbo', 'id': 'indonesian', 'ga': 'irish', 'it': 'italian', 'ja': 'japanese', 'jw': 'javanese', 'kn': 'kannada', 'kk': 'kazakh', 'km': 'khmer', 'ko': 'korean', 'ku': 'kurdish (kurmanji)', 'ky': 'kyrgyz', 'lo': 'lao', 'la': 'latin', 'lv': 'latvian', 'lt': 'lithuanian', 'lb': 'luxembourgish', 'mk': 'macedonian', 'mg': 'malagasy', 'ms': 'malay', 'ml': 'malayalam', 'mt': 'maltese', 'mi': 'maori', 'mr': 'marathi', 'mn': 'mongolian', 'my': 'myanmar (burmese)', 'ne': 'nepali', 'no': 'norwegian', 'or': 'odia', 'ps': 'pashto', 'fa': 'persian', 'pl': 'polish', 'pt': 'portuguese', 'pa': 'punjabi', 'ro': 'romanian', 'ru': 'russian', 'sm': 'samoan', 'gd': 'scots gaelic', 'sr': 'serbian', 'st': 'sesotho', 'sn': 'shona', 'sd': 'sindhi', 'si': 'sinhala', 'sk': 'slovak', 'sl': 'slovenian', 'so': 'somali', 'es': 'spanish', 'su': 'sundanese', 'sw': 'swahili', 'sv': 'swedish', 'tg': 'tajik', 'ta': 'tamil', 'te': 'telugu', 'th': 'thai', 'tr': 'turkish', 'uk': 'ukrainian', 'ur': 'urdu', 'ug': 'uyghur', 'uz': 'uzbek', 'vi': 'vietnamese', 'cy': 'welsh', 'xh': 'xhosa', 'yi': 'yiddish', 'yo': 'yoruba', 'zu': 'zulu'}

ASSETS_PATH = Path(r"assets/frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def convert_text():
    t=entry_3.get(1.0, "end-1c")
    s=entry_4.get()
    d=entry_2.get()
    d=d.lower()
    s=s.lower()
    d=[k for k, v in lang.items() if v == d]
    d=''.join(d)
    s=[k for k, v in lang.items() if v == s]
    s=''.join(s)
    #print(translator.translate(t,d[0],s[0]).text)
    if s=='':
        s=translator.detect(t).lang
        entry_4.delete(0,END)
        entry_4.insert(END,lang[s])
        
    if d=='':
        d='en'
        entry_2.delete(0,END)
        entry_2.insert(END,'English')
    entry_1.delete(index1=1.0,index2=END)
    entry_1.insert(index=END,chars=translator.translate(t,d,s).text)


def change_language():
    s=entry_4.get()
    d=entry_2.get()
    entry_4.delete(0,END)
    entry_2.delete(0,END)
    entry_4.insert(END,d)
    entry_2.insert(END,s)

window = Tk()

window.geometry("1000x800")
window.configure(bg = "#FFFFFF")
window.title('Translator App')

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 800,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    500.00096130371094,
    400.00000762939453,
    image=image_image_1
)


entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))

entry_bg_1 = canvas.create_image(
    597.5,
    570.0,
    image=entry_image_1
)

entry_1 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=('Montserrat',18)
)

entry_1.place(
    x=270.0,
    y=470.0,
    width=655.0,
    height=198.0
)


entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))

entry_bg_2 = canvas.create_image(
    850.0,
    725.0,
    image=entry_image_2
)

entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=('Montserrat',20,'bold')
)

entry_2.place(
    x=775.0,
    y=700.0,
    width=150.0,
    height=48.0
)


entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))

entry_bg_3 = canvas.create_image(
    402.5,
    229.99999999999997,
    image=entry_image_3
)

entry_3 = Text(
    bd=0,
    bg="#577EDF",
    fg="#FFFFFF",
    highlightthickness=0,
    font=('Montserrat',18)
)

entry_3.place(
    x=75.0,
    y=129.99999999999997,
    width=655.0,
    height=198.0
)


entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))

entry_bg_4 = canvas.create_image(
    150.0,
    74.99999999999997,
    image=entry_image_4
)

entry_4 = Entry(
    bd=0,
    bg="#3E50AE",
    fg="#FFFFFF",
    highlightthickness=0,
    font=('Montserrat',20,'bold')
)

entry_4.place(
    x=75.0,
    y=49.99999999999997,
    width=150.0,
    height=48.0
)
    
    
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))

button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: convert_text(),
    relief="flat"
)

button_1.place(
    x=400.0,
    y=725.0,
    width=200.0,
    height=50.0
)


button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))

button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: change_language(),
    relief="flat"
)

button_2.place(
    x=451.0,
    y=350.0,
    width=100.0,
    height=101.0
)


entry_4.insert(END,'Auto detect')
entry_2.insert(END,'English')

window.resizable(False, False)
window.mainloop()