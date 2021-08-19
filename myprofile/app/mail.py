
class Mail():
    def __init__(self,name,email,dub,msg):
        self.name=name
        self.email=email
        self.dub=dub
        self.msg=msg
    def send_mail1(self):
        import smtplib 
        from email.mime.multipart import MIMEMultipart 
        from email.mime.text import MIMEText 
        from email.mime.base import MIMEBase 
        from email.mime.image import MIMEImage
        from email import encoders 

        fromaddr = "venkatesh.m@aitrg.com"
        toaddr = 'venkatesh2615@gmail.com'
        msg = MIMEMultipart('mixed')
        msg['From'] = fromaddr 
        msg['To'] = toaddr 
        from datetime import datetime
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")

        msg['Subject'] = 'PROFILE WEBSITE ENQUIRY MAIL'
        html = "<html><head><body><h1>"+self.name+"</h1><span>"+self.dub+"</span><br><p><span>"+self.email+"</span><br><p>"+self.msg+"</p></body></head></html>"
        msg.attach(MIMEText(html, 'html'))  
        s = smtplib.SMTP('mail.aitrg.com', 26) 
        s.starttls() 
        s.login(fromaddr, "Polojak@1") 
        text = msg.as_string() 

        s.sendmail(fromaddr, toaddr, text)
        s.quit()
        return 'Your message has been sent. Thank you!'