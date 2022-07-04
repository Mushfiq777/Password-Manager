import csv
import textwrap
from cryptography.fernet import Fernet
import os
width = os.get_terminal_size().columns
b1 = "%"*65 #settting the border for viewing accounts
#function to view all the accounts
def view():
    with open("key.txt","rb") as e:
        key = e.read()
        fer = Fernet(key)
    try:
        with open("passwords.txt","r") as f:
            for line in f.readlines():
                line = line.strip()
                acc,username,pwd = line.split(",")
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
#function to add accounts
def add():        
    adj = 32
    found = True
    while found:
        
        acc = input("Enter Account name or website: ".center(width-adj).rstrip())
        with open("passwords.txt","r") as f:
            for line in f.readlines():
                line = line.strip()
                data = line.split(",")
                if acc.lower() == data[0].lower():
                    
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
        f.write(acc+","+user.decode()+","+pwd.decode()+"\n")
#function to search account    
def search():
    adj = 40
    b1 = "%"*65
    acc_name = input("Enter the account name you want to search: ".center(width-20).rstrip()).lower()
    with open("passwords.txt","r") as f:
        count = 0
        for line in f.readlines():
            line = line.strip()
            acc,username,pwd = line.split(",")
            if acc_name==acc.lower():
                count+=1
        if count != 0:
            print("Account found!".center(width))
        else:
            print("No account found".center(width))
    with open("key.txt","rb") as e:
        key = e.read()
        fer = Fernet(key)
    with open("passwords.txt","r") as f:
        for line in f.readlines():
            line = line.strip()
            acc,username,pwd = line.split(",")
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
#function to edit account            
def edit():
    with open("key.txt","rb") as e:
        key = e.read()
        fer = Fernet(key)
    count = 0
    adj = 40
    found = False
    acc_edit = input("Enter the account you want to edit: ".center(width).rstrip()).lower()
    with open("passwords.txt","r") as f:
        new_data = f.readlines()     
    with open("passwords.txt","r") as f:
        data = []
        for i in range(len(new_data)):
            acc = new_data[i].split(",")
            acc[1] = fer.decrypt(acc[1].encode())
            acc[1] = acc[1].decode()
            acc[2] = fer.decrypt(acc[2].encode())
            acc[2] = acc[2].decode()
            if acc_edit==acc[0].lower():
                print("Account found!".center(width))
                found = True
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
                        break
                    else:
                        print("Invalid input Please try again".center(width))              
                acc[1] = fer.encrypt(acc[1].encode())
                acc[2] = fer.encrypt(acc[2].encode())
                acc[1] = acc[1].decode()
                acc[2] = acc[2].decode()
                new = ",".join(acc)
                data.append(new)
            else:
                acc[1] = fer.encrypt(acc[1].encode())
                acc[2] = fer.encrypt(acc[2].encode())
                acc[1] = acc[1].decode()
                acc[2] = acc[2].decode()
                new = ",".join(acc)
                data.append(new)                
    if found==False:
        print("No account found by the name.".center(width))
    with open("passwords.txt","w") as p:
        for i in data:
            p.write(i+"\n") 
#function to delete all account           
def delete_all():
    open("passwords.txt","w").close()
    print("All records deleted successfully".center(width))
#function to delete a specific account
def delete_s():
    with open("key.txt","rb") as e:
        key = e.read()
        fer = Fernet(key)
    acc_d = input("Enter the account name you want to delete: ".center(width).rstrip())
    found = False
    newdata = []
    with open("passwords.txt","r") as d:
        for line in d.readlines():
            linestripped = line.strip()
            l = linestripped.split(",")
            pwd = fer.decrypt(l[2].encode())
            pwd = pwd.decode()
            username = fer.decrypt(l[1].encode())
            username = username.decode()
            adj = 40            
            if acc_d == l[0]:
                found = True
                print("Account found!".center(width))
                print(b1.center(width))
                print("Account:".center(width-adj).rstrip(),acc_d.center(width).lstrip())
                print("Username:".center(width-adj).rstrip(),username.center(width).lstrip())
                print("Password:".center(width-adj).rstrip(),pwd.center(width).lstrip())
                print(b1.center(width))
                while True:                    
                    input1 = input("Are you sure you want to delete?(y/n): ".center(width).rstrip()).lower()
                    if input1=="y":
                        print("Account deleted successfully!".center(width))
                        break
                    elif input1=="n":
                        newdata.append(linestripped)
                        print("Account not deleted".center(width).rstrip())
                        break
                    else:
                        print("Invalid Input Please Try Again".center(width))  
            else:
                newdata.append(linestripped)
    if found==False:
        print("No account found by the name.".center(width))
    with open("passwords.txt","w") as p:
        for i in newdata:
            p.write(i+"\n")
#function for delete menu          
def delete():
    while True:        
        input1 = input("Do you want to delete all records or a specifc one?(a/s): ".center(width).rstrip()).lower()
        if input1=="a":
            delete_all()
            break
        elif input1=="s":
            delete_s()
            break
        else:
            print("Invalid Input Please Try Again".center(width).rstrip())
#function to sort accounts                 
def sort():
    with open("key.txt","rb") as e:
        key = e.read()
        fer = Fernet(key)
    input1 = input("Do you want to sort in ascending order or descending order of account names?(a/d): ".center(width).rstrip()).lower()
    
    if input1=="a":
        try:
            with open("passwords.txt","r") as f:
                data = f.readlines()
                data = sorted(data,key=str.lower)
                # print(data)
                for i in data:
                    acc,username,pwd = i.split(",")
                    username = fer.decrypt(username.encode())
                    username = username.decode()
                    pwd = fer.decrypt(pwd.encode())
                    pwd = pwd.decode()
                    adj = 40
                    print(b1.center(width))
                    print("Account:".center(width-adj).rstrip(),acc.center(width).lstrip())
                    print("Username:".center(width-adj).rstrip(),username.center(width).lstrip())
                    print("Password:".center(width-adj).rstrip(),pwd.center(width).lstrip())
                print(b1.center(width))         
        except:
            print("No record in the database.".center(width)) 
    elif input1=="d":
        try:
            with open("passwords.txt","r") as f:
                data = f.readlines()                
                data = sorted(data,key=str.lower,reverse=True)
                for i in data:
                    acc,username,pwd = i.split(",")
                    username = fer.decrypt(username.encode())
                    username = username.decode()
                    pwd = fer.decrypt(pwd.encode())
                    pwd = pwd.decode()
                    adj = 40
                    print(b1.center(width))
                    print("Account:".center(width-adj).rstrip(),acc.center(width).lstrip())
                    print("Username:".center(width-adj).rstrip(),username.center(width).lstrip())
                    print("Password:".center(width-adj).rstrip(),pwd.center(width).lstrip())
                print(b1.center(width))         
        except:
            print("No record in the database.".center(width))
#function to export to a .csv file            
def export_csv():
    with open("key.txt","rb") as e:
        key = e.read()
        fer = Fernet(key)
    save_path = input("Enter the path of the folder you want to export to:".center(width).rstrip())
    file_name = "Accounts_passwords.csv"
    completename= os.path.join(save_path,file_name)
    header = ["Account","Username","Password"]
    with open("passwords.txt","r") as p:
        data = []
        for line in p.readlines():
            line = line.strip()
            line = line.split(",")
            line[1] = fer.decrypt(line[1].encode())
            line[1]=line[1].decode()
            line[2] = fer.decrypt(line[2].encode())
            line[2]=line[2].decode()
            data.append(line)
    try:       
        with open(completename,"w",newline="") as c:
            writer = csv.writer(c)
            writer.writerow(header)
            writer.writerows(data)
        print("Export successful".center(width))
    except:
        print("Export uncsuccessful- Check if file with the same name and directory is open or being used by another service".center(width))    
#function to edit the master password
def edit_master():
    with open("key.txt","rb") as e:
        key = e.read()
        fer = Fernet(key)
    while True:
        input1 = input("Enter your new master password: ".center(width).rstrip())
        input2 = input("Re-confirm new master password: ".center(width).rstrip())
        if input1==input2:
            print("Password matched!".center(width))
            break
        else:
            print("Passwords did not match please try again".center(width))
        
    while True:
        sure = input("Are you sure you want to change the master password?(y/n): ".center(width).rstrip()).lower()
        if sure=="y":
            input1 = fer.encrypt(input1.encode()) 
            with open("master.txt","wb") as m:
                m.write(input1)
                print("Master password changed successfully!".center(width))
                break
        elif sure=="n":    
            print("Master password remained unchanged".center(width))
            break
        else:
            print("Invalid Input Please Try Again".center(width))                    
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
    
options = ["1","2","3","4","5","6","7","8","9"]
while True:
    t1 = "1.Edit master password"
    t2 = "2.view       6.sort"
    t3 = "3.add        7.search"
    t4=  "4.edit       8.export"
    t5 = "5.delete     9.quit"
    print("Main menu:".center(width),
            t1.center(width+len(t1)-24).rstrip() ,
            t2.center(width+len(t2)-22).rstrip(),
            t3.center(width+len(t3)-22).rstrip(),
            t4.center(width+len(t4)-22).rstrip(),
            t5.center(width+len(t5)-22).rstrip(),
            sep="\n")
    ask = input("Enter your choice: ".center(width-3).rstrip()).lower()
    if ask in options:
        if ask=="1":
            edit_master()
        elif ask == "2":
            view()
        elif ask=="3":
            add()
        elif ask=="4":
            edit()
        elif ask=="5":
            delete()
        elif ask=="6":
            sort() 
        elif ask=="7":
            search()
        elif ask=="8":
            export_csv()   
        else:
            print("You have exited the password manager..".center(width))
            break
    else:
        print("Invalid input please try again".center(width).rstrip())    