import webbrowser,os,shutil
import encodings.idna
from pathlib import Path
import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
global root,username
import re
from itertools import product
from subprocess import PIPE,Popen,CREATE_NO_WINDOW,call
global zip7
import hashlib
import urllib.request
import multiaddr.codecs.idna
import multiaddr.codecs.uint16be
checkhash = True

def getdependencies():
    if messagebox.askyesno("Exit", "You need to install ipfshttpclient to run the software,you want to do it now?") == True:
        try:
            call("pip install ipfshttpclient==0.8.0a1")
        except:
            pass
        try:
            import ipfshttpclient
        except:
            messagebox.showerror(title="Missing dependencies", message="Cant install requiered libraries,closing the program")
            exit(code = 404)
    else:
        messagebox.showerror(title="Missing dependencies", message="Cant find requiered libraries,closing the program")
        exit(code = 404)
        
try:
    import ipfshttpclient
except:
    getdependencies()
    

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
            if fname == "Zip Password Recover.py":
                hashfolder.append((str(hash_bytestr_iter(file_as_blockiter(open(fname, 'rb')), hashlib.sha256()))))
        except:
            pass
    hashfolder = ''.join(hashfolder)
    githublink = []
    for line in urllib.request.urlopen("https://raw.githubusercontent.com/LoreBadTime/zip-password-recover/main/redirector.txt"):
        githublink = line.decode('utf-8')
    ipfsurl = ''
    for letter in githublink:
        if letter != '\n':
            ipfsurl = ipfsurl + str(letter)
    del githublink
    api = ipfshttpclient.connect()
    onlinehash = str(api.cat(ipfsurl), "utf-8")
    if str(onlinehash) != str(hashfolder):
        checkhash = False

    del ipfsurl
    del onlinehash
    del api
    del hashfolder
except:
    checkhash = False

selection = 0
filename = ""
root = tk.Tk()
root.title("Zip password recover")
root.configure(background='black')
root.geometry("204x160")
root.resizable(False,False) 
txt1=""
txt3="Chose file"
username = str(os.getlogin())
def openlicence():
    Licence = "This work is licensed under the Creative Commons Attribution-NonCommercial-NoDerivs 3.0 Unported License.\nTo view a copy of this license, visit http://creativecommons.org/licenses/by-nc-nd/3.0/ or send a letter to Creative Commons,\nPO Box 1866, Mountain View, CA 94042, USA.\nwork by LoreBadTime / Lorenzo Vittorio Concas email <concas324@gmail.com>" 
    with open('Licencezipassrecover.txt', 'w+') as file:
        file.write(Licence)
    webbrowser.open("Licencezipassrecover.txt")
    
try:
    root.iconbitmap('icon.ico')
except:
    pass
def breacker():
    global T,zip7
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789\|"£$/()=><._-çò@?ìà°#ù#*+]}èé[{' 
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
            print(rc)
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


def callback(num):
    global selection,build,filename,T,b,k,c,colorv,colorv2,directory,file,f_w_ext,configfile,chars
    selection = num
    if selection == 3:
            filename = askopenfilename()
            directory = os.path.dirname(filename)
            file = os.path.basename(filename)
            f_w_ext = Path(filename).stem
            
            if filename == "" or (file.endswith('.7z') != True and file.endswith('.zip') != True and file.endswith('.rar') != True):
                T.delete('1.0', tk.END)
                T.insert(tk.END, "Warning no file chosen")
                
                c.configure(foreground='yellow',activeforeground='yellow')
                k.configure(foreground='red',activeforeground='red')
                
            else:
                T.delete('1.0', tk.END)
                T.insert(tk.END, file)
                
                k.configure(foreground='green',activeforeground='yellow')
                build = True
            
    elif selection == 2 or selection == 4 or selection == 5:
            if filename == "" or filename == None or (file.endswith('.7z') != True and file.endswith('.zip') != True and file.endswith('.rar') != True):
                T.delete('1.0', tk.END)
                T.insert(tk.END, "Warning no file chosen")
                k.configure(foreground='red',activeforeground='red')
                c.configure(foreground='yellow',activeforeground='yellow')
            else:
                #try:
                os.chdir(directory)
                
                if filename != "":
                    T.delete('1.0', tk.END)
                    T.insert(tk.END, file)
                    root.update()
                    if (file.endswith('.7z') != True and file.endswith('.zip') != True and file.endswith('.rar') != True):
                        T.delete('1.0', tk.END)
                        T.insert(tk.END, "not a source file")
                        k.configure(foreground='red',activeforeground='red')
                        c.configure(foreground='yellow',activeforeground='yellow')
                    
                    else:
                        T.delete('1.0', tk.END)
                        T.insert(tk.END, file)
                        breacker()
               # except:
                    #pass
    try: 
        return filename,directory,file,f_w_ext
    except:
        pass
def hasherror():
    if messagebox.askyesno("Exit", "Cannot verify files integrity,be sure you have downloaded the software from https://github.com/LoreBadTime/zip-password-recover or else i suggest you to do an antivirus scan ,do you want to continue?") == False:
        root.destroy()
      
 
if os.path.isfile("C:\\Program Files\\7-Zip\\7z.exe") == True or os.path.isfile("C:\\Program Files (x86)\\7-Zip\\7z.exe") == True :
    root.geometry("204x160")
    if os.path.isfile("C:\\Program Files\\7-Zip\\7z.exe") == True:
        zip7 = '"C:\\Program Files\\7-Zip\\7z.exe"'
    else:
        zip7 = '"C:\\Program Files (x86)\\7-Zip\\7z.exe"'
    c = tk.Button(root, text=txt3, height = 1,width = 25,activebackground='black',background='black',foreground='white',activeforeground='yellow')
    c.configure(command=lambda :callback(3))
    c.place(x=10 ,y=20)
    k = tk.Button(root, text="Recover archive", height = 1,width = 25,activebackground='black',background='black',foreground='yellow',activeforeground='red')
    k.configure(command=lambda :callback(5))
    k.place(x=10 ,y=50)
    w = tk.Button(root, text="Licence", height = 1,width = 25,activebackground='black',background='black',foreground='yellow',activeforeground='red')
    w.configure(command=lambda :openlicence())
    w.place(x=10 ,y=80)
    
    T = tk.Text(root, height = 2, width = 22,)
    T.place(x=10 ,y=110)
    T.insert(tk.END, "Chose your  protected archive")
    if checkhash == False:
        hasherror()
else:
    root.geometry("204x60")
    j = tk.Button(root, text="Download 7zip", height = 1,width = 25,activebackground='black',background='black',foreground='cyan',activeforeground='yellow')
    j.configure(command=lambda :open7z())
    j.place(x=10 ,y=20)
    if checkhash == False:
        hasherror()
def close():
    if messagebox.askokcancel("Exit", "Do you want to exit?"):
        root.destroy()

try:
    root.protocol("WM_DELETE_WINDOW", close)
except:
    pass
root.mainloop()






