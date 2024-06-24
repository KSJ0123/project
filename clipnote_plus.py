import tkinter
import clipboard
import threading
import tkinter.messagebox as msbox

window = tkinter.Tk()
window.title('Notes Plus')
window.geometry('400x500+100+100')


def th():
    th = threading.Thread(target=clipture)
    th.daemon = True
    th.start()


def pined():
    if cv1.get()==1:
        window.wm_attributes("-topmost",1)
    else:
        window.wm_attributes("-topmost",0)


def clipture():
    result2=""
    while True:
        result=clipboard.paste()
        if result != result2 :
            result2=result
            clippaste=tkinter.Text(window,width=50,height=10,)
            clippaste.pack()
            clippaste.insert('1.0',result2)
            clipdelet=tkinter.Button(window,text='X')
            clipdelet.pack()
            clipdelet.config(command=lambda cl=clippaste , dl=clipdelet : clip_delet(cl,dl))
        if cv2.get() != 1 :
            break

def clip_delet(cl,dl):
    dl.destroy()
    cl.destroy()
    
def exit_window():
    if msbox.askokcancel("종료","종료 하시겠습니까?"):
        window.destroy()
    


def add_meom1():
    meom=tkinter.Text(window,width=50,height=10)
    meom.pack()
    delet=tkinter.Button(window,text='X',command=lambda: (meom.destroy(),delet.destroy()))
    delet.pack()


cv1=tkinter.IntVar()
pin=tkinter.Checkbutton(window,text="고정",variable=cv1,command=pined)
pin.pack()


cv2=tkinter.IntVar()
clip=tkinter.Checkbutton(window,text="클립보드 연동",variable=cv2,command=th)
clip.pack()


add_memo=tkinter.Button(window,text='+',width=30,command=add_meom1)
add_memo.pack()

window.protocol('WM_DELETE_WINDOW',exit_window)

window.mainloop()