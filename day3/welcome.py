import tkinter as tk
import tkmacosx as tkm
import json
import re
import random
from typing import List

datainfo = []
w=420
h=375
sp=r'!@#$%^&*'
cl=r'QWERTYUIOPLKJHGFDSAZXCVBNM'
ncl=r'qwertyuioplkjhgfdsazxcvbnm'
num=r'0123456789'
spa=r'[!@#$%^&*]'
cla=r'[QWERTYUIOPLKJHGFDSAZXCVBNM]'
ncla=r'[qwertyuioplkjhgfdsazxcvbnm]'
numa=r'[0123456789]'

class App():
    datainfo=[]
    def __init__(self):
        self.win=tk.Tk()
        self.win.title("Metorm")
        self.win.geometry("420x375+650+300")
        self.win.configure(bg="#181818")
        self.win.resizable(False,False)
        
        self.frm1=tk.Frame(self.win,bg="#181818")
        self.frm1.pack(padx=0,pady=0)
        self.frm2=tk.Frame(self.win,bg="#181818")
        
        self.label0=tk.Label(self.frm1, text="Email	:",fg="#fffcf0", bg="#181818")
        self.label0.configure(font=("Cormorant Garamond",15))
        self.label0.grid(padx=20, pady=20, row=0,column=0,sticky=tk.E)

        self.text0= tk.Entry(self.frm1, fg="#000000", bg="#f5f5dc")
        self.text0.configure(font=("Cormorant Garamond",15))
        self.text0.grid(row=0,column=1)

        self.label1=tk.Label(self.frm1, text="Username	:",fg="#fffcf0", bg="#181818")
        self.label1.configure(font=("Cormorant Garamond",15))
        self.label1.grid(padx=20, pady=20, row=1,column=0,sticky=tk.E)

        self.text1= tk.Entry(self.frm1, fg="#000000", bg="#f5f5dc")
        self.text1.configure(font=("Cormorant Garamond",15))
        self.text1.grid(row=1,column=1)

        self.label2=tk.Label(self.frm1, text="Password	:",fg="#fffcf0", bg="#181818")
        self.label2.configure(font=("Cormorant Garamond",15))
        self.label2.grid(padx=20, pady=20, row=2,column=0,sticky=tk.E)

        self.text2= tk.Entry(self.frm1,show="*", fg="#000000", bg="#f5f5dc")
        self.text2.configure(font=("Cormorant Garamond",15))
        self.text2.grid(row=2,column=1)

        self.label3=tk.Label(self.frm1, text="Confirm	:",fg="#fffcf0", bg="#181818")
        self.label3.configure(font=("Cormorant Garamond",15))
        self.label3.grid(padx=20, pady=20, row=3,column=0,sticky=tk.E)
        
        self.text3=tk.Entry(self.frm1,show="*", fg="#000000", bg="#f5f5dc")
        self.text3.configure(font=("Cormorant Garamond",15))
        self.text3.grid(row=3,column=1)

        self.button1=tkm.Button(self.frm1, text="CHECK", fg="#000000", bg="#ADD8E6", borderless=1,height=30, width=125, command=self.register)
        self.button1.configure(font=("Cormorant Garamond",20))
        self.button1.grid(padx=20, pady=20, row=4,column=1)
        
        self.button6=tkm.Button(self.frm1, text="SIGN-UP", fg="#000000", bg="#ADD8E6", borderless=1,height=30, width=125, command=self.login)
        self.button6.configure(font=("Cormorant Garamond",20))

        self.button2=tkm.Button(self.frm1, text="TRY AGAIN", fg="#000000", bg="red", height=30, width=150, command=self.reset)
        self.button2.configure(font=("Cormorant Garamond",20))

        self.button3=tkm.CircleButton(self.frm1, text="◌", fg="#fffcf0", bg="#181818",  borderless=1, height=30, width=30, command=self.rpg)
        self.button3.configure(font=("Cormorant Garamond",20))
        self.button3.grid(row=2,column=3)

        self.button4=tkm.CircleButton(self.frm1, text="👁️", fg="#000000", bg="#181818", borderless=1, height=30, width=30, command=self.show)
        self.button4.configure(font=("Cormorant Garamond",20))
        self.button4.grid(row=2,column=2,sticky=tk.E)

        self.button5=tkm.CircleButton(self.frm1, text="🔒️", fg="#000000", bg="#181818", borderless=1, height=30, width=30, command=self.hide)
        self.button5.configure(font=("Cormorant Garamond",20))

        self.err=tk.Label(self.frm1, bg="#181818")
        self.err.configure(font=("Cormorant Garamond",10))
        self.err.grid(row=5,column=1)
        
        self.label11=tk.Label(self.frm2, text="Username	:",fg="#fffcf0", bg="#181818")
        self.label11.configure(font=("Cormorant Garamond",15))
        self.label11.grid(padx=0, pady=20, row=1,column=0,sticky=tk.E)

        self.text11= tk.Entry(self.frm2, fg="#000000", bg="#f5f5dc")
        self.text11.configure(font=("Cormorant Garamond",15))
        self.text11.grid(row=1,column=1,sticky=tk.E)

        self.label22=tk.Label(self.frm2, text="Password	:",fg="#fffcf0", bg="#181818")
        self.label22.configure(font=("Cormorant Garamond",15))
        self.label22.grid(padx=0, pady=20, row=2,column=0,sticky=tk.E)

        self.text22= tk.Entry(self.frm2,show="*", fg="#000000", bg="#f5f5dc")
        self.text22.configure(font=("Cormorant Garamond",15))
        self.text22.grid(row=2,column=1,sticky=tk.E)

        self.button11=tkm.Button(self.frm2, text="LOGIN", fg="#000000", bg="#ADD8E6", height=30, width=100, command=self.on_clk)
        self.button11.configure(font=("Cormorant Garamond",20))
        self.button11.grid(padx=20, pady=20, row=3,column=1)

        self.button22=tkm.Button(self.frm2, text="TRY AGAIN", fg="#000000", bg="#ADD8E6", height=30, width=150, command=self.reset1)
        self.button22.configure(font=("Cormorant Garamond",20))

        self.err1=tk.Label(self.frm2, bg="#181818")
        self.err1.configure(font=("Cormorant Garamond",10))
        self.err1.grid(row=4,column=1)
        
        self.button44=tkm.CircleButton(self.frm2, text="👁️", fg="#000000", bg="#181818", borderless=1, height=30, width=30, command=self.show1)
        self.button44.configure(font=("Cormorant Garamond",20))
        self.button44.grid(row=2,column=2,sticky=tk.E)

        self.button55=tkm.CircleButton(self.frm2, text="🔒️", fg="#000000", bg="#181818", borderless=1, height=30, width=30, command=self.hide1)
        self.button55.configure(font=("Cormorant Garamond",20))
        
        self.waste=tk.Label(self.frm2, bg="#181818")
        self.waste.grid( pady=30, row=0,column=0)

    
    def login(self):
        self.frm1.pack_forget()
        self.frm2.pack(padx=0, pady=0)
        
    def show1(self):
        self.text22.config(show="")
        self.button44.grid_forget()
        self.button55.grid(row=1,column=2,sticky=tk.E)

    def hide1(self):
        self.button44.grid(row=1,column=2,sticky=tk.E)
        self.button55.grid_forget()
        self.text22.config(show="*")
        
    def show(self):
        self.text2.config(show="")
        self.text3.config(show="")
        self.button4.grid_forget()
        self.button5.grid(row=2,column=2,sticky=tk.E)

    def hide(self):
        self.button5.grid_forget()
        self.button4.grid(row=2,column=2,sticky=tk.E)
        self.text2.config(show="*")
        self.text3.config(show="*")
        
    def rpg(self):
        self.text2.delete(0, len(self.text2.get()))
        self.text3.delete(0, len(self.text3.get()))
        pwdlen = random.randint(8, 12)
        temppass=[]
        for i in range(0,pwdlen,1):
            choice=random.randint(1,4)
            if(choice==1):
                let=random.randint(0,(len(sp)-1))
                temppass.append(sp[let])
            elif(choice==2):
                let=random.randint(0,(len(cl)-1))
                temppass.append(cl[let])
            elif(choice==3):
                let=random.randint(0,(len(num)-1))
                temppass.append(num[let])
            elif(choice==4):
                let=random.randint(0,(len(ncl)-1))
                temppass.append(ncl[let])
        randpass="".join(temppass)
        self.text2.insert(0, randpass)
        self.text2.config(show="")
        self.text3.insert(0, randpass)
        self.text3.config(show="")
        self.button4.grid_forget()
        self.button5.grid(row=2,column=2,sticky=tk.E)
        self.err["text"]="Secure password generated!!";
        self.err.configure(fg="green")
        
    def reset(self):
        self.button2.grid_forget()
        self.button1.grid(padx=20, pady=20, row=4,column=1)
        self.err["text"]=""
        self.text0.delete(0, len(self.text0.get()))
        self.text1.delete(0, len(self.text1.get()))
        self.text2.delete(0, len(self.text2.get()))
        self.text3.delete(0, len(self.text3.get()))
        self.text2.config(show="*")
        self.text3.config(show="*")



    def register(self):
        global datainfo
        if(((self.text2.get()==self.text3.get()) and (((re.search(spa,self.text2.get()) and re.search(cla,self.text2.get()) and re.search(numa,self.text2.get())))) and (len(self.text2.get())>8)) and ("@" in self.text0.get()) and (".com" in self.text0.get()) and ((self.text0.get() or self.text1.get() or self.text2.get() or self.text3.get())!=(""or" "))):
            self.button2.grid_forget()
            self.button6.grid(padx=20, pady=20, row=4,column=1)
            try:
                with open("credits.json", "r",encoding="utf-8") as jf:
                    datainfo = json.load(jf)
            except FileNotFoundError:
                print("File not found.")
            except json.JSONDecodeError:
                print("Invalid JSON data in the file.")

            data = {
                "email": self.text0.get(),
                "username": self.text1.get(),
                "password": self.text3.get()
            }
            datainfo.append(data)
            try:
                with open("credits.json", "w",encoding="utf-8") as jf:
                    json.dump(datainfo, jf)
            except FileNotFoundError:
                print("File not found.")
            except json.JSONDecodeError:
                print("Invalid JSON data in the file.")
            self.err["text"]="All details verified!!"
            self.err.configure(fg="green")
            self.button1.grid_forget()
            self.button2.grid_forget()
            self.button6.grid(padx=20, pady=20, row=4,column=1)

        else:
            if((self.text2.get()!=self.text3.get()) and (("@" not in self.text0.get()) or (".com" not in self.text0.get()))):
                self.err["text"]="Password doesn't match & e-mail invalid!!"
                self.err.configure(fg="red")
            elif((((re.search(spa,self.text2.get()) and re.search(cla,self.text2.get()) and re.search(numa,self.text2.get())))) and (len(self.text2.get())<8)):
                self.err["text"]="Invalid Password!!"
                self.err.configure(fg="red")
            elif((self.text0.get() or self.text1.get() or self.text2.get() or self.text3.get())==(""or" ")):
                self.err["text"]="Some fields are empty!!"
                self.err.configure(fg="red")
            elif(self.text2.get()!=self.text3.get()):
                self.err["text"]="Password doesn't match!!"
                self.err.configure(fg="red")
            elif(("@" not in self.text0.get()) and (".com" not in self.text0.get())):
                self.err["text"]="Invalid e-mail!!"
                self.err.configure(fg="red")
            self.button1.grid_forget()
            self.button2.grid(padx=20, pady=20, row=4,column=1)        

    def reset1(self):
        self.button22.grid_forget()
        self.button11.grid(padx=0, pady=40, row=3,column=1)
        self.err1["text"]=""
        self.text11.delete(0, len(self.text11.get()))
        self.text22.delete(0, len(self.text22.get()))
   
    def on_clk(self):
        global datainfo
        mf=False
        try :
            with open("credits.json", "r",encoding="utf-8") as jf:
                datainfo = json.load(jf)
        except FileNotFoundError:
            print("File not found.")
        except json.JSONDecodeError:
            print("Invalid JSON data in the file.")

        for data in datainfo:
            if ((data.get("email") == self.text11.get() or data.get("username") == self.text11.get()) and data.get("password") == self.text22.get()):
                mf = True
                break
        if(mf==True):
            self.err1["text"]="Validated Credentials!!"
            self.err1.configure(fg="green")
            self.text11.delete(0, len(self.text11.get()))
            self.text22.delete(0, len(self.text22.get()))
                
        elif(mf==False):
            self.button11.grid_forget()
            self.button22.grid(padx=0, pady=40, row=3,column=1)
            self.err1["text"]="Invalid Credentials!!"
            self.err1.configure(fg="red")
            self.text11.delete(0, len(self.text11.get()))
            self.text22.delete(0, len(self.text22.get()))
            
x=App()
