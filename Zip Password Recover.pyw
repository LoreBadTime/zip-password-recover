import webbrowser,os,shutil
from pathlib import Path
import tkinter as tk
from tkinter.ttk import *
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
global root,username,style
import re
from itertools import product
from subprocess import PIPE,Popen,CREATE_NO_WINDOW,call
global zip7
import hashlib
import urllib.request
checkhash = True
root = tk.Tk()
root.title("Zip password recover")
root.configure(background='#202020')
root.geometry("204x160")
root.resizable(False,False) 


usbtn = ttk.Style()
usbtn.theme_use("alt")
usbtn.configure("cyan.TButton",height = 1,width = 25,foreground = "cyan",background = "#202020",activebackground = "#202124",border = 0)
usbtn.map("cyan.TButton",
    foreground=[('pressed', 'blue'), ('active', 'white'),('disabled', 'red')],
    background=[('pressed',  '#101010'), ('active', '#202020')],
    )

def hash_bytestr_iter(bytesiter, hasher, ashexstr=False):
    for block in bytesiter:
        hasher.update(block)
    return hasher.hexdigest() if ashexstr else hasher.digest()
def file_as_blockiter(afile, blocksize=65536):
    with afile:
        block = afile.read(blocksize)
        while len(block) > 0:
            yield block
            block = afile.read(blocksize)
try: 
    hashfolder = []
    for fname in os.listdir():
        try:
            if fname == "Zip Password Recover.pyw":
                hashfolder.append((str(hash_bytestr_iter(file_as_blockiter(open(fname, 'rb')), hashlib.sha256()))))
        except:
            pass
    hashfolder = ''.join(hashfolder)
    githublink = []
    for line in urllib.request.urlopen("https://raw.githubusercontent.com/LoreBadTime/zip-password-recover/main/hash.txt"):
        githublink = line.decode('utf-8')
    hashonline = ''
    for letter in githublink:
        if letter != '\n':
            hashonline = hashonline + letter 
            
    if str(hashonline) != str(hashfolder):
        checkhash = False
    del hashonline
    del githublink
    del hashfolder
except:
    checkhash = False

selection = 0
filename = ""
txt1=""
txt3="Chose file"

def openlicence():
    webbrowser.open("https://github.com/LoreBadTime/zip-password-recover/blob/main/LICENSE", new=2)
    
try:
    root.iconbitmap('icon.ico')
except:
    pass
def breacker():
    global T,zip7
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789\|"??$/()=><._-????@???????#??#*+]}????[{' 
    for length in range(1, 32): 
        to_attempt = product(chars, repeat=length)
        for attempt in to_attempt:
            passwd = ''.join(attempt)
            try:
                T.delete('1.0', tk.END)
                T.insert(tk.END, passwd)
            except:
                pass
            output = Popen(str(zip7 + ' x -p"'+ str(passwd) + '" ' + file + ' -y'),stderr=PIPE,stdin=PIPE, stdout=PIPE,creationflags = CREATE_NO_WINDOW)
            streamdata = output.communicate()[0]
            rc = output.returncode      
            if rc == 0:
                try:
                    T.delete('1.0', tk.END)
                    final = "files recovered pass: \n" + passwd
                    T.insert(tk.END, final)
                except:
                    pass
                return
            try:
                root.update()
            except:
                return
     
def open7z():
    webbrowser.open('https://www.7-zip.org/', new=2)
    try:
        root.destroy()
    except:
        pass


def callback():
    global build,filename,T,b,k,c,directory,file,f_w_ext,configfile,chars
    filename = askopenfilename()
    directory = os.path.dirname(filename)
    file = os.path.basename(filename)
    f_w_ext = Path(filename).stem
    
    if filename == "" or (file.endswith('.7z') != True and file.endswith('.zip') != True and file.endswith('.rar') != True):
        T.delete('1.0', tk.END)
        T.insert(tk.END, "Warning no file chosen")      
        k.state(["disabled"])
        
    else:
        T.delete('1.0', tk.END)
        T.insert(tk.END, file)
        k.state(["!disabled"])
    try: 
        return filename,directory,file,f_w_ext
    except:
        pass
def cracker():
    global filename,directory,file,f_w_ext
    if filename == "" or filename == None or (file.endswith('.7z') != True and file.endswith('.zip') != True and file.endswith('.rar') != True):
        T.delete('1.0', tk.END)
        T.insert(tk.END, "Warning no file chosen")
        k.state(["disabled"])
    else:
        os.chdir(directory)
        
        if filename != "":
            T.delete('1.0', tk.END)
            T.insert(tk.END, file)
            root.update()
            if (file.endswith('.7z') != True and file.endswith('.zip') != True and file.endswith('.rar') != True):
                T.delete('1.0', tk.END)
                T.insert(tk.END, "not a source file")
                k.state(["disabled"])
            else:
                T.delete('1.0', tk.END)
                T.insert(tk.END, file)
                breacker()
    try: 
        return filename,directory,file,f_w_ext
    except:
        pass
licenceacp = False
try:
    if os.path.isfile('ACCEPTEDLIC') == True:
        licenceacp = True
    else:
        licenceacp = messagebox.askyesno("Disclamer", "The program that is licensed to you is absolutely legal and you can use it provided that you are the legal owner of all files or data you are going to recover through the use of this software or have permission from the legitimate owner to perform these acts. Any illegal use of this software will be solely your responsibility. Accordingly, you affirm that you have the legal right to access all data, information and files that have been hidden.You further attest that the recovered data, passwords and/or files will not be used for any illegal purpose. Be aware password recovery and the subsequencial data decryption of unauthorized or otherwise illegally obtained files may constitute theft or another wrongful action and may result in your civil and (or) criminal prosecution,this popup will appear only the first time")
        if licenceacp  == False:
            exit()
        else:
            with open("ACCEPTEDLIC", "w+"):
                pass
        
except:
    pass
if os.path.isfile("C:\\Program Files\\7-Zip\\7z.exe") == True or os.path.isfile("C:\\Program Files (x86)\\7-Zip\\7z.exe") == True :
    root.geometry("204x160")
    if os.path.isfile("C:\\Program Files\\7-Zip\\7z.exe") == True:
        zip7 = '"C:\\Program Files\\7-Zip\\7z.exe"'
    else:
        zip7 = '"C:\\Program Files (x86)\\7-Zip\\7z.exe"'
    c = ttk.Button(root, text=txt3)
    c.configure(command=lambda :callback(),style = "cyan.TButton")
    c.place(x=20 ,y=20)
    k = ttk.Button(root, text="Recover archive",style = "cyan.TButton")
    k.state(["disabled"]) 
    k.configure(command=lambda :cracker())
    k.place(x=20 ,y=50)
    w = ttk.Button(root, text="Licence",style = "cyan.TButton")
    w.configure(command=lambda :openlicence())
    w.place(x=20 ,y=80)
    
    T = tk.Text(root, height = 2, width = 22,)
    T.place(x=10 ,y=110)
    T.insert(tk.END, "Chose your  protected archive")
    if licenceacp == False:
        exit()
    if checkhash == False:
        if messagebox.askyesno("Exit", "Cannot verify files integrity,be sure you have downloaded the software from https://github.com/LoreBadTime/zip-password-recover or else i suggest you to do an antivirus scan ,do you want to continue?") == False:
            exit()
else:
    root.geometry("204x60")
    j = tk.Button(root, text="Download 7zip", height = 1,width = 25,activebackground='black',background='black',foreground='cyan',activeforeground='yellow')
    j.configure(command=lambda :open7z())
    j.place(x=10 ,y=20)
    if licenceacp == False:
        exit()
    if checkhash == False:
        if messagebox.askyesno("Exit", "Cannot verify files integrity,be sure you have downloaded the software from https://github.com/LoreBadTime/zip-password-recover or else i suggest you to do an antivirus scan ,do you want to continue?") == False:
            exit()
def close():
    if messagebox.askokcancel("Exit", "Do you want to exit?"):
        root.destroy()

try:
    root.protocol("WM_DELETE_WINDOW", close)
except:
    pass
root.mainloop()



#by LorebadTime


