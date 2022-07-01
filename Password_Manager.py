import textwrap
from cryptography.fernet import Fernet
import os
width = os.get_terminal_size().columns
def view():
    with open("passwords.txt","r") as f:
        for line in f.readlines():
            line = line.strip()
            acc,username,pwd = line.split("|")
            adj = 40
            b1 = "%"*65
            print(b1.center(width))
            print("Account:".center(width-adj).rstrip(),acc.center(width).lstrip())
            print("Username:".center(width-adj).rstrip(),username.center(width).lstrip())
            print("Password:".center(width-adj).rstrip(),pwd.center(width).lstrip())
        print(b1.center(width))

def add():        
    adj = 32
    acc = input("Enter Account name or website: ".center(width-adj).rstrip())
    user = input("Enter username of the account: ".center(width-adj).rstrip())
    pwd = input("Enter the password of the account: ".center(width-29).rstrip())
    with open("passwords.txt","a") as f:
        f.write(acc+"|"+user+"|"+pwd+"\n")
    
def search():
    adj = 40
    b1 = "%"*65
    acc_name = input("Enter the account name you want to search: ".center(width-20).rstrip()).lower()
    with open("passwords.txt","r") as f:
        count = 0
        for line in f.readlines():
            line = line.strip()
            acc,username,pwd = line.split("|")
            if acc_name==acc.lower():
                count+=1

        if count != 0:
            print("Account(s) found!".center(width))
        else:
            print("No account found".center(width))
    with open("passwords.txt","r") as f:
        for line in f.readlines():
            line = line.strip()
            acc,username,pwd = line.split("|")
            if acc_name==acc.lower():
                print(b1.center(width))
                print("Account:".center(width-adj).rstrip(),acc.center(width).lstrip())
                print("Username:".center(width-adj).rstrip(),username.center(width).lstrip())
                print("Password:".center(width-adj).rstrip(),pwd.center(width).lstrip())
        if count != 0:
            print(b1.center(width))
                              
logo = (
"██████╗░░█████╗░░██████╗░██████╗░██╗░░░░░░░██╗░█████╗░██████╗░██████╗░\n"+
"██╔══██╗██╔══██╗██╔════╝██╔════╝░██║░░██╗░░██║██╔══██╗██╔══██╗██╔══██╗\n"+
"██████╔╝███████║╚█████╗░╚█████╗░░╚██╗████╗██╔╝██║░░██║██████╔╝██║░░██║\n"+
"██╔═══╝░██╔══██║░╚═══██╗░╚═══██╗░░████╔═████║░██║░░██║██╔══██╗██║░░██║\n"+
"██║░░░░░██║░░██║██████╔╝██████╔╝░░╚██╔╝░╚██╔╝░╚█████╔╝██║░░██║██████╔╝\n"+
"╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═════╝░░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚═╝╚═════╝░\n"+
"\n"+
"███╗░░░███╗░█████╗░███╗░░██╗░█████╗░░██████╗░███████╗██████╗░\n"+
"████╗░████║██╔══██╗████╗░██║██╔══██╗██╔════╝░██╔════╝██╔══██╗\n"+
"██╔████╔██║███████║██╔██╗██║███████║██║░░██╗░█████╗░░██████╔╝\n"+
"██║╚██╔╝██║██╔══██║██║╚████║██╔══██║██║░░╚██╗██╔══╝░░██╔══██╗\n"+
"██║░╚═╝░██║██║░░██║██║░╚███║██║░░██║╚██████╔╝███████╗██║░░██║\n"+
"╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝░╚═════╝░╚══════╝╚═╝░░╚═╝")


wrappedtext = textwrap.wrap(logo)
for line in wrappedtext:
    print(line.center(width))
    
while True:
    with open("key.txt","rb") as e:
        key = e.read()
    with open("master.txt","rb") as f:
        master = f.read()
    fer = Fernet(key)
    dec_master = fer.decrypt(master)
    dec_master = dec_master.decode()
    master_pwd = input("Enter master password: ".center(width).rstrip())
    if master_pwd==dec_master:
        print("Master password correct!".center(width))
        break
    else:
        print("Incorrect master password Try again!".center(width))
    

options = ["v","a","s","q"]
while True:
    ask = input("Do you want to view, add or search password(v/a/s) or quit(q): ".center(width).rstrip()).lower()
    if ask in options:
        if ask == "v":
            view()
        elif ask=="a":
            add()
        elif ask=="s":
            search()
        else:
            print("You have exited the password manager..".center(width))
            break
    else:
        print("Invalid input please try again".center(width).rstrip())    
        continue
    

