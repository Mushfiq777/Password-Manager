from cryptography.fernet import Fernet
# fernet=  Fernet(b'HhR3hAZwfu4OkCX-Pkit_Hc-Qi9Tkw_9Dw0udGZ-B9w=')
with open("master.txt","rb") as f:
    master = f.read()

with open("key.txt","rb") as e:
    key = e.read()
    
fer = Fernet(key)
dec = fer.decrypt(master)
print(dec.decode())
    
