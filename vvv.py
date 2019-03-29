import smtplib
s=smtplib.SMTP("smtp.gmail.com","587")
s.starttls()
sender="kruthikan6666@gmail.com"
receiver="cocoousha@gmail.com"
msg="heyy baby"
s.login(sender,"9449831120")
s.sendmail(sender,receiver,msg)

print("erroe occured")

print("msg sent successfully")
s.quit()