from tkinter import *

running_speed = 30

def initialize_running_speed():
    global running_speed
    top = Tk()
    top.geometry('500x100')
    top.title("自定义动作速率")
    entry = Entry(top,width=20)
    entry.pack()

    def setting():
        var = entry.get()		# 调用get()方法，将Entry中的内容获取出来
        print(var)
        global running_speed
        running_speed = int(var)
        top.destroy()

    Button(top,text='请输入10~30间数字，数字越大越快',command=setting).pack()
    top.mainloop()

def get_running_speed():
    return running_speed