from cryptography.fernet import Fernet
key = Fernet.generate_key()
print(key)
pwd = "5571"
fernet = Fernet(key)
enc_pwd = fernet.encrypt(pwd.encode())
print(enc_pwd)


with open("master.txt","wb") as g:
    # g.write(key+"\r\n"+enc_pwd
    g.write(enc_pwd)
    # g.writelines(key)
    # g.writelines(enc_pwd)
    
with open("key.txt","wb") as e:
    e.write(key)
    
# with open("master.txt","rb") as f:
#     a = f.read()
#     # print(a)
#     dec = fernet.decrypt(a)
#     print(dec)
