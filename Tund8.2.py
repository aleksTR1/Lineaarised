import ssl
import imghdr
import smtplib
from tkinter import *
from tkinter import filedialog, messagebox
from email.message import EmailMessage

aken = Tk()
aken.title("E-kirja saatmine")
aken.geometry("400x400")

fail = ""

def vali_fail():
    global fail
    fail = filedialog.askopenfilename()
    fail_label.config(text=fail)

def saada_kiri():
    saajad = email_box.get().split(",")
    sisu = kiri_box.get("1.0", END)

    server = "smtp.gmail.com"
    port = 587
    saatja = "sinu.email@gmail.com"
    parool = "rakenduse_võti"

    msg = EmailMessage()
    msg.set_content(sisu)
    msg['Subject'] = "E-kiri"
    msg['From'] = saatja
    msg['To'] = ", ".join(saajad)

    if fail:
        with open(fail, 'rb') as f:
            andmed = f.read()
            msg.add_attachment(andmed, maintype='image',
                               subtype=imghdr.what(None, andmed),
                               filename=fail.split("/")[-1])

    try:
        with smtplib.SMTP(server, port) as s:
            s.starttls(context=ssl.create_default_context())
            s.login(saatja, parool)
            s.send_message(msg)
        messagebox.showinfo("OK", "Kiri saadetud")
    except Exception as e:
        messagebox.showerror("Viga", str(e))

Label(aken, text="Saaja (komadega):").pack()
email_box = Entry(aken, width=40)
email_box.pack()

Label(aken, text="Sõnum:").pack()
kiri_box = Text(aken, width=45, height=10)
kiri_box.pack()

Button(aken, text="Vali fail", command=vali_fail).pack(pady=5)
fail_label = Label(aken, text="")
fail_label.pack()

Button(aken, text="Saada", command=saada_kiri).pack(pady=10)

aken.mainloop()
