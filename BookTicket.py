import QRTicketing
import pyqrcode

def GenerateQR(str):
    qr=pyqrcode.create(str)
    qr.show()

def Encode(str):
    a='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    cipherstr=''
    for i in str:
        if(i.isalpha()):
            k=a.index(i)
            cipherstr+=a[((k + 5)%26)]
    return str

def Decode(str):
    #code
    return str

def Accept():
    name=input("Enter Name : ")
    date=input("Enter Date (DDMMYYYY):")
    str=name.upper()+"_"+date
    return str

str=Accept()
qr_str=Encode(str)
QRTicketing.main.qr_update(qr_str)
GenerateQR(qr_str)