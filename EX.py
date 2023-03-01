import os, sys, platform
print('\033[1;92mCONGRATULATIONS YOUR DEVICE HAS BEEN SUPPORT THIS TOOLS')
try:
    import requests
except:
    os.system('pip install requests')
os.system('xdg-open https://facebook.com/groups/darkforce71officials/')
time.sleep(2)
os.system("git pull")

bit = platform.architecture()[0]
if bit == '64bit':
    import sex
elif bit == '32bit':
    import sex32
