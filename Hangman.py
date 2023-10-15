from tkinter import *
import random
import time
lst=['dog','cat','snake','bear','lion','tiger','deer','zebra','horse','pig','albatross','ant','ape','monkey']
rattempt=0
win=Tk()
win.title('MADE BY AYUSH KUMAR')

done=False
t=True
number123=random.randint(0,13)
word=lst[number123]



times=0

def clicked():
  global done
  for i in range(len(word)):
    if letter.get()==word[i]:
      buffer[i]=letter.get()
  u.configure(text=(" ".join(buffer)))
  letter.delete(0, 1)
  if "".join(buffer)==word:
    u.configure(text="correct")
    done=True
    clicked1()


def popupmsg():
    popup = Tk()
    label = Label(popup, text="timeup! The answer is "+word)
    label.pack(side="top", fill="x", pady=10)
    B1 = Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()

def clicked2():
  global t1,t,start,times,word
  t1=time.time()
  t=True
  start=True
  if times==0:
    for i in word:
        buffer.append("_")
    u.configure(text=(" ".join(buffer)))
  times+=1
  run()


def run():
  global t1,done
  while t==True:
    t2=time.time()
    u1.configure(text=("Time left: "+str(20-t2+t1)).split(".")[0])
    l=str(round(t2-t1))
    if (str(t2-t1)).split(".")[0]=="20":
      if done==False:
        u1.configure()
        clicked1()
        popupmsg()
      
def clicked1():
  global t
  t=False
  u1.configure(text="")
  run()

intro=Label(win,text='GUESS THE ANIMAL',width=21,height=2)
intro.place(x=139,y=0)

u=Label(win,text='',width=10,height=1)#buffer
u.place(x=165,y=50)
u1=Label(win,text='',width=20,height=1)#timer
u1.place(x=155,y=20)
buffer=[]
letter = Entry(win, width =1)
letter.place(x = 120, y = 70)
bt1=Button(win,text=' Check ',command=clicked)
bt1.place(x = 165, y= 126)
bt2=Button(win,text=' start ',command=clicked2)
bt2.place(x = 170, y= 100)


win.geometry('400x200')
win.mainloop()



