import textwrap
from cryptography.fernet import Fernet
import os
width = os.get_terminal_size().columns
b1 = "%"*65
def view():
    with open("key.txt","rb") as e:
        key = e.read()
        fer = Fernet(key)
    try:
        with open("passwords.txt","r") as f:
            for line in f.readlines():
                line = line.strip()
                acc,username,pwd = line.split("|")
                pwd = fer.decrypt(pwd.encode())
                pwd = pwd.decode()
                username = fer.decrypt(username.encode())
                username = username.decode()
                adj = 40
                b1 = "%"*65
                print(b1.center(width))
                print("Account:".center(width-adj).rstrip(),acc.center(width).lstrip())
                print("Username:".center(width-adj).rstrip(),username.center(width).lstrip())
                print("Password:".center(width-adj).rstrip(),pwd.center(width).lstrip())
            print(b1.center(width))
    except:
        print("No records stored in the database".center(width))

def add():        
    adj = 32
    found = True
    while found:
        
        acc = input("Enter Account name or website: ".center(width-adj).rstrip())
        with open("passwords.txt","r") as f:
            for line in f.readlines():
                line = line.strip()
                data = line.split("|")
                if acc == data[0]:
                    
                    print("Account name already exist. Please try a different account name".center(width))
                    break
            else:
                found = False
                
    user = input("Enter username of the account: ".center(width-adj).rstrip())
    pwd = input("Enter the password of the account: ".center(width-27).rstrip())
    with open("key.txt","rb") as e:
        key = e.read()
        fer = Fernet(key)
    pwd = fer.encrypt(pwd.encode())
    user = fer.encrypt(user.encode())

    with open("passwords.txt","a") as f:
        f.write(acc+"|"+user.decode()+"|"+pwd.decode()+"\n")
    
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
    with open("key.txt","rb") as e:
        key = e.read()
        fer = Fernet(key)
    with open("passwords.txt","r") as f:
        for line in f.readlines():
            line = line.strip()
            acc,username,pwd = line.split("|")
            if acc_name==acc.lower():
                pwd = fer.decrypt(pwd.encode())
                pwd = pwd.decode()
                username = fer.decrypt(username.encode())
                username = username.decode()
                print(b1.center(width))
                print("Account:".center(width-adj).rstrip(),acc.center(width).lstrip())
                print("Username:".center(width-adj).rstrip(),username.center(width).lstrip())
                print("Password:".center(width-adj).rstrip(),pwd.center(width).lstrip())
                
        if count != 0:
            print(b1.center(width))
            
def edit():
    with open("key.txt","rb") as e:
        key = e.read()
        fer = Fernet(key)
    count = 0
    adj = 40
    found = False
    acc_edit = input("Enter the account you want to edit: ").lower()
    with open("passwords.txt","r") as f:
        new_data = f.readlines()
        
    with open("passwords.txt","r") as f:
        data = []
        for i in range(len(new_data)):
            acc = new_data[i].split("|")
            acc[1] = fer.decrypt(acc[1].encode())
            acc[1] = acc[1].decode()
            acc[2] = fer.decrypt(acc[2].encode())
            acc[2] = acc[2].decode()
            if acc_edit==acc[0]:
                print("Account found!")
                found = True
                # username = acc[1]
                # pwd = acc[2]
                
                # pwd = fer.decrypt(pwd.encode())
                # pwd = pwd.decode()
                # username = fer.decrypt(username.encode())
                # username = username.decode()
                # acc[1] = fer.decrypt(acc[1].encode())
                # acc[1] = acc[1].decode()
                # acc[2] = fer.decrypt(acc[2].encode())
                # acc[2] = acc[2].decode()
                print(b1.center(width))
                print("Account:".center(width-adj).rstrip(),acc[0].center(width).lstrip())
                print("Username:".center(width-adj).rstrip(),acc[1].center(width).lstrip())
                print("Password:".center(width-adj).rstrip(),acc[2].center(width).lstrip())
                print(b1.center(width))
                user = acc[1]
                passw = acc[2]
                while True:
                    uorp = input("Want to edit username or password?{u/p): ".center(width).rstrip())
                    if uorp == "u":
                        new_username = input("Enter new username: ".center(width).rstrip())
                        acc[1] = new_username
                        
                        break
                    elif uorp == "p":
                        new_password = input("Enter new password: ".center(width).rstrip())
                        acc[2] = new_password
                        # acc[1] = username
                        break
                    else:
                        print("Invalid input Please try again".center(width))
                # with open("key.txt","rb") as e:
                #     key = e.read()
                #     fer = Fernet(key)
                acc[1] = fer.encrypt(acc[1].encode())
                acc[2] = fer.encrypt(acc[2].encode())
                acc[1] = acc[1].decode()
                acc[2] = acc[2].decode()
                new = "|".join(acc)
                data.append(new)
            else:
                acc[1] = fer.encrypt(acc[1].encode())
                acc[2] = fer.encrypt(acc[2].encode())
                acc[1] = acc[1].decode()
                acc[2] = acc[2].decode()
                new = "|".join(acc)
                data.append(new)
                # acc[1] = fer.encrypt(user.encode())
                # acc[2] = fer.encrypt(passw.encode())
                # acc[1] = acc[1].decode()
                # acc[2] = acc[2].decode()
                # new = "|".join(acc)
                # data.append(new)
    if found==False:
        print("No account found by the name.".center(width))
    with open("passwords.txt","w") as p:
        for i in data:
            p.write(i+"\n")               
                              
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
    
options = ["v","a","s","q","e"]
while True:
    ask = input("Do you want to view, add, edit or search password(v/a/e/s) or quit(q): ".center(width).rstrip()).lower()
    if ask in options:
        if ask == "v":
            view()
        elif ask=="a":
            add()
        elif ask=="s":
            search()
        elif ask=="e":
            edit()
        else:
            print("You have exited the password manager..".center(width))
            break
    else:
        print("Invalid input please try again".center(width).rstrip())    
        continue
    

