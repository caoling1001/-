import tkinter as tk
from PIL import ImageTk, Image
import os
import random
filename=""
def shuru():
    a=str(random.randint(1,100))
    b=random.choice('+-*/')
    c=str(random.randint(1,100))
    d=random.choice('+-*/')
    e=str(random.randint(1,100))
    return a+b+c+d+e
def panduan():
    t=shuru()
    while True:
        if eval(t)<100:
            if eval(t)>0:
                if eval(t)%2==0:
                    return t
        t=shuru()
def sizeyunsuan(num):
    x=[]
    k=[]
    for i in range(num):
        t=panduan()
        while True:
            if t in x:
                t=panduan()
            else:
                x.append(t)
                y=eval(t)
                a=t+'='+str(y)
                k.append(a)
                break
    return x,k 
def mynew():
    global root,filename,textPad
    root.title("δ�����ļ�")
    filename=None
    textPad.delete(1.0,END)

def myopen():
    global filename,root,textPad
    filename=askopenfilename(defaultextension=".txt")
    if filename=="":
        filename=None
        tk.messagebox.showerror(title='hi', message='�ļ���ʧ��!')
    else:
        root.title("�������������"+os.path.basename(filename))
        textPad.delete(1.0,END)
        f=open(filename,'r')
        textPad.insert(1.0,f.read())
        f.close()

def mysave():
    global filename,textPad
    try:
        f=open(filename,'w')
        msg=textPad.get(1.0,'end')
        f.write(msg)
        f.close()
        tk.messagebox.showinfo(title='hi',message='�ļ�����ɹ���')
    except:
        mysaveas()
        tk.messagebox.showinfo(title='hi',message='�ļ�����ɹ���')

def mysaveas():
    global filename
    f=asksaveasfilename(initialfile="δ����.txt",defaultextension=".txt")
    filename=f
    fh=open(f,'w')
    msg=textPad.get(1.0,END)
    fh.write(msg)
    fh.close()
    root.title("�������������"+os.path.basename(f)) 

def insert_point():
    global textPad,entry,chVarDis,check1
    t=int(entry.get())
    label=chVarDis.get()
    x,k=sizeyunsuan(t)
    if label==0:
        for i in range(t//3):
            textvar = "��%3d����%10s\t" %(3*i+1,x[3*i+0])+"��%3d����%10s\t" %(3*i+2,x[3*i+1])+"��%3d����%10s\t" %(3*i+3,x[3*i+2])
            textPad.insert(tk.INSERT,textvar+'\n')
        check1.select()
        label=chVarDis.get()
        if label==1:
            for i in range(len(x)):
                textvar = "��%3d����%15s\t" %(3*i+1,k[3*i+0])+"��%3d����%15s\t" %(3*i+2,k[3*i+1])+"��%3d����%15s\t" %(3*i+3,k[3*i+2])
                textPad.insert(tk.INSERT,textvar+'\n')
                
        #textPad.insert('insert','\t')# ����insert��ʾ�ڹ�괦�����ַ�
    else:
        for i in range(len(x)):
            textvar = "��%3d����%15s\t" %(3*i+1,k[3*i+0])+"��%3d����%15s\t" %(3*i+2,k[3*i+1])+"��%3d����%15s\t" %(3*i+3,k[3*i+2])
            textPad.insert(tk.INSERT,textvar+'\n')
def delete_text():
    global textPad
    t=tk.messagebox.askquestion(title='��Ϣ', message='ȷ�������?')
    if t=='yes':
        textPad.delete('1.0','end')
        tk.messagebox.showinfo(title='��Ϣ',message='��ճɹ���')
root = tk.Tk()
root.title("�������������")
#����
canvas = tk.Canvas(root, width=900,height=800,bd=0, highlightthickness=0)
imgpath = './1.jpg'
img = Image.open(imgpath)
photo = ImageTk.PhotoImage(img)
canvas.create_image(400, 50, image=photo)
canvas.pack()
imgpath2 = './2.jpg'
img2 = Image.open(imgpath2)
photo2 = ImageTk.PhotoImage(img2)
canvas.create_image(450, 650, image=photo2)
canvas.pack()
#�˵���
menubar=tk.Menu(root)

# �ļ�����
filemenu=tk.Menu(root)
filemenu.add_command(label="�½�",accelerator="Ctrl+N",command=mynew)
filemenu.add_command(label="��",accelerator="Ctrl+O",command=myopen)
filemenu.add_command(label="����",accelerator="Ctrl+S",command=mysave)
filemenu.add_command(label="���Ϊ",accelerator="Ctrl+shift+s",command=mysaveas)
menubar.add_cascade(label="�ļ�",menu=filemenu)
root['menu']=menubar

#��ȡ���ֿ�
entry=tk.Entry(root,insertbackground='blue', highlightthickness =2)
entry.pack()
canvas.create_window(300, 150, width=100, height=30,window=entry)
L1 = tk.Label(root, text="�����������1-100����")
L1.pack()
canvas.create_window(150, 150, width=150, height=20,window=L1)
t=entry.get()
b = tk.Button(root, text='ȷ��',  width=20, height=20,command=insert_point)
b.pack()
canvas.create_window(400, 150, width=80, height=20,window=b)
chVarDis = tk.IntVar()   
check1 = tk.Checkbutton(root, text="��ʾ��", variable=chVarDis)   
check1.select()     # �ø�ѡ���Ƿ�ѡ,selectΪ��ѡ, deselectΪ����ѡ
check1.pack()
canvas.create_window(550, 150, width=150, height=20,window=check1)      
fr=tk.Frame(root)
fr.place()
canvas.create_window(450, 350, width=850, height=300,window=fr)
scroll = tk.Scrollbar(fr)
textPad=tk.Text(fr,undo=True, font =("����", 14,"normal"),width=800, height=300)
scroll.pack(side=tk.RIGHT,fill=tk.Y)
textPad.pack(side=tk.LEFT,fill=tk.Y)
scroll.config(command=textPad.yview) # ���ı���������������ϣ��������������ı�����滬��
textPad.config(yscrollcommand=scroll.set) # ���������������ı���
#canvas.create_window(400, 350, width=700, height=300,window=textPad)
b2 = tk.Button(root, text='������',  width=20, height=20,command=delete_text)
b2.pack()
canvas.create_window(650, 150, width=80, height=20,window=b2)
root.mainloop()
