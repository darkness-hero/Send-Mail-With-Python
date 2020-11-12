import smtplib


def sendmail(from_addr,
             to_addr_list,
             cc_addr_list,
             subject,
             message,
             login,
             password,
             smtpserver="smtp.gmail.com:587"):

    header = "From %s\n" % from_addr
    header += "To: %s\n" % ",".join(to_addr_list)
    header += "CC: %s\n" % ",".join(cc_addr_list)
    header += "Subject: %s\n\n" % subject
    message = header + message

    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login, password)
    problems = server.sendmail(from_addr, to_addr_list, message)
    server.quit()
    return problems


to = input("To wich email do you want to send this email: ")
sub = input("What is your subject: ")
text = input("What is your message? ")

sendmail(from_addr="Your Mail",
         to_addr_list=[to],
         cc_addr_list=[""],
         subject=sub,
         message=text,
         login="Your Mail",
         password="Your Email password")
