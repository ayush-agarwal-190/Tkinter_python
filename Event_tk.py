from tkinter import *
def Ayush(event):
    print(f"Hello world{event.x},{event.y}")
    # event is sending the coordinates of x,y
root=Tk()
root.title("Events in tkinter")
root.geometry("644x344")

widget=Button(root,text='Click me please')
widget.pack()

widget.bind('<Button-1>', Ayush) #events
widget.bind('<Double-1>', quit) #events
root.mainloop()