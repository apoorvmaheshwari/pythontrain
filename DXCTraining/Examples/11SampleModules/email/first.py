import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)

#Next, log in to the server
server.login("sampleEmail@gmail.com", "secretPassword")

#Send the mail
msg = "\nHello!This is a test mail" # The /n separates the message from the headers
server.sendmail("anotherEmail@gmail.com", "sv.shashankvats@gmail.com", msg)