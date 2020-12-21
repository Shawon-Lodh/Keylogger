import winreg

searching_browser_name = ['7Star', 'Amigo', 'BlackHawk',
                          'Brave', 'Centbrowser', 'Chedot',
                          'Chrome Canary', 'Chromium', 'Coccoc', 'Comodo Dragon',
                          'Comodo IceDragon', 'Cyberfox', 'Elements Browser',
                          'Epic Privacy Browser', 'Firefox','MoFirefox', 'Google Chrome',
                          'Icecat', 'K-Meleon', 'Kometa',
                          'Opera', 'Orbitum', 'Sputnik',
                          'Torch', 'Uran', 'Vivaldi']

def foo(hive, flag):
    aReg = winreg.ConnectRegistry(None, hive)
    aKey = winreg.OpenKey(aReg, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
                          0, winreg.KEY_READ | flag)

    count_subkey = winreg.QueryInfoKey(aKey)[0]

    software_list = []

    for i in range(count_subkey):
        software = {}
        try:
            asubkey_name = winreg.EnumKey(aKey, i)
            asubkey = winreg.OpenKey(aKey, asubkey_name)
            software['name'] = winreg.QueryValueEx(asubkey, "DisplayName")[0]

            try:
                software['version'] = winreg.QueryValueEx(asubkey, "DisplayVersion")[0]
            except EnvironmentError:
                software['version'] = 'undefined'
            try:
                software['publisher'] = winreg.QueryValueEx(asubkey, "Publisher")[0]
            except EnvironmentError:
                software['publisher'] = 'undefined'
            software_list.append(software)
        except EnvironmentError:
            continue

    return software_list

def find_browser():
    browser_installed_in_machine = []
    software_list = foo(winreg.HKEY_LOCAL_MACHINE, winreg.KEY_WOW64_32KEY) + foo(winreg.HKEY_LOCAL_MACHINE,winreg.KEY_WOW64_64KEY) + foo(winreg.HKEY_CURRENT_USER, 0)
    #print all install software
    # for software in software_list:
    #     print('Name=%s, Version=%s, Publisher=%s' % (software['name'], software['version'], software['publisher']))
    # print('Number of installed apps: %s' % len(software_list))

    #find installed browser
    for i in software_list:
        for j in searching_browser_name:
            if (i['name'].lower()).find(j.lower()) != -1:
                browser_installed_in_machine.append(j)
                # print(i['name'])
    return browser_installed_in_machine


print(find_browser())
