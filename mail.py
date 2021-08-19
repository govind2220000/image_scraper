import smtplib
from logger.auto_logger import autolog

def send_email(receiver,msg):

    sender = "govindbgmi@gmail.com"
    password = "govind456123"

    server = smtplib.SMTP('smtp.gmail.com',  587)
    server.starttls()
    autolog("Sending Mail...")
    message = f"""
    URL: {msg}
    """

    try:
        server.login(sender,password)
        server.sendmail(sender,receiver,message)
        autolog("Mail Sent Successfully")       
    except:
        autolog("Sending Failed.", 3)
