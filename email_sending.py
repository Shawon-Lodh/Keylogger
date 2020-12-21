import smtplib
from email.message import EmailMessage
import imghdr

# The mail addresses and password
sender_address = 'shawonlodh2508@gmail.com'
sender_pass = 'shawon1996'
receiver_address = 'shawonlodh2016@gmail.com'

# #normal text message sent
# msg = EmailMessage()
# msg['Subject'] = 'Test mail'
# msg['From'] = sender_address
# msg['To'] = 'shawonlodh2016@gmail.com'
# msg.set_content('Hi how are you?')
#
# #Create SMTP session for sending the mail
# session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
# session.starttls() #enable security
# session.login(sender_address, sender_pass) #login with mail_id and password
# text = msg.as_string()
# session.sendmail(sender_address, receiver_address, text)
# session.quit()
# print('Mail Sent')


# #text message sent with image
#
# with open(r'C:\Users\shawon\Downloads\flooop.png', 'rb') as f:
#     file_data = f.read()
#     file_type = imghdr.what(f.name)
#     file_name = f.name
#     # print(file_type)
#
# msg = EmailMessage()
# msg['Subject'] = 'Test mail'
# msg['From'] = sender_address
# msg['To'] = 'shawonlodh2016@gmail.com'
# msg.set_content('Hi how are you? one image attached ...')
# msg.add_attachment(file_data, maintype = 'image', subtype = file_type, filename = file_name)
#
# #Create SMTP session for sending the mail
# session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
# session.starttls() #enable security
# session.login(sender_address, sender_pass) #login with mail_id and password
# text = msg.as_string()
# session.sendmail(sender_address, receiver_address, text)
# session.quit()
# print('Mail Sent')


# #text message sent pdf/text/zip/otherfile

with open(r'C:\Users\shawon\Downloads\Documents\Documents.rar', 'rb') as f:
    file_data = f.read()
    file_name = f.name

msg = EmailMessage()
msg['Subject'] = 'Test mail'
msg['From'] = sender_address
msg['To'] = 'shawonlodh2016@gmail.com'
msg.set_content('Hi how are you? one image attached ...')
msg.add_attachment(file_data, maintype = 'application', subtype = 'octet-stream', filename = file_name)

#Create SMTP session for sending the mail
session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
session.starttls() #enable security
session.login(sender_address, sender_pass) #login with mail_id and password
text = msg.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
print('Mail Sent')