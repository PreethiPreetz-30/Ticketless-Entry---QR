import QRTicketing
import cv2

def Decode(str):
    a='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    cipherstr=''
    for i in str:
        k=a.index(i)
        cipherstr+=a[((k - 5)%26)]
    return str

cap = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()
while True:
    _, img = cap.read()
    data, bbox, _ = detector.detectAndDecode(img)
    if data:
        a=data
        break
    cv2.imshow("image", img)
    if cv2.waitKey(1) == ord("q"):
        break
if(QRTicketing.main.verifyQR(a)):
    QRTicketing.db_update([Decode(a[:"_"]),a["_"+1:]])
    print("ValidQr")
else:
    print("Invalid QR")