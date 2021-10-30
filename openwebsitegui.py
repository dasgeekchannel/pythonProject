import tkinter as tk
import webbrowser

root = tk.Tk()
# Set the resolution of window
# Adjust size
root.geometry("600x600")
root.resizable(width=True, height=True)
# defines open onion function for btn
def openonion():
    webbrowser.open_new('https://www.dasgeekcommunity.com')
btn = tk.Button(root, text='Take the blue pill', command=openonion)
btn.pack()
def opensite():
    webbrowser.open_new('http://cpy2u26bzxkirlvpdevohr4yj2t4od6fpkrplkus5lj47sl4x7pv46id.onion/')
btn1 = tk.Button(root, text='Follow The White Rabbit', command=opensite)
btn1.pack()
# loops window so it displays
root.mainloop()