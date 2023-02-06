f = open("ciper.txt", "r")
f1 = open("Plain.txt", "w")
from thug import *
key = 7
Message = "Olssv"


for line in f:

    words=line.split()
    myline=""
    for word in words:
        dec=decrypt(word, key)
        myline+=dec+" "
    print(myline)
    f1.write(myline+"\n")

f.close()
f1.close()
print("success")
