# Color Collection
# Версия: 1.0

# Создатель: qpikzz (https://t.me/qpikzzbot)
# Актуальные версии: https://github.com/qpikzz

# Шрифты: Основной: Involve(https://github.com/StefanPeev), Акцент: StampatelloFaceto(https://github.com/JapanYoshi) thx!!!
# Иконка оливковой ветви, бамбук: https://www.flaticon.com/authors/istar-design-bureau

# Рекомендуется запускать при помощи pythonw.exe
# Хорошего дня!


# Импорты
try:
    from PIL import Image as PilImage, ImageTk
    from tkinter import messagebox as mb
    import tkinter.font as tkFont
    from tkinter import ttk
    from tkinter import *
    import webbrowser
    import json
    import os
    
except ModuleNotFoundError:
    import os
    from tkinter import messagebox as mb
    mb.showinfo(title="!!!", message="Сейчас будет установлен модуль Pillow, необходимый для работы приложения.")
    os.system("pip install pillow")
    from PIL import Image as PilImage, ImageTk
    import tkinter.font as tkFont
    from tkinter import ttk
    from tkinter import *
    import webbrowser
    import json


# Переменные 1
orange = "#E17B4B"
white = "#BEC1C6"
light = "#6E757F"
dark = "#3A393E"
nowScreen = "MainMenu"

beforeTheme = "Любая"
beforeSearch = "Поиск"

true = True
yNow = 0.3
color = {}
nowPage = 1
palettes = {}
pagesFrame = None
pageLabel = None


# Окно
tk = Tk()
tk.geometry("720x480")
tk.title("ColorCollection • v1.0")
tk["bg"] = light
tk.resizable(0,0)

bold = tkFont.Font(size=15, family="Involve", weight="bold")
font = tkFont.Font(size=15, family="Involve")
accent = tkFont.Font(size=15, family="StampatelloFaceto")
h1 = tkFont.Font(size=30, family="Involve", weight="bold")
h2 = tkFont.Font(size=20, family="Involve", weight="bold")

icon = PilImage.open("images/logo.png")
iconTk = ImageTk.PhotoImage(icon)
tk.iconphoto(False,iconTk)

def close():
    global true
    true = not true
tk.protocol("WM_DELETE_WINDOW",close)


# Переменные 2
themes = ("Любая", "Темная", "Светлая")
frameColors = {"Темная": dark,
               "Светлая": white,
               "Любая": light}
fontColors = {"Темная": white,
               "Светлая": dark,
               "Любая": dark}

themeStr = StringVar(value=themes[0])
themeStrAdd = StringVar(value=themes[0])

sidePng = PilImage.open("images/side.png")
sideImg = ImageTk.PhotoImage(sidePng)

welcomePng = PilImage.open("images/welcome.png")
welcomeImg = ImageTk.PhotoImage(welcomePng)

mainPng = PilImage.open("images/main.png")
mainImg = ImageTk.PhotoImage(mainPng)

infoPng = PilImage.open("images/info.png")
infoImg = ImageTk.PhotoImage(infoPng)

errorPng = PilImage.open("images/error.png")
errorImg = ImageTk.PhotoImage(errorPng)


# Боковое меню
side = Frame(tk,
            bg=dark,
            bd=0,
            height=480,
            width=216)
side.place(x=0, y=0)

Label(side,
      image=sideImg,
      width=216,
      height=480,
      bd=0).place(x=0, y=0)


# Главное меню
main = Frame(tk,
            bd=0,
            bg=light,
            height=480,
            width=720-216)
main.place(relx=0.3, rely=0)


# Функции
def clearMainMenu():
    global main, yNow
    main.destroy()
    main = Frame(tk,
                 bd=0,
                 bg=light,
                 height=480,
                 width=720-216)
    main.place(relx=0.3, rely=0) 
    yNow = 0.3

def url(link):
    webbrowser.open(link)

def drawPage(num):
    global palettes, main, pagesFrame, pageLabel, nowPage

    clearMainMenu()

    Label(main,
          width=504,
          height=480,
          image=mainImg,
          bd=0).place(x=0, y=0)
    
    pagesFrame.lift()

    try:
        pageLabel["text"]=f"Страница {nowPage}/{max(palettes)}"
    except ValueError:
        showError()

    if len(palettes) == 0:
        mb.showerror(title="!!!",message="X﹏X")
        return None
    
    try:
        page = palettes[num]
    except KeyError:
        page = palettes[1]
        nowPage = 1
        pageLabel.config(text=f"Страница {nowPage}/{max(palettes)}")

    for i in page:
        
        key = round(150/len(i["colors"]))
        step = 5
        
        if page.index(i) == 0:
            frame1 = Frame(main,
                           height=200,
                           width=200,
                           bg = frameColors[i["theme"]],
                           bd=0)
            frame1.place(relx=0.09,rely=0.03)

            Button(frame1,
                   height=1,
                   width=3,
                   font=accent,
                   text="i",
                   bd=0,
                   bg=frameColors[i["theme"]],
                   fg=fontColors[i["theme"]],
                   activebackground=frameColors[i["theme"]],
                   activeforeground=orange,
                   command = lambda:infoColor(0)).place(x=158,y=155)
            
            for j in i["colors"]:
                Frame(frame1,
                      height=key,
                      width=190,
                      bd=0,
                      bg=j).place(x=5,y=step)
                step += key
            
            Label(frame1,
                  height=1,
                  width=13,
                  font=accent,
                  text=i["name"],
                  bg=frameColors[i["theme"]],
                  anchor="w",
                  fg=fontColors[i["theme"]]).place(x=5,y=160)


        elif page.index(i) == 1:
            frame2 = Frame(main,
                           height=200,
                           width=200,
                           bg = frameColors[i["theme"]],
                           bd=0)
            frame2.place(relx=0.51,rely=0.03)

            Button(frame2,
                   height=1,
                   width=3,
                   font=accent,
                   text="i",
                   bd=0,
                   bg=frameColors[i["theme"]],
                   fg=fontColors[i["theme"]],
                   activebackground=frameColors[i["theme"]],
                   activeforeground=orange,
                   command = lambda:infoColor(1)).place(x=158,y=155)
            
            for j in i["colors"]:
                Frame(frame2,
                      height=key,
                      width=190,
                      bd=0,
                      bg=j).place(x=5,y=step)
                step += key

            Label(frame2,
                  height=1,
                  width=13,
                  font=accent,
                  text=i["name"],
                  bg=frameColors[i["theme"]],
                  anchor="w",
                  fg=fontColors[i["theme"]]).place(x=5,y=160)


        elif page.index(i) == 2:
            frame3 = Frame(main,
                           height=200,
                           width=200,
                           bg = frameColors[i["theme"]],
                           bd=0)
            frame3.place(relx=0.09,rely=0.47)

            Button(frame3,
                   height=1,
                   width=3,
                   font=accent,
                   text="i",
                   bd=0,
                   bg=frameColors[i["theme"]],
                   fg=fontColors[i["theme"]],
                   activebackground=frameColors[i["theme"]],
                   activeforeground=orange,
                   command=lambda:infoColor(2)).place(x=158,y=155)

            for j in i["colors"]:
                Frame(frame3,
                      height=key,
                      width=190,
                      bd=0,
                      bg=j).place(x=5,y=step)
                step += key

            Label(frame3,
                  height=1,
                  width=13,
                  font=accent,
                  text=i["name"],
                  bg=frameColors[i["theme"]],
                  anchor="w",
                  fg=fontColors[i["theme"]]).place(x=5,y=160)
 

        elif page.index(i) == 3:
            frame4 = Frame(main,
                           height=200,
                           width=200,
                           bg=frameColors[i["theme"]],
                           bd=0)
            frame4.place(relx=0.51, rely=0.47)

            Button(frame4,
                   height=1,
                   width=3,
                   font=accent,
                   text="i",
                   bd=0,
                   bg=frameColors[i["theme"]],
                   fg=fontColors[i["theme"]],
                   activebackground=frameColors[i["theme"]],
                   activeforeground=orange,
                   command=lambda:infoColor(3)).place(x=158, y=155)

            for j in i["colors"]:
                Frame(frame4,
                      height=key,
                      width=190,
                      bd=0,
                      bg=j).place(x=5, y=step)
                step += key

            Label(frame4,
                  height=1,
                  width=13,
                  font=accent,
                  text=i["name"],
                  bg=frameColors[i["theme"]],
                  anchor="w",
                  fg=fontColors[i["theme"]]).place(x=5, y=160)

def swipe(vector):
    try:
        global nowPage, palettes
        if vector == "-":
            if nowPage == 1:
                pass
            else:
                nowPage -= 1
                drawPage(nowPage)
        else:
            if nowPage == max(palettes):
                pass
            else:
                nowPage += 1
                drawPage(nowPage)
    except:
        showError()

def deletePallete(tempPallete):
    palletsFile = os.listdir("saves")

    foundPallete = False
    for i in palletsFile:
        if tempPallete["name"] in i:
            foundPallete = True
    
    if not foundPallete:
        mb.showerror(title="!!!", message="Палитра не найдена! :(")
        return None

    if mb.askyesno(title="???", message="Вы уверены, что хотите удалить данную палитру?"):
        os.remove(f"saves/{tempPallete['name']}.palette")
        mainMenu()

def showError():
    global main, nowScreen
    nowScreen = "error"

    clearMainMenu()

    Label(main,
          width=504,
          height=480,
          image=errorImg,
          bd=0).place(x=0, y=0)

def searchFunc(prompt, theme):
    global palettes, nowPage, beforeSearch, beforeTheme
    
    palettesFile = os.listdir("saves")
    palettesFileClear = []
    paletteList = []
    palettes = {}

    for i in palettesFile:
        if i.split(".")[-1] == "palette" and "." in i:
            palettesFileClear.append(i)

    if len(palettesFile) <= 0:
        showError()
        return None
    
    if prompt == "Поиск":
        prompt = ""
    if theme == "Любая":
        theme = ""

    for name in palettesFileClear:
        with open(f"saves/{name}", "r", -1, "utf-8") as file:
            palette = json.load(file)
            
            tempTags = ""
            if palette["tags"][0]:
                tempTags = ", ".join(palette["tags"])

            if theme in palette["theme"]:
                if prompt in palette["name"] or prompt.lower().strip() in tempTags:
                    paletteList.append(palette)

    if len(paletteList) == 0:
        showError()
        return None

    key, step = 1, 4
    for i in range(0, len(paletteList), step):
        palettes[key] = paletteList[i:i+step]
        key += 1

    tempSearch, tempTheme = beforeSearch.replace("Поиск",""), beforeTheme.replace("Любая","")
    if prompt != tempSearch and theme != tempTheme:
        nowPage = 1
    drawPage(nowPage)


# Экраны
def addNewColor(): # Добавление
    global main, color, nowScreen
    nowScreen = "addColor"
    
    clearMainMenu()

    name = Entry(main,
                 bd=0,
                 bg=light,
                 font=h1,
                 fg=dark,
                 insertbackground=dark,
                 selectforeground=light,
                 selectbackground=dark,
                 width=14)
    name.place(relx=0.05, rely=0.03)

    def focusName(event):
        if name.get() == "Название":
            name.delete(0, "end")
        elif name.get() == "":
            name.insert(0, "Название")
    focusName(None)
    name.bind('<FocusIn>', focusName)
    name.bind('<FocusOut>', focusName)

    themeAdd = ttk.Combobox(main,
                            width=8,
                            font=h2,
                            background=light,
                            foreground=dark,
                            state="readonly",
                            values=themes,
                            textvariable=themeStrAdd)
    themeAdd.place(relx=0.69, rely=0.03)

    tagsAdd = Text(main,
                   width=35,
                   height=2,
                   font=font,
                   bg=light,
                   bd=0,
                   fg=dark,
                   wrap="word",
                   selectbackground=dark,
                   selectforeground=light)
    tagsAdd.place(relx=0.06, rely=0.15)

    def focusTag(event):
        if tagsAdd.get("1.0", "end") == "Теги (вписывайте через запятую)\n":
            tagsAdd.delete("1.0", "end")
        elif tagsAdd.get("1.0", "end") == "\n":
            tagsAdd.insert(END, "Теги (вписывайте через запятую)")
    focusTag(None)
    tagsAdd.bind('<FocusIn>', focusTag)
    tagsAdd.bind('<FocusOut>', focusTag)

    # <hr>
    Frame(main,
          height=2, 
          width=460, 
          bd=0, 
          relief=SUNKEN,
          bg=dark).place(relx=0.05, rely=0.27)
    
    color = {}
    tempFrame = Frame(main,
                      bg=dark,
                      width=300,
                      height=38)
    tempFrame.place(relx=0.05, rely=0.3)

    tempEntry = Entry(tempFrame,
                      font=h2,
                      width=9,
                      bd=0,
                      bg=dark,
                      fg=white,
                      insertbackground=light,
                      selectbackground=light,
                      selectforeground=dark
                      )
    tempEntry.place(relx=0, rely=0)

    tempEntry.insert(0, dark)

    color[1] = (tempFrame, tempEntry)
    

    def addColor():
        if max(color) == 9:
            mb.showwarning(title="!!!", message="Вы не можете создать палитру более чем из 9 цветов :(")
            return None

        global yNow
        yNow += 0.07
        tempFrame = Frame(main,
                          bg=dark,
                          width=300,
                          height=38)
        tempFrame.place(relx=0.05, rely=yNow)

        tempEntry = Entry(tempFrame,
                          font=h2,
                          width=9,
                          bd=0,
                          bg=dark,
                          fg=white,
                          insertbackground=light,
                          selectbackground=light,
                          selectforeground=dark
                          )
        tempEntry.place(relx=0, rely=0)

        tempEntry.insert(0, dark)

        color[max(color)+1] = (tempFrame, tempEntry)

    addColorButton = Button(main,
                            text="+",
                            bg=dark,
                            fg=white,
                            activebackground=orange,
                            activeforeground=white,
                            width=10,
                            bd=0,
                            font=font,
                            command=addColor
                            )
    addColorButton.place(relx=0.7, rely=0.3)


    def removeColor():
        global yNow
        if max(color) == 1:
            mb.showwarning(title="!!!",message="Вы не можете удалить все цвета!")
            return None
        color[max(color)][0].destroy()
        del color[max(color)]
        yNow -= 0.07

    removeColorButton = Button(main,
                               text="-",
                               bg=dark,
                               fg=white,
                               activebackground=orange,
                               activeforeground=white,
                               width=10,
                               bd=0,
                               font=font,
                               command=removeColor
                               )
    removeColorButton.place(relx=0.7, rely=0.39)


    def save():

        for i in color:
            if color[i][1]["bg"] != dark:
                mb.showwarning(title="!!!", message="Мы не можем сохранить вашу палитру!\nИсправьте ошибку в выделеном поле")
                return None

        saveDict = {}
        saveDict["name"] = name.get()
        saveDict["theme"] = themeStrAdd.get()
        saveDict["tags"] = []
        saveDict["colors"] = []

        try:
            with open(f"saves/{saveDict['name']}.palette", "r", -1, "utf-8") as file:
                if not mb.askyesno(title="!!!",message="Палитра с таким названием уже существует. Вы уверены, что хотите перезаписать её?"):
                    return None
        except FileNotFoundError:
            pass

        if tagsAdd.get("1.0",END) == 'Теги (вписывайте через запятую)\n':
            saveDict["tags"].append(None)
        else:
            for i in tagsAdd.get("1.0",END).split(","):
                i = i.replace("\n","").lower().strip()
                saveDict["tags"].append(i)

        for i in color:
            saveDict["colors"].append(color[i][1].get())
            
        with open(f"saves/{saveDict['name']}.palette", "w", -1, "utf-8") as file:
            json.dump(saveDict, file, indent=4)

        mb.showinfo(title="!!!", message=f"Палитра сохранена в \"saves/{saveDict['name']}.palette\"")

    saveButton = Button(main,
                        text="Сохранить",
                        bg=dark,
                        fg=white,
                        activebackground=orange,
                        activeforeground=white,
                        width=10,
                        bd=0,
                        font=font,
                        command=save
                        )
    saveButton.place(relx=0.7, rely=0.8)

    backButton = Button(main,
                        text="Назад",
                        bg=dark,
                        fg=white,
                        activebackground=orange,
                        activeforeground=white,
                        width=10,
                        bd=0,
                        font=font,
                        command=mainMenu,
                        justify=CENTER
                        )
    backButton.place(relx=0.7, rely=0.89)


def mainMenu():
    global color, palettes, nowPage, pagesFrame, pageLabel, nowScreen, search, theme
    nowScreen = "MainMenu"
    color = {}

    clearMainMenu()

    palettesFile = os.listdir("saves")
    palettesFileClear = []
    paletteList = []
    palettes = {}

    for i in palettesFile:
        
        if i.split(".")[-1] == "palette" and "." in i:
            palettesFileClear.append(i)

    if len(palettesFileClear) == 0:
        Label(main,
              width=504,
              height=480,
              image=welcomeImg,
              bd=0).place(x=0,y=0)
        
        Button(main,
               font=font,
               text="Обо мне",
               bd=0,
               bg=light,
               fg=dark,
               activebackground=light,
               activeforeground=orange,
               command=lambda:url("https://t.me/qpikzzbot")).place(relx=0.45, rely=0.9)
        
        Button(main,
               font=font,
               text="ГитХаб",
               bd=0,
               bg=light,
               fg=dark,
               activebackground=light,
               activeforeground=orange,
               command=lambda:url("https://github.com/qpikzz")).place(relx=0.653, rely=0.9)
        
        Button(main,
               font=font,
               text="Донат",
               bd=0,
               bg=light,
               fg=dark,
               activebackground=light,
               activeforeground=orange,
               command=lambda:url("https://donationalerts.com/r/qpikzz")).place(relx=0.82, rely=0.9)
    
    else:
        for name in palettesFileClear:
            with open(f"saves/{name}", "r", -1, "utf-8") as file:
                palette = json.load(file)
                paletteList.append(palette)
            
        key, step = 1, 4
        for i in range(0, len(paletteList), step):
            palettes[key] = paletteList[i:i+step]
            key += 1

        # Страницы
        pagesFrame = Frame(tk,
                           height=10,
                           width=10,
                           bg=light)
        pagesFrame.place(x=220, y=440)

        pageLabel = Label(pagesFrame,
                          bg=light,
                          fg=dark,
                          text=f"Страница {nowPage}/{max(palettes)}",
                          font=font)
        pageLabel.grid(row=0, column=2)

        bt1 = Button(pagesFrame,
                     bg=light,
                     fg=dark,
                     text="<",
                     font=bold,
                     bd=0,
                     activebackground=light,
                     activeforeground=orange,
                     command=lambda:swipe("-"))
        bt1.grid(row=0, column=0)

        bt2 = Button(pagesFrame,
                     bg=light,
                     fg=dark,
                     text=">",
                     font=bold,
                     bd=0,
                     activebackground=light,
                     activeforeground=orange,
                     command=lambda:swipe("+"))
        bt2.grid(row=0, column=1)

        
        searchFunc(search.get(),theme.get())

        drawPage(nowPage)


def infoColor(num):
    global main, nowPage, palettes, nowScreen
    nowScreen = "aboutColor"

    tempColors = {}
    tempPallete = palettes[nowPage][num]

    clearMainMenu()

    Label(main,
          image=infoImg,
          width=504,
          height=480,
          bd=0).place(x=0, y=0)

    backButton = Button(main,
                 text="Назад",
                 bg=light,
                 bd=0,
                 width=7,
                 fg=dark,
                 command=mainMenu,
                 activebackground=light,
                 activeforeground=orange,
                 font=bold)
    backButton.place(relx=0.8, rely=0.71)

    deleteButton = Button(main,
                   text="Удалить",
                   bg=light,
                   bd=0,
                   fg=dark,
                   width=7,
                   activebackground=light,
                   activeforeground=orange,
                   font=bold,
                   command=lambda:deletePallete(tempPallete))
    deleteButton.place(relx=0.8, rely=0.79)


    Label(main,
          font=h1,
          text=tempPallete["name"],
          bg=light,
          fg=dark,
          width=16,
          bd=0,
          anchor="w"
          ).place(x=10, rely=0.71)
    
    tempTags = Text(main,
                    font=font,
                    height=2,
                    width=30,
                    bg=light,
                    fg=dark,
                    selectbackground=dark,
                    selectforeground=orange,
                    bd=0,
                    wrap="word")
    tempTags.place(x=10, rely=0.85)
    if tempPallete["tags"][0]:
        tempTags.insert(END,", ".join(tempPallete["tags"]))
    else:
        tempTags.insert(END,"Тегов нет :(")
    tempTags.config(state="disabled")

    
    size = 320/len(tempPallete["colors"])
    tempY = 10

    for color in tempPallete["colors"]:
        tempColors[color] = Frame(main,
              height=size,
              width=485,
              bg=color)
        tempColors[color].place(x=10, y=tempY)
        tempY += size

        tempEntry = Entry(tempColors[color],
              font=h2,
              bg=color,
              fg=dark,
              selectbackground=dark,
              selectforeground=color,
              insertbackground=color,
              bd=0,
              justify=CENTER,
              )
        tempEntry.place(relx=0.5, rely=0.5, anchor="center")
        tempEntry.insert(0, color)

        r = int(color[1:3], 16)
        g = int(color[3:5], 16)
        b = int(color[5:], 16)

        if (g + b - r <= 20) or (r + b - g <= 20) or (r + g - b <= 20):
            newFg = f'#{str(hex(min(r+200, 255)))[-2:]}{str(hex(min(g+200, 255)))[-2:]}{str(hex(min(b+200, 255)))[-2:]}'
        elif r+g+b <= 600:
            newFg = f'#{str(hex(min(r+70, 255)))[-2:]}{str(hex(min(g+70, 255)))[-2:]}{str(hex(min(b+70, 255)))[-2:]}'
        else:
            newFg = f'#{str(hex(max(r-80, 0)))[-2:]}{str(hex(max(g-80, 0)))[-2:]}{str(hex(max(b-80, 0)))[-2:]}'
        
        tempEntry.config(fg=newFg, selectbackground=newFg)


# Виджеты бокового меню 
# Поиск
search = Entry(side,
               width=16,
               font=bold,
               bd=0,
               bg=dark,
               fg=white,
               selectbackground=white,
               selectforeground=dark,
               insertbackground=white)
search.place(relx=0.07, rely=0.05)

def focusSearch(event):
    if search.get() == "Поиск":
        search.delete(0, "end")
    elif search.get() == "":
        search.insert(0, "Поиск")
def deleteFocus(event):
    event.widget.master.focus_set()
focusSearch(None)
search.bind('<FocusIn>', focusSearch)
search.bind('<FocusOut>', focusSearch)
search.bind('<Return>', deleteFocus)

# Тема
theme = ttk.Combobox(side,
                     width=14,
                     font=bold,
                     background=dark,
                     foreground=white,
                     state="readonly",
                     values=themes,
                     textvariable=themeStr)
theme.place(relx=0.07, rely=0.13)

# Добавить
add = Button(side,
             width=16,
             font=bold,
             text="+",
             bd=0,
             bg=dark,
             fg=white,
             activebackground=orange,
             activeforeground=white,
             command=addNewColor)
add.place(relx=0.04, rely=0.9)

# Загрузка основной страницы
mainMenu()

# Основной цикл
while true:
    try:
        for i in color:
            if nowScreen != "addColor":
                continue
                
            if "#" in color[i][1].get() and len(color[i][1].get()) == 7:
                try:
                    color[i][0]["bg"] = color[i][1].get()
                    color[i][1]["bg"] = dark
                except:
                    color[i][1]["bg"] = "#561111"
            else:
                color[i][1]["bg"] = "#561111"
    except:
        pass
    
    if theme.get() != beforeTheme or beforeSearch != search.get():
        if (search.get() == "Поиск" or search.get() == "") and theme.get() == "Любая":
            if nowScreen != "addColor":
                mainMenu()
        else:  
            searchFunc(search.get(), theme.get())
    
    beforeTheme = theme.get()
    beforeSearch = search.get()
    tk.update()