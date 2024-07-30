from tkinter import messagebox as mb
import webbrowser
import json
import os

def download():
    try:
        with open("default.json","r",-1,"utf-8") as file:
            default = json.load(file)
    except FileNotFoundError:
        mb.showerror(title="!!!",message="Не удалось найти файл default.json.")
        return None
    
    for file in default:
        with open(f"saves/{file}","w",-1,"utf-8") as palette:
            palette.write(default[file])
    
if __name__ == "__main__":

    # Создание директории для хранения палитр, если её нет
    if not os.path.isdir("saves"):
        os.mkdir("saves")

    download()
    
    mb.showinfo(title="успех!",message="набор установлен!")

    path = os.path.dirname(os.path.abspath(__file__))
    webbrowser.open(url=f"file:///{path}/saves/default.html")