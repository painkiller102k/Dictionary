import smtplib,ssl
from email.message import EmailMessage
from tkinter import Tk, filedialog
#https://myaccount.google.com/apppasswords

def saada_kiri(): #обычное письмо с текстом
    kellele=input("Kellele: ")
    teema=input("Teema: ")
    sisu=input("Sisu: ")
    smtp_server='smtp.gmail.com'
    smtp_port=587
    kellelt="rossakovmartin@gmail.com"
    parool=input("Parool: ") # fyhg ejdp qdma zygm к примеру 
    msg=EmailMessage()
    msg['From']=kellelt
    msg['To']=kellele
    msg['Subject']=teema
    msg.set_content(sisu)
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls(context=ssl.create_default_context())
            server.login(kellelt, parool)
            server.send_message(msg)
            print("Kiri saadetud!")
    except Exception as e:
        print(f"Viga: {e}")

saada_kiri() #вызвать функцию

def saada_kiri1(): # письмо с файлом или картинкой
    kellele=input("Kellele: ")
    teema=input("Teema: ")
    sisu=input("Sisu: ")
    smtp_server='smtp.gmail.com'
    smtp_port=587
    kellelt="rossakovmartin@gmail.com"
    parool=input("Parool: ") # fyhg ejdp qdma zygm к примеру 
    msg=EmailMessage()
    msg['From']=kellelt
    msg['To']=kellele
    msg['Subject']=teema
    msg.set_content(sisu)


    fail=filedialog.askopenfilename(title="Vali fail", filetypes=[("All files", "*.*")])
    with open(fail, "rb") as f:
        faili_sisu = f.read()
        msg.add_attachment(faili_sisu, maintype="application", subtype="octet-stream", filename=fail)
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls(context=ssl.create_default_context())
            server.login(kellelt, parool)
            server.send_message(msg)
            print("Kiri saadetud!")
    except Exception as e:
        print(f"Viga: {e}")

saada_kiri1() #вызвать функцию