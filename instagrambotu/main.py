
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from dotenv import load_dotenv
import os
import pyautogui
import random

load_dotenv()
#şifre
INSTAGRAM_USER = os.getenv("INSTAGRAM_USER")
INSTAGRAM_PASSWORD = os.getenv("INSTAGRAM_PASSWORD")

ayarlar = webdriver.ChromeOptions()
ayarlar.headless= True
PATH = "D:\selenium\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.instagram.com/")

def soru():
    print("hangi işlemi yaptırmak istersiniz")
    print("1 = işlem Takip  \n"
          "2 = işlem keşfet yorum \n"
          "3 = işlem hesap yorum\n")
    secim = input("kaçıncı işlem ?")
    if "1" in secim:
        print("seçim takip atma oldu")
        takip()
    if "2" in secim:
        print("seçim keşfet yorum oldu")
        kesfet()
    if "3" in secim:
        print("seçim belirli hesap fotoğraflarına yorum attırma")
        hesap()
    else:
        print("seçim yapılmadı")


# login
def login():
    time.sleep(4)
    username = driver.find_element("css selector", "input[name='username']")
    password = driver.find_element("css selector", "input[name='password']")
    username.clear()
    password.clear()
    username.send_keys(INSTAGRAM_USER)
    password.send_keys(INSTAGRAM_PASSWORD)
    login = driver.find_element("css selector", "button[type='submit']").click()


#profil takip atma
def takip():
    time.sleep(10)
    driver.get("https://www.instagram.com/explore/people/")
    time.sleep(5)
    kac = input("kaç takip atılsın")
    time.sleep(5)
    kac1 = int(kac)
    i = 1
    while i<=kac1:
        n = str(i)
        profile3 = driver.find_element(
            "css selector", "body._a3wf.system-fonts--body.segoe:nth-child(2) div.x9f619.x1n2onr6.x1ja2u2z:nth-child(2) div.x78zum5.xdt5ytf.x1n2onr6.x1ja2u2z div.x78zum5.xdt5ytf.x1n2onr6 div.x78zum5.xdt5ytf.x1n2onr6.xat3117.xxzkxad div.x78zum5.xdt5ytf.x10cihs4.x1t2pt76.x1n2onr6.x1ja2u2z:nth-child(1) div.x9f619.xnz67gz.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib:nth-child(1) div.xh8yej3.x1gryazu.x10o80wk.x14k21rp.x1porb0y.x17snn68.x6osk4m section.x78zum5.xdt5ytf.x1iyjqo2.x6ikm8r.xg6iff7 main.x78zum5.xdt5ytf.x1iyjqo2.x182iqb8.xvbhtw8:nth-child(1) div._aa0- div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.xwib8y2.x1y1aw1k.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1:nth-child(2) div.x1i10hfl.x1qjc9v5.xjbqb8w.xjqpnuy.xa49m3k.xqeqjp1.x2hbi6w.x13fuv20.xu3j5b3.x1q0q8m5.x26u7qi.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x1ypdohk.xdl72j9.x2lah0s.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x2lwn1j.xeuugli.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x16tdsg8.x1hl2dhg.xggy1nq.x1ja2u2z.x1t137rt.x1q0g3np.x87ps6o.x1lku1pv.x1a2a7pz.xh8yej3.x193iq5w.x1lliihq.x1dm5mii.x16mil14.xiojian.x1yutycm:nth-child("+n+") div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1pi30zi.x1swvt13.xwib8y2.x1y1aw1k.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1 div.x9f619.x1n2onr6.x1ja2u2z.x1qjc9v5.x78zum5.xdt5ytf.x1iyjqo2.xl56j7k.xeuugli div.x9f619.x1n2onr6.x1ja2u2z.x78zum5.x2lah0s.x1qughib.x6s0dn4.xozqiw3.x1q0g3np div.x9f619.x1n2onr6.x1ja2u2z.xdt5ytf.x2lah0s.x193iq5w.xeuugli.xamitd3.x78zum5:nth-child(3) div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x16n37ib.x1uhb9sk.x1plvlek.xryxfnj.xs83m0k.x1c4vz4f.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1 > button._acan._acap._acas._aj1-").click()
        time.sleep(8)
        i+=1


def kesfet():
    #keşfet yorum
    time.sleep(10)
    kesfetanamenu = driver.find_element(
        "css selector", "body._a3wf.system-fonts--body.segoe:nth-child(2) div.x9f619.x1n2onr6.x1ja2u2z:nth-child(2) div.x78zum5.xdt5ytf.x1n2onr6.x1ja2u2z div.x78zum5.xdt5ytf.x1n2onr6 div.x78zum5.xdt5ytf.x1n2onr6.xat3117.xxzkxad div.x78zum5.xdt5ytf.x10cihs4.x1t2pt76.x1n2onr6.x1ja2u2z:nth-child(1) div.x9f619.xnz67gz.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib:nth-child(1) div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1.xeq5yr9.x1dr59a3.xixxii4.x13vifvy.x1n327nk div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj div.x78zum5.x1q0g3np.x1gvbg2u.x1qughib.xleuxlb.xxfw5ft.x1mh60rb.x1f91t4q.x1n2onr6 div.xvb8j5.x1vjfegm div.x1cy8zhl.x9f619.x78zum5.xdt5ytf.x1gvbg2u.x1y1aw1k.xn6708d.xx6bls6.x1ye3gou.xvbhtw8.x1xgvd2v.x1o5hw5a.xaeubzz div.xh8yej3.x1iyjqo2 div:nth-child(3) div.x1n2onr6 a.x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz._a6hd > div.x9f619.x3nfvp2.xr9ek0c.xjpr12u.xo237n4.x6pnmvc.x7nr27j.x12dmmrz.xz9dl7a.xn6708d.xsag5q8.x1ye3gou.x80pfx3.x159b3zp.xdoji71.x1dejxi8.x9k3k5o.xs3sg5q.x11hdxyr.x12ldp4w.x1wj20lx.x1dn74xm.xif99yt.x172qv1o.x10djquj.x1lhsz42.xzauu7c.x1lq5wgf.xgqcy7u.x30kzoy.x9jhf4c").click()
    time.sleep(10)
    kesfetilkfoto = driver.find_element(
    "css selector", "body._a3wf.system-fonts--body.segoe:nth-child(2) div.x9f619.x1n2onr6.x1ja2u2z:nth-child(2) div.x78zum5.xdt5ytf.x1n2onr6.x1ja2u2z div.x78zum5.xdt5ytf.x1n2onr6 div.x78zum5.xdt5ytf.x1n2onr6.xat3117.xxzkxad div.x78zum5.xdt5ytf.x10cihs4.x1t2pt76.x1n2onr6.x1ja2u2z:nth-child(1) div.x9f619.xnz67gz.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib:nth-child(1) div.xh8yej3.x1gryazu.x10o80wk.x14k21rp.x1porb0y.x17snn68.x6osk4m section.x78zum5.xdt5ytf.x1iyjqo2.x6ikm8r.xg6iff7 main.x78zum5.xdt5ytf.x1iyjqo2.x182iqb8.xvbhtw8:nth-child(1) div._ac-t._ac-u._ac-v div._acgg div.x9f619.xjbqb8w.x1lliihq.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1n2onr6.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1:nth-child(1) div._al5u:nth-child(2) div.x9f619.xjbqb8w.x1lliihq.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1n2onr6.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1 a.x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz._acg7._a6hd div._aagu > div._aagw").click()
    cumleler =['su ic!','proje gelistir','yazılım ogren','boyle devam','hayat cok pahalı be','cok komik dssada','eeee bu ne simdi','ah be ronaldom','messi be','oku oku']
    kacyorumkesfet = input("kaç yorum yapılsın")
    kacyorumkesfet1 = int(kacyorumkesfet)
    time.sleep(10)

    for i in range(kacyorumkesfet1 ):
        try:
            kesfetyorum = driver.find_element("css selector", "body._a3wf.system-fonts--body.segoe:nth-child(2) div.x1uhb9sk div.x9f619.x1n2onr6.x1ja2u2z:nth-child(1) div.x78zum5.xdt5ytf.xg6iff7.x1n2onr6 div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj:nth-child(3) div.x1qjc9v5.x9f619.x78zum5.xdt5ytf.x1iyjqo2.xl56j7k div.x1cy8zhl.x9f619.x78zum5.xl56j7k.x2lwn1j.xeuugli.x47corl div.x1ja2u2z.x1afcbsf.x1a2a7pz.x6ikm8r.x10wlt62.xdt5ytf.x1n2onr6.xl56j7k.x78zum5.x6s0dn4.x5yr21d.xh8yej3.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x47corl div.xs83m0k.xl56j7k.x1iy3rx.x1n2onr6.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xh8yej3.xjbqb8w.x1v7wizp.x1l0w46t.xa3vuyk.xw8ag78 div.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe.x1qjc9v5.xjbqb8w.x1lcm9me.x1yr5g0i.xrt01vj.x10y3i5r.x47corl.xh8yej3.x15h9jz8.xr1yuqi.xkrivgy.x4ii5y1.x1gryazu.xir0mxb.x1juhsu6:nth-child(2) article._aatb._aate._aatg._aati div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1n2onr6.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.xl56j7k div._ae65 div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1n2onr6.x1plvlek.xryxfnj.x1iyjqo2.x2lwn1j.xeuugli.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1 div._ae1k._ae2q._ae2r div._ae2s._ae3v._ae3w section._aaoe._ae5y._ae5z._ae62 div._aaof form._aidk._ak6u div._akhn > textarea.x1i0vuye.xvbhtw8.x76ihet.xwmqs3e.x112ta8.xxxdfa6.x5n08af.x78zum5.x1iyjqo2.x1qlqyl8.x1d6elog.xlk1fp6.x1a2a7pz.xexx8yu.x4uap5.x18d9i69.xkhd6sd.xtt52l0.xnalus7.x1bq4at4.xaqnwrm.xs3hnx8:nth-child(2)").click()
            time.sleep(4)
            kesfetyorum.send_keys(Keys.ENTER)
            pyautogui.typewrite(random.choice(cumleler))
            time.sleep(4)
            kesfetyorum.send_keys(Keys.ENTER)
            time.sleep(8)
            kesfetgec = driver.find_element("css selector", "body._a3wf.system-fonts--body.segoe:nth-child(2) div.x1uhb9sk div.x9f619.x1n2onr6.x1ja2u2z:nth-child(1) div.x78zum5.xdt5ytf.xg6iff7.x1n2onr6 div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj:nth-child(3) div.x1qjc9v5.x9f619.x78zum5.xdt5ytf.x1iyjqo2.xl56j7k div.x1cy8zhl.x9f619.x78zum5.xl56j7k.x2lwn1j.xeuugli.x47corl div.x1ja2u2z.x1afcbsf.x1a2a7pz.x6ikm8r.x10wlt62.xdt5ytf.x1n2onr6.xl56j7k.x78zum5.x6s0dn4.x5yr21d.xh8yej3.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x47corl div.xs83m0k.xl56j7k.x1iy3rx.x1n2onr6.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xh8yej3.xjbqb8w.x1v7wizp.x1l0w46t.xa3vuyk.xw8ag78 div:nth-child(1) div._aeap._aeaq div._aear div._aaqg._aaqh > button._abl-").click()
            time.sleep(8)
        except:
            kesfetgec = driver.find_element("css selector","body._a3wf.system-fonts--body.segoe:nth-child(2) div.x1uhb9sk div.x9f619.x1n2onr6.x1ja2u2z:nth-child(1) div.x78zum5.xdt5ytf.xg6iff7.x1n2onr6 div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj:nth-child(3) div.x1qjc9v5.x9f619.x78zum5.xdt5ytf.x1iyjqo2.xl56j7k div.x1cy8zhl.x9f619.x78zum5.xl56j7k.x2lwn1j.xeuugli.x47corl div.x1ja2u2z.x1afcbsf.x1a2a7pz.x6ikm8r.x10wlt62.xdt5ytf.x1n2onr6.xl56j7k.x78zum5.x6s0dn4.x5yr21d.xh8yej3.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x47corl div.xs83m0k.xl56j7k.x1iy3rx.x1n2onr6.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xh8yej3.xjbqb8w.x1v7wizp.x1l0w46t.xa3vuyk.xw8ag78 div:nth-child(1) div._aeap._aeaq div._aear div._aaqg._aaqh > button._abl-").click()
            time.sleep(8)

    kesfetgec2 = driver.find_element(
    "css selector", "body._a3wf.system-fonts--body.segoe:nth-child(2) div.x1uhb9sk div.x9f619.x1n2onr6.x1ja2u2z:nth-child(1) div.x78zum5.xdt5ytf.xg6iff7.x1n2onr6 div.x10l6tqk.x160vmok.x1eu8d0j.x1vjfegm:nth-child(2) > div.x1i10hfl.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x9f619.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz.x6s0dn4.x78zum5.xjbqb8w.x1ejq31n.xd10rxx.x1sy0etr.x17r0tee.x1ypdohk.xl56j7k.x1y1aw1k.x1sxyh0.xwib8y2.xurb0ha").click()
    time.sleep(10)
def hesap():
    hesapsoru =input("hesap ismi")
    time.sleep(10)
    searchbox1 = driver.find_element(
        "css selector","body._a3wf.system-fonts--body.segoe:nth-child(2) div.x9f619.x1n2onr6.x1ja2u2z:nth-child(2) div.x78zum5.xdt5ytf.x1n2onr6.x1ja2u2z div.x78zum5.xdt5ytf.x1n2onr6 div.x78zum5.xdt5ytf.x1n2onr6.xat3117.xxzkxad div.x78zum5.xdt5ytf.x10cihs4.x1t2pt76.x1n2onr6.x1ja2u2z:nth-child(1) div.x9f619.xnz67gz.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib:nth-child(1) div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1.xeq5yr9.x1dr59a3.xixxii4.x13vifvy.x1n327nk div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj div.x78zum5.x1q0g3np.x1gvbg2u.x1qughib.xleuxlb.xxfw5ft.x1mh60rb.x1f91t4q.x1n2onr6 div.xvb8j5.x1vjfegm div.x1cy8zhl.x9f619.x78zum5.xdt5ytf.x1gvbg2u.x1y1aw1k.xn6708d.xx6bls6.x1ye3gou.xvbhtw8.x1xgvd2v.x1o5hw5a.xaeubzz div.xh8yej3.x1iyjqo2 div:nth-child(2) div.x1n2onr6 a.x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz._a6hd > div.x9f619.x3nfvp2.xr9ek0c.xjpr12u.xo237n4.x6pnmvc.x7nr27j.x12dmmrz.xz9dl7a.xn6708d.xsag5q8.x1ye3gou.x80pfx3.x159b3zp.xdoji71.x1dejxi8.x9k3k5o.xs3sg5q.x11hdxyr.x12ldp4w.x1wj20lx.x1dn74xm.xif99yt.x172qv1o.x10djquj.x1lhsz42.xzauu7c.x1lq5wgf.xgqcy7u.x30kzoy.x9jhf4c").click()
    time.sleep(10)
    searchbox = driver.find_element("css selector","body._a3wf.system-fonts--body.segoe:nth-child(2) div.x9f619.x1n2onr6.x1ja2u2z:nth-child(2) div.x78zum5.xdt5ytf.x1n2onr6.x1ja2u2z div.x78zum5.xdt5ytf.x1n2onr6 div.x78zum5.xdt5ytf.x1n2onr6.xat3117.xxzkxad div.x78zum5.xdt5ytf.x10cihs4.x1t2pt76.x1n2onr6.x1ja2u2z:nth-child(1) div.x9f619.xnz67gz.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib:nth-child(1) div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1.xeq5yr9.x1dr59a3.xixxii4.x13vifvy.x1n327nk div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj div.x78zum5.x1q0g3np.x1gvbg2u.x1qughib.xleuxlb.xxfw5ft.x1mh60rb.x1f91t4q.x1n2onr6 div.x10l6tqk.x1u3tz30.x1ja2u2z div.xvbhtw8.xvb8j5.x9f619.x78zum5.xdt5ytf.x1dr59a3.x1odjw0f.xish69e.x1y1aw1k.x4uap5.xwib8y2.xkhd6sd.xzmilaz.x168nmei.xoqspk4.x12v9rci.xo71vjh.x1n2onr6.x1zvrr1 div.xh8yej3.x5yr21d.x78zum5.xdt5ytf.x10wlt62 div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1n2onr6.x1plvlek.xryxfnj.x1iyjqo2.x2lwn1j.xeuugli.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1 div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1d52u69.xktsk01.x1n2onr6.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1 div._aawf._aawg._aexm._abli > input._aauy")
    time.sleep(4)
    searchbox.clear()
    searchbox.send_keys(hesapsoru)
    time.sleep(4)
    searchbox.send_keys(Keys.ENTER)
    time.sleep(4)
    searchbox.send_keys(Keys.ENTER)
    time.sleep(4)
    hesap1 = driver.find_element(
        "css selector", "body._a3wf.system-fonts--body.segoe:nth-child(2) div.x9f619.x1n2onr6.x1ja2u2z:nth-child(2) div.x78zum5.xdt5ytf.x1n2onr6.x1ja2u2z div.x78zum5.xdt5ytf.x1n2onr6 div.x78zum5.xdt5ytf.x1n2onr6.xat3117.xxzkxad div.x78zum5.xdt5ytf.x10cihs4.x1t2pt76.x1n2onr6.x1ja2u2z:nth-child(1) div.x9f619.xnz67gz.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib:nth-child(1) div.xh8yej3.x1gryazu.x10o80wk.x14k21rp.x1porb0y.x17snn68.x6osk4m section.x78zum5.xdt5ytf.x1iyjqo2.x6ikm8r.xg6iff7 main.x78zum5.xdt5ytf.x1iyjqo2.x182iqb8.xvbhtw8:nth-child(1) div._aa_y._aa_z._aa_- div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1n2onr6.x1plvlek.xryxfnj.x1iyjqo2.x2lwn1j.xeuugli.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1 article.x1iyjqo2 div._ac7v._al3n:nth-child(1) div._aabd._aa8k._al3l:nth-child(1) a.x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz._a6hd div._aagu > div._aagw").click()
    time.sleep(5)
    cumleler1 =['messim be ','thiss is goat !!','I love bro','boyle devam kral',"I have goat's signed jersey"]
    kacyorumhesap = input("kaç yorum yapılsın")
    kacyorumhesap1 = int(kacyorumhesap)

    for i in range(kacyorumhesap1):
        time.sleep(4)
        try:
            hesapyorum = driver.find_element("css selector", "body._a3wf.system-fonts--body.segoe:nth-child(2) div.x1uhb9sk div.x9f619.x1n2onr6.x1ja2u2z:nth-child(1) div.x78zum5.xdt5ytf.xg6iff7.x1n2onr6 div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj:nth-child(3) div.x1qjc9v5.x9f619.x78zum5.xdt5ytf.x1iyjqo2.xl56j7k div.x1cy8zhl.x9f619.x78zum5.xl56j7k.x2lwn1j.xeuugli.x47corl div.x1ja2u2z.x1afcbsf.x1a2a7pz.x6ikm8r.x10wlt62.xdt5ytf.x1n2onr6.xl56j7k.x78zum5.x6s0dn4.x5yr21d.xh8yej3.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x47corl div.xs83m0k.xl56j7k.x1iy3rx.x1n2onr6.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xh8yej3.xjbqb8w.x1v7wizp.x1l0w46t.xa3vuyk.xw8ag78 div.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe.x1qjc9v5.xjbqb8w.x1lcm9me.x1yr5g0i.xrt01vj.x10y3i5r.x47corl.xh8yej3.x15h9jz8.xr1yuqi.xkrivgy.x4ii5y1.x1gryazu.xir0mxb.x1juhsu6:nth-child(2) article._aatb._aate._aatg._aati div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1n2onr6.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.xl56j7k div._ae65 div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1n2onr6.x1plvlek.xryxfnj.x1iyjqo2.x2lwn1j.xeuugli.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1 div._ae1k._ae2q._ae2r div._ae2s._ae3v._ae3w section._aaoe._ae5y._ae5z._ae62 div._aaof form._aidk._ak6u div._akhn > textarea.x1i0vuye.xvbhtw8.x76ihet.xwmqs3e.x112ta8.xxxdfa6.x5n08af.x78zum5.x1iyjqo2.x1qlqyl8.x1d6elog.xlk1fp6.x1a2a7pz.xexx8yu.x4uap5.x18d9i69.xkhd6sd.xtt52l0.xnalus7.x1bq4at4.xaqnwrm.xs3hnx8:nth-child(2)").click()
            time.sleep(3)
            hesapyorum.send_keys(Keys.ENTER)
            pyautogui.typewrite(random.choice(cumleler1))
            time.sleep(4)
            hesapyorum.send_keys(Keys.ENTER)
            time.sleep(8)
        except:
            hesapyorum = driver.find_element("css selector",
                                             "body._a3wf.system-fonts--body.segoe:nth-child(2) div.x1uhb9sk div.x9f619.x1n2onr6.x1ja2u2z:nth-child(1) div.x78zum5.xdt5ytf.xg6iff7.x1n2onr6 div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj:nth-child(3) div.x1qjc9v5.x9f619.x78zum5.xdt5ytf.x1iyjqo2.xl56j7k div.x1cy8zhl.x9f619.x78zum5.xl56j7k.x2lwn1j.xeuugli.x47corl div.x1ja2u2z.x1afcbsf.x1a2a7pz.x6ikm8r.x10wlt62.xdt5ytf.x1n2onr6.xl56j7k.x78zum5.x6s0dn4.x5yr21d.xh8yej3.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x47corl div.xs83m0k.xl56j7k.x1iy3rx.x1n2onr6.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xh8yej3.xjbqb8w.x1v7wizp.x1l0w46t.xa3vuyk.xw8ag78 div.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe.x1qjc9v5.xjbqb8w.x1lcm9me.x1yr5g0i.xrt01vj.x10y3i5r.x47corl.xh8yej3.x15h9jz8.xr1yuqi.xkrivgy.x4ii5y1.x1gryazu.xir0mxb.x1juhsu6:nth-child(2) article._aatb._aate._aatg._aath._aati div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1n2onr6.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.xl56j7k div._ae65 div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1n2onr6.x1plvlek.xryxfnj.x1iyjqo2.x2lwn1j.xeuugli.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1 div._ae1k._ae2q._ae2r div._ae2s._ae3v._ae3w section._aaoe._ae5y._ae5z._ae62 div._aaof form._aidk._ak6u div._akhn > textarea.x1i0vuye.xvbhtw8.x76ihet.xwmqs3e.x112ta8.xxxdfa6.x5n08af.x78zum5.x1iyjqo2.x1qlqyl8.x1d6elog.xlk1fp6.x1a2a7pz.xexx8yu.x4uap5.x18d9i69.xkhd6sd.xtt52l0.xnalus7.x1bq4at4.xaqnwrm.xs3hnx8:nth-child(2)").click()
            time.sleep(3)
            hesapyorum.send_keys(Keys.ENTER)
            pyautogui.typewrite(random.choice(cumleler1))
            time.sleep(4)
            hesapyorum.send_keys(Keys.ENTER)
            time.sleep(8)
        hesapyorumgec = driver.find_element("css selector", "body._a3wf.system-fonts--body.segoe:nth-child(2) div.x1uhb9sk div.x9f619.x1n2onr6.x1ja2u2z:nth-child(1) div.x78zum5.xdt5ytf.xg6iff7.x1n2onr6 div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj:nth-child(3) div.x1qjc9v5.x9f619.x78zum5.xdt5ytf.x1iyjqo2.xl56j7k div.x1cy8zhl.x9f619.x78zum5.xl56j7k.x2lwn1j.xeuugli.x47corl div.x1ja2u2z.x1afcbsf.x1a2a7pz.x6ikm8r.x10wlt62.xdt5ytf.x1n2onr6.xl56j7k.x78zum5.x6s0dn4.x5yr21d.xh8yej3.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x47corl div.xs83m0k.xl56j7k.x1iy3rx.x1n2onr6.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xh8yej3.xjbqb8w.x1v7wizp.x1l0w46t.xa3vuyk.xw8ag78 div:nth-child(1) div._aeap._aeaq div._aear div._aaqg._aaqh > button._abl-").click()
        time.sleep(5)

    hesapgec = driver.find_element("css selector", "body._a3wf.system-fonts--body.segoe:nth-child(2) div.x1uhb9sk div.x9f619.x1n2onr6.x1ja2u2z:nth-child(1) div.x78zum5.xdt5ytf.xg6iff7.x1n2onr6 div.x10l6tqk.x160vmok.x1eu8d0j.x1vjfegm:nth-child(2) > div.x1i10hfl.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x9f619.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz.x6s0dn4.x78zum5.xjbqb8w.x1ejq31n.xd10rxx.x1sy0etr.x17r0tee.x1ypdohk.xl56j7k.x1y1aw1k.x1sxyh0.xwib8y2.xurb0ha").click()
    time.sleep(8)

login()
while True:
    soru()