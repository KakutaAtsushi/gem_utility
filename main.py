import tkinter as tk
from tkinter import *
#   from tkinter とは、tkinterライブラリから~をする　米印はすべてを意味する
from tkinter import ttk
from tkinter import messagebox
import webbrowser
import requests

main = tk.Tk()


def click_alert():
    message_box = messagebox.askyesno("確認", 'GemForexに移動しますか？')
    if message_box:
        response = requests.post('http://gemforex.com/login_submit.php')
        print(response)
        # webbrowser.open(response.url)
        print("移動しました")
    else:
        pass


main.title("GemForex AccountManager")
main.geometry("450x300")
label = ttk.Label(main, text='GemForexAccountManager!')

AccountKind = [ttk.Label(main, text="test", font=15),
               ttk.Label(main, text="", font=15),
               ttk.Label(main, text="", font=15),
               ttk.Label(main, text="", font=15)]
for i in range(len(AccountKind)):
    AccountKind[i].grid(row=i, column=0, ipady=3, sticky=tk.W)
tk.Button(main, text="ログイン後のGemに移動する", width=50, height=1, command=click_alert).grid(row=4, column=0, ipady=5,
                                                                                        sticky=tk.W + tk.E)

main.mainloop()
