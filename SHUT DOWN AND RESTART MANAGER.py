from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import time
import os
root=Tk()

root.minsize(width=410,height=390)
root.maxsize(width=410,height=390)
root.title("SHUT DOWN AND RESTART MANAGER")
root.iconbitmap('power.ico')
file=PhotoImage(file="bg.png")
bt_image=PhotoImage(file="power1.png")
bt_image=bt_image.subsample(2,2)
abort_image=PhotoImage(file="abort.png")

label=Label(root,image=file).pack()

hours_i=StringVar()
min_i=StringVar()
sec_i=StringVar()

hours_o1=StringVar()
hours_o2=StringVar()
min_o1=StringVar()
min_o2=StringVar()
sec_o1=StringVar()
sec_o2=StringVar()

hours_o1.set("0")
hours_o2.set("0")
min_o1.set("0")
min_o2.set("0")
sec_o1.set("0")
sec_o2.set("0")

frame1=Frame(root,border=2,bg="#00b8e6",width=330,highlightbackground="red",highlightthickness=4,height=40).place(x=39,y=10)
#frame1=Frame(root).place(x=1,y=50)

lbl1=Label(frame1,text="SHUT DOWN AND RESTART MANAGER",fg="black",bg="#00b8e6",font=("Blanka",13)).place(x=49,y=17)

hours_combo=ttk.Combobox(root,width=7,textvariable=hours_i,font="9",)
hours_combo["values"] =("HOURS","00","01","02","03","04","05","06","07","08","09","10","11","12")
hours_combo["state"]="readonly"
hours_combo.current(0)
hours_combo.place(x=39,y=70)

min_combo=ttk.Combobox(root,width=7,textvariable=min_i,font="9")
min_combo["values"] =("MINUTE","00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59","60")  
min_combo["state"]="readonly"
min_combo.current(0)
min_combo.place(x=155,y=70)

sec_combo=ttk.Combobox(root,width=8,textvariable=sec_i,font="9")
sec_combo["values"] =("SECOND","00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59","60")  
sec_combo["state"]="readonly"
sec_combo.current(0)
sec_combo.place(x=275,y=70)

radio_i=IntVar()

radio_b=Radiobutton(root,text="SHUTDOWN",value=0,variable=radio_i,bg="#00b8e6")
radio_b.place(x=85,y=110)

radio_b=Radiobutton(root,text="RESTART",value=1,variable=radio_i,bg="#00b8e6")
radio_b.place(x=225,y=110)

frm=Frame(root,width=40,).pack()

timer=Label(frm,text="TIMES LEFT TO SHUTDOWN / RESTART",font=("Arial",15),fg="red",bg="#00b8e6")
timer.place(y=200,x=15)

ent_h1=Label(frm,textvariable=hours_o1,font=("Arial",25),fg="red",bg="#00b8e6")
ent_h1.place(y=230,x=80)
ent_h2=Label(frm,textvariable=hours_o2,font=("Arial",25),fg="red",bg="#00b8e6")
ent_h2.place(y=230,x=110)
ent_h3=Label(frm,text=":",font=("Arial",25),fg="red",bg="#00b8e6")
ent_h3.place(y=230,x=140)
ent_m1=Label(frm,textvariable=min_o1,font=("Arial",25),fg="red",bg="#00b8e6")
ent_m1.place(y=230,x=170)
ent_m2=Label(frm,textvariable=min_o2,font=("Arial",25),fg="red",bg="#00b8e6")
ent_m2.place(y=230,x=200)
ent_m3=Label(frm,text=":",font=("Arial",25),fg="red",bg="#00b8e6")
ent_m3.place(y=230,x=235)
ent_s1=Label(frm,textvariable=sec_o1,font=("Arial",25),fg="red",bg="#00b8e6")
ent_s1.place(y=230,x=265)
ent_s2=Label(frm,textvariable=sec_o2,font=("Arial",25),fg="red",bg="#00b8e6")
ent_s2.place(y=230,x=295)

abort=Label(frm,text="IF YOU WANT TO ABORT SHUTDOWN / RESTART PRESS ABORT",font=("Arial",10),bg="#00b8e6",fg="black")
abort.place(x=1,y=270)

lbl2=Label(frm,text="Make by Boranno Golder",fg="white",bg="#00b8e6",font=("Arial",15))
lbl2.place(x=90,y=360)  
     
abort_out=0    
def abort():
    os.system("shutdown /a")
    root.destroy()

def countdown():
    try:
        user_input=int(hours_i.get())*3600+int(min_i.get())*60+int(sec_i.get())
    except:
        messagebox.showwarning("Warning","invlaid option")

    def shutdown():
        os.system(f"shutdown /s /f /t {user_input} ")

    def restart():
        os.system(f"shutdown /r /f /t {user_input}")

    if radio_i.get() == 0:
        shutdown()
    elif radio_i.get() ==1:
        restart()

    while user_input  >-1:
        hours=user_input//3600

        ext_sec=user_input-3600*hours

        min=ext_sec//60

        sec=ext_sec%60

        def n1(a):
            d=a//10
            return d
    
        def n2(a):
            d=a%10
            return d

        hours_o1.set(n1(hours))
        hours_o2.set(n2(hours))

        min_o1.set(n1(min))
        min_o2.set(n2(min))

        sec_o1.set(n1(sec))
        sec_o2.set(n2(sec))

        root.update()
        time.sleep(1)
        user_input-=1

btn_start=Button(root,width=50,text="Enter",height=45,image=bt_image,bg="#00b8e6",command=countdown)
btn_start.place(x=170,y=140)

btn_abort=Button(width=50,height=45,image=abort_image,bg="#00b8e6",command=abort,)
btn_abort.place(x=170,y=300)

root.mainloop()