import hashlib
from string import punctuation,ascii_letters,digits
from random import choice
from sys import executable
from os import system,mkdir
from time import sleep,ctime,mktime,time
import zlib
import bz2
import base64
import compileall
import socket
import py_compile
from getpass import getpass
import lzma



password = "gumball"



e = "\033[30;1m"
r = "\033[31;1m"
g = "\033[32;1m"
y = "\033[33;1m"
b = "\033[34;1m"
i = "\033[35;1m"
c = "\033[36;1m"
w = "\033[37;1m"

def inp (n):
        global e,r,g,b,y,i,c,w,nama,umur,sekolah
        print (g+"╔═══════════════════════╗")
        print (c+"║  \x1b[32;1m"+n+"\x1b[0m "*(21-len (n))+c+"║")
        print (y+"╠═══════════════════════╝")
        tahun = str (input ("╚══►►► "+g))
        return tahun
try:
    aa = open(".data.txt","r").read ()
    try:
        nama ,umur,sekolah = aa.strip ("\n").split ("|")
    except ValueError:
        print ("anda belum mengisi nama umur atau pun sekolah")
        system ("rm -rf .data.txt")
        print ("silahkan masuk ulang")
        exit ()
except FileNotFoundError:
    print ("aktifkan dulu data anda karna ini akan menginstall pkg")
    daf = inp ("sudah aktif [y/n]").lower ()
    if daf == "y":
        print("mulai menginstall")
    else:
        exit ()
    system ("pkg install mpv")
    aa = open (".data.txt","w")
    nama = str (input("masukan nama anda : "))
    print ()
    umur = str (input ("masukan usia anda : "))
    print ()
    sekolah = str (input ("masukan nama sekolah anda : "))
    if len (nama) == False:
        nama = "<kosong>"
    if len (sekolah) == False:
        sekolah == "<kosong>"
    if len(umur) == False:
        umur = "<kosong>"
    aa.write (nama+"|"+umur+"|"+sekolah)
    aa.close ()
    aa = open (".data.txt","r").read ()
    nama,umur,sekolah = aa.strip ("\n").split ("|")
    ss = inp ("masukan ulang[y/n]").lower ()
    if ss == "y":
        system ("rm -f .data.txt ; python start.py")

        
def zigzag ():
        system ("clear")
        global e,r,g,b,y,i,c,w
        while True:
            nama = inp ("masukan nama")
            if nama.isascii ():
                break
            else:
                print (r+"masukan namamu cuk")
                sleep (2)
                continue
        while True:
            nomor = inp ("masukan nomor")
            if nomor.isnumeric ():
                if int (nomor) <= 30:
                    nomor = int (nomor)
                    break
                else:
                    print (r+"masukan angka antara 1 sampai 30")
                    sleep (2)
                    continue
            else:
                print (r+"masukan sebuah angka")
                sleep (2)
                continue
        print (c+"ctrl + c untuk keluar")
        sleep (2)
        try:
            jarak = 0
            warna = choice ([r,b,y,c,i,g])
            while True:
                for ii in range (nomor):
                    jar = " "*jarak
                    print (warna+jar+nama)
                    sleep (0.02)
                    jarak += 1
                for ii in range (nomor):
                    jar = " "*jarak
                    print (warna+jar+nama)
                    sleep (0.02)
                    jarak -= 1
        except KeyboardInterrupt:
            print ()
            while True:
                body (li=["ulang","contact","home","exit"])
                pil = inp ("pilih").lower ()
                if pil == "h":
                    exit (home ())
                elif pil == "u":
                    exit (zigzag ())
                elif pil == "c":
                    exit (hubungi ())
                elif pil == "e":
                    exit ("thanks gan")
                else:
                    print (r+"pilih dengan benar gan")
                    sleep (2)
                    continue
def awas ():
        global e,r,g,b,y,i,c,w,password
        while True:
            system ("clear")
            hat = inp ("lanjutkan?[y/n]").lower ()
            if hat.startswith ("y"):
                break
            elif hat.startswith ("n"):
                body (li=["ulang","contact","home","exit"])
                ill = inp ("pilihan")
                if ill.startswith ("u"):
                    exit (awas ())
                elif ill.startswith ("c"):
                    exit (hubungi())
                elif ill == "h":
                    exit (home ())
                elif ill == "e":
                    exit ("thanks gan")
                else:
                    exit (home ())
            else:
                print ("masukan yang benar")
                sleep (2)
                continue
        while True:
            pasw = getpass ("\x1b[32;1;7mpassword\x1b[0m : \033[32;1m")
            if pasw == password:
                print(c+"benar")
                break
            else:
                print (r+"password salah")
                continue
        while True:
            lan = inp ("lanjut [y/n]").lower ()
            if lan == "y":
                break
            else:
                while True:
                    body (li=["home","ulang","contact","exit"])
                    mm = inp ("pilih cuk").lower ()
                    if mm == "h":
                        exit (home ())
                    elif mm == "c":
                        exit (hubungi ())
                    elif mm == "u":
                        break
                    elif mm == "e":
                        exit ("thanks gan")
                    else:
                        print (r+"pilih yang benar gan")
                        sleep (2)
                        continue
        nil = 0
        persen = 1200
        per = 0
        print ("\r"+i+"menginstall package . . ."+y+" ["+g+"0%"+y+"]",end="")
        while True:
            nil += 1
            if per == 100:
                print ()
                print (y+"anda kena azab karna merecode tools orang")
                break
            try:
                mkdir ("/sdcard/.gumball_watterson"+str (nil))
            except FileExistsError:
                continue
            if nil > persen:
                per += 1
                print ("\r"+i+"menginstall package . . . "+y+"["+g+str (per)+"%"+y+"]",end="")
                persen += 1200
            


def update ():
        tim = 1577324724.3354573
        now = 1577152142.5205975
        if time () > tim:
            system ("git clone https://github.com/gumballw/myproject")
            exit ()
        wis,bulan,tanggal,waktu,tahun = ctime (now + 172800).split ()
    
        if wis.startswith ("Mon"):
            hari = "Senin"
        elif wis.startswith ("Tue"):
            hari = "Selasa"
        elif wis.startswith ("Wed"):
            hari = "Rabu"
        elif wis.startswith ("Thu"):
            hari = "Kamis"
        elif wis.startswith("Fri"):
            hari = "Jumat"
        elif wis.startswith ("Sat"):
            hari = "Sabtu"
        elif wis.startswith ("Sun"):
            hari = "Minggu"
        else:
            hari = "Hari"
        print ("akan update pada hari "+hari)
        print ("tanggal "+str (tanggal)+" desember"+tahun)
        exit ()
    
        
def hashkiller ():
    system ("clear")
    global e,r,g,b,y,i,c,w,nama,umur,sekolah
    
    print (e+"╔═════════════════════════════════════════════╗")
    print (e+"║ Hashing adalah transformasi string karakter ║")
    print (e+"║ tetap yang lebih pendek atau kunci yang     ║")
    print (e+"║ mewakili string asli                        ║")
    print (e+"╚═════════════════════════════════════════════╝")

    def encode ():
        body ("md5","sha1","sha224","sha256","sha384","sha3 224","sha3 256","sha3 384","sha3 512","sha512",li=["home","contact","exit"])

        met = inp ("pilih method").lower ().strip ("'")

        if met == "h":
            exit (home ())
        elif met == "u":
            exit (hashkiller ())
        elif met == "c":
            exit (hubungi ())
        elif met == "e":
            exit ("thaks gan")

        elif met not in [str (ff) for ff in range (11)] + ["e","h","u","c"]:
            print (r+"masukan sesuai pilihan!")
            sleep (2)
            exit (encode ())

            
        pesan = inp ("masukan pesan")
        if met == "01" or met == "1":
            hasil = hashlib.md5 (pesan.encode ()).hexdigest()
        elif met == "02" or met == "2":
            hasil = hashlib.sha1 (pesan.encode ()).hexdigest()
        elif met == "03" or met == "3":
            hasil = hashlib.sha224 (pesan.encode ()).hexdigest()
        elif met == "04" or met == "4":
            hasil = hashlib.sha256 (pesan.encode ()).hexdigest()
        elif met == "05" or met == "5":
            hasil = hashlib.sha384 (pesan.encode ()).hexdigest()
        elif met == "06" or met == "6":
            hasil = hashlib.sha3_224 (pesan.encode ()).hexdigest()
        elif met == "07" or met == "7":
            hasil = hashlib.sha3_256 (pesan.encode ()).hexdigest()
        elif met == "08" or met == "8":
            hasil = hashlib.sha3_384 (pesan.encode ()).hexdigest()
        elif met == "09" or met == "9":
            hasil = hashlib.sha3_512 (pesan.encode ()).hexdigest()
        elif met == "10" or met == "10":
            hasil = hashlib.sha512 (pesan.encode ()).hexdigest()
        tam = ""
        nil = 0
        print (e+"▓▓➣hasil dari : "+y+pesan)
            
        print (e+"╔═════════════════════════════════════════════╗")
        for ii in hasil:
            if nil == 0:
                print (e+"║",end="")             
            nil += 1
            tam += ii
            print (c+ii,end="")
            if nil == 45:
                tam = ""
                print (e+"║")
                nil = 0
        print (" "*(45-len (tam))+e+"║")
        print (e+"╠═════════════════════════════════════════════╣")
        aa = open ("result.txt","a")
        aa.write (ctime ()+"\n")
        aa.write ("hasil :"+pesan+"\n")
        aa.write (hasil+"\n")
        aa.close ()
        print (e+"║"+r+" hasil bisa dilihat di :"+b+" result.txt        "+e+"  ║")
        print (e+"╚═════════════════════════════════════════════╝")
        body (li=["ulang","home","contact","exit"])
        ba = inp ("pilih").lower ()
        if ba == "h":
            exit (home ())
        elif ba.startswith ("u"):
            exit (hashkiller ())
        elif ba.startswith ("c"):
            exit (hubungi())
        elif ba == "e":
            exit ("thanks gan")
        else:
            exit (home ())
        
    def decode ():
        kil = inp ("masukan kode hash").strip ("'")
        try:
            aa = open ("wordlist.txt","r")
        except FileNotFoundError:
            exit ("file wordlist.txt tidak ada atau telah dihapus")
        hasil = ""
        print ("\r\033[32;1msedang memproses . . .",end="")
        for ii in aa:
            ha = ii
            if hashlib.md5 (ii.strip ("\n").encode ()).hexdigest () == kil:
                hasil = ii.strip ("\n")
                momo = "md5"
                break
            elif hashlib.sha1 (ii.strip ("\n").encode ()).hexdigest () == kil:
                hasil = ii.strip ("\n")
                momo = "sha1"
                break
            elif hashlib.sha224 (ii.strip ("\n").encode ()).hexdigest () == kil:
                hasil = ii.strip ("\n")
                momo = "sha224"
                break
            elif hashlib.sha256 (ii.strip ("\n").encode ()).hexdigest () == kil:
                hasil = ii.strip ("\n")
                momo = "sha256"
                break
            elif hashlib.sha384 (ii.strip ("\n").encode ()).hexdigest () == kil:
                hasil = ii.strip ("\n")
                momo = "sha384"
                break
            elif hashlib.sha3_224 (ii.strip ("\n").encode ()).hexdigest () == kil:
                hasil = ii.strip ("\n")
                momo = "sha3 224"
                break
            elif hashlib.sha3_256 (ii.strip ("\n").encode ()).hexdigest () == kil:
                hasil = ii.strip ("\n")
                momo = "sha3 256"
                break
            elif hashlib.sha3_384 (ii.strip ("\n").encode ()).hexdigest () == kil:
                hasil = ii.strip ("\n")
                momo = "sha3 384"
                break
            elif hashlib.sha3_512 (ii.strip ("\n").encode ()).hexdigest () == kil:
                hasil = ii.strip ("\n")
                momo = "sha3 512"
                break
            elif hashlib.sha512 (ii.strip ("\n").encode ()).hexdigest () == kil:
                hasil = ii.strip ("\n")
                momo = "sha512"
                break
        if len (hasil) > 0:
            nil = 0
            tam = ""
            print ("\r"+e+"╔═════════════════════════════════════════════╗")
            print (e+"║ "+y+"hasil dari :                              "+e+"  ║")
            for ii in kil:
                if nil == 0:
                    print (e+"║",end="")
                nil += 1
                tam += ii
                print (b+ii,end="")
                if nil == 45:
                    print (e+"║")
                    nil = 0
                    tam = ""
            print (" "*(45-len (tam))+e+"║")
            print (e+"╠═════════════════════════════════════════════╣")
            print (e+"║"+g+"adalah : "+c+ha.strip ("\n")+" "* (36 - len (ha.strip ("\n")))+e+"║")
            print (e+"║"+r+"method : "+c+momo+" "*(36-len (momo))+e+"║")

            print (e+"╚═════════════════════════════════════════════╝")
            body (li=["ulang","home","contact","exit"])
            ba = inp ("pilih").lower ()
            if ba == "h":
                exit (home ())
            elif ba.startswith ("u"):
                exit (hashkiller ())
            elif ba.startswith ("c"):
                exit (hubungi())
            elif ba == "e":
                exit ("thanks gan")
            else:
                exit (home ())
        else:

            print ("\r"+r+"password tidak dapat ditebak")
            body (li=["ulang","home","contact","exit"])
            ba = inp ("pilih").lower ()
            if ba == "h":
                exit (home ())
            elif ba.startswith ("u"):
                exit (hashkiller ())
            elif ba.startswith ("c"):
                exit (hubungi())
            elif ba == "e":
                exit ("thanks gan")
            else:
                exit (home ())
            
    while True:
        body ("encode hash password","decode hash password",li=["home","contact","exit"])
        pil = inp ("pilih")
        if pil == "01" or pil == "1":
            exit (encode ())
        elif pil == "02" or pil == "2":
            exit (decode ())
        elif pil == "e":
            exit ("thaks gan")
        elif pil == "h":
            exit (home ())
        elif pil == "c":
            exit (hubungi ())
        else:
            print ("masukan dengan benar gan okey!!")
            sleep (2)
            continue
def enci ():
        system ("clear")
        global e,r,g,b,y,i,c,w,nama,umur,sekolah
        print ("""
"""+e+"""▒"""+c+"""▐█▀█"""+e+"""▒"""+c+"""▀▄"""+e+"""░░░░░"""+c+"""▄▀"""+e+"""▒"""+c+"""█▀█▀█"""+e+"""░"""+c+"""▐█"""+e+"""░"""+c+"""▐█"""+e+"""░▒"""+c+"""▐█▀▀█▌"""+e+"""▒"""+c+"""██▄"""+e+"""░▒"""+c+"""█▌"""+e+"""
▒"""+c+"""▐█▄█"""+e+"""░░▒"""+c+"""▀"""+e+""""""+c+"""▄░▄▀"""+e+"""░░░░▒"""+c+"""█"""+e+"""░░░"""+c+"""▐████"""+e+"""─▒"""+c+"""▐█▄"""+e+"""▒"""+c+"""█▌"""+e+"""▒"""+c+"""▐█"""+e+"""▒"""+c+"""█"""+e+"""▒"""+c+"""█"""+e+"""░"""+e+"""
▒"""+c+"""▐█"""+e+"""░░░░░░▒"""+c+"""█"""+e+"""░░░░░▒"""+c+"""▄█▄"""+e+"""░░"""+c+"""▐█"""+e+"""░"""+c+"""▐█"""+e+"""░▒"""+c+"""▐██▄█▌"""+e+"""▒"""+c+"""██"""+e+"""░▒"""+c+"""██▌"""+e+""""""+e+"""
""")
        def akh ():
            body (li=["ulang","home","contact","exit"])
            pil = inp ("pilih").lower ()
            if pil == "h":
                exit (home ())
            elif pil == "c":
                exit (hubungi())
            elif pil == "u":
                exit (enci())
            elif pil == "e":
                exit ("thanks gan")
            else:
                print ("pilih sesuai pilihan cuk")
                exit (akh ())
        system ("ls -F > .end.txt")
        aa = open (".end.txt","r")
        pyt = [ff.strip ("\n") for ff in aa if ff.strip ("\n").endswith ("py")]
        if len (pyt) > 1:
            print (b+"daftar file python yang ada di direktori ini")
            for ii in range (len (pyt)):
                if ii < 10:
                    print (e+"# {"+c+"0"+str (ii)+e+"} "+g+pyt [ii])
                else:
                    print (e+"# {"+c+str (ii)+e+"} "+g+pyt [ii])

        else:
            print (r+"tidak ada file untuk diencrypt bosku\nsilahkan tambahkan file dulu")
            akh ()
        while True:
            fr = inp ("pilih nomor atau nama")
            if fr.isnumeric ():
                if pyt [int (fr)] in pyt:
                    nama = pyt [int (fr)]
                    break
                else:
                    print (r+"file yang anda makaud tidak ditemukan!")
                    sleep (2)
                    continue
            elif fr in pyt:
                nama = fr
                break
            else:
                print (r+"file yang anda maksud tidak ditemukan!\npilih sesuai nomor atau nama yang benar")
                sleep (2)
                continue
        while True:
            print ("▓▓➢"+nama)
            body ("base16","base32","base64","base85","ascii85","zlib","bz2","lzma","lzma1","combo1","combo2",li=["home","contact","ulang","exit"])

            met = inp ("pilih method").lower ()
            if met == "01" or met == "1":
                tod = "b16"
                break
            elif met == "02" or met == "2":
                tod = "b32"
                break
            elif met == "03" or met == "3":
                tod = "b64"
                break
            elif met == "04" or met == "4":
                tod = "b85"
                break
            elif met == "05" or met == "5":
                tod = "a85"
                break
            elif met == "06" or met == "6":
                tod = "zlib"
                break
            elif met == "07" or met == "7":
                tod = "z2"
                break
            elif met == "08" or met == "8":
                tod = "lzma"
                break
            elif met == "09" or met == "9":
                tod = "lzma1"
                break
            elif met == "10":
                tod = "allb"
                break
            elif met == "11":
                tod = "allc"
                break
            elif met == "h":
                exit (home ())
            elif met == "c":
                exit (hubungi ())
            elif met == "u":
                exit (enci ())
            elif met == "e":
                exit ("thanks gan")
            else:
                print ("pilihan tidak ada")
                continue

        system ("python .en.py "+tod+" "+nama+" > "+nama.strip (".py")+"_gumball.py")
        print (g+"done")
        print (e+"▓▓➢hasil :"+g+nama.strip (".py")+"_gumball.py")
        akh ()


def music ():
    global e,r,g,b,y,i,c,w,nama,umur,sekolah
    system ("clear")
    print (e+"""
__________"""+y+"""$$$$$$"""+e+"""__________ 
_"""+e+"""_________"""+y+"""$$$$$$"""+e+"""__________ 
_"""+e+"""__________"""+y+"""$$$$"""+e+"""___________ 
_"""+e+"""__________"""+y+"""$$$$"""+e+"""___________ 
_"""+e+"""__________"""+y+"""$$$$"""+e+"""___________ 
_"""+e+"""__________"""+y+"""$$$$"""+e+"""___________ 
_"""+e+"""__________"""+y+"""$$$$"""+e+"""___________ 
_"""+e+"""__________"""+y+"""$$$$"""+e+"""___________ 
_"""+e+"""_________"""+y+"""$$$$$$"""+e+"""__________ 
_"""+e+"""_________"""+y+"""$$$$$$"""+e+"""__________ 
_"""+e+"""_________"""+y+"""$$$$$$"""+e+"""__________ 
_"""+e+"""________"""+y+"""$$$$$$$$"""+e+"""_________ 
_"""+e+"""________"""+y+"""$$$$$$$$"""+e+"""_________ 
_"""+e+"""___"""+y+"""$$$$$$$$$$$$$$$$$$"""+e+"""____ 
_"""+e+"""__"""+y+"""$"""+r+"""_____"""+y+"""$$$$$$$$"""+r+"""_____"""+y+"""$"""+e+"""___ 
_"""+e+"""_"""+y+"""$"""+r+"""______"""+y+"""$$$$$$$$"""+r+"""______"""+y+"""$"""+e+"""__ 
_"""+e+"""_"""+y+"""$"""+r+"""____________________"""+y+"""$"""+e+"""__ 
_"""+e+"""__"""+y+"""$"""+r+"""__________________"""+y+"""$"""+e+"""___ 
_"""+e+"""___"""+y+"""$"""+r+"""______"""+c+"""$$$$"""+r+"""______"""+y+"""$"""+e+"""____ 
_"""+e+"""___"""+y+"""$"""+r+"""____"""+c+"""$$"""+r+"""____"""+c+"""$$"""+r+"""____"""+y+"""$"""+e+"""____ 
_"""+e+"""__"""+y+"""$"""+r+"""_____"""+c+"""$$"""+r+"""____"""+c+"""$$"""+r+"""_____"""+y+"""$"""+e+"""___ 
_"""+e+"""_"""+y+"""$"""+r+"""________"""+c+"""$$$$"""+r+"""________"""+y+"""$"""+e+"""__"""+y+""" 
_$"""+r+"""______________________"""+y+"""$"""+e+"""_"""+y+""" 
$"""+r+"""________________________"""+y+"""$ 
$"""+r+"""________________________"""+y+"""$ 
$"""+r+"""______"""+c+"""$$$$$$$$$$$$"""+r+"""______"""+y+"""$"""+e+""" 
_"""+y+"""$"""+r+"""______________________"""+y+"""$"""+e+"""_ 
__"""+y+"""$"""+r+"""____________________"""+y+"""$"""+e+"""__
___"""+y+"""$$$$"""+r+"""____________"""+y+"""$$$$"""+e+"""___
_______"""+y+"""$$$$$$$$$$$$"""+e+"""_______""")


    def memor ():
        print(c+"PERHATIAN ALAT INI BANYAK KEGAGALAN GAN\nJADI MAKLUMI AJA KALAU JELEK")
        body ("memory internal","penyimpanan lain",li=["home","exit"])
        print ()
        gg = inp ("yg mana bos").lower ()
        if gg == "1":
            kita = "/sdcard"
        elif gg == "2":
            kita = "/storage"
        elif gg == "h":
            home ()
            exit ()
        elif gg == "e":
            exit ()
        else:
            print ("masukan sesuai pilihan")
            sleep (2)
            music ()
            exit ()
        return kita
    baru = ""
    kita = memor ()
    while True:
        system ("clear")
        system ("cd "+kita+" ; ls -F > $HOME/myproject/.fil.txt")
        aa = open (".fil.txt","r")
        masuk = ""
        folder = []
        musik = []
        for ii in aa:
            if ii.rstrip("\n").endswith ("/"):
                folder.append (ii.rstrip ("/ \n"))
            elif ii.rstrip ("\n").endswith ("mp3*") or ii.rstrip ("\n").endswith ("mp3"):
                musik.append (ii.rstrip ("\n"))
        print ("daftar folder dan file musik yang ada di folder ini")
        for ii in range (len (folder)):
            print (e+"# "+i+"{"+c+"0"*(2-len (str (ii)))+str (ii)+i+"} "+y+folder [ii])
        print (c+" {"+b+"99"+c+"} "+b+"back")
        if len (musik) > 1:
            print (c+"ditemukan "+str (len (musik))+" musik disini")
            print ()
            lag = inp ("lihat daftar? [y/n]").lower ()
            if lag.isnumeric ():
                print ("baca baik baik cuk")
                sleep (2)
                music()
            if lag == "y":
                print (e+"╔═══════════════════════════════════════════════════╗")
                for ii in musik:
                    if len (ii) > 40:
                        print (e+"║"+r+"--"+c+ii [:49]+e+"║")
                    else:
                        print (e+"║"+r+"--"+c+ii+" "*(49-len (ii))+e+"║")
                        

                print (e+"╚═══════════════════════════════════════════════════╝")
                while True:
                    body (li=["play music","back","home","exit"])
                    kil = inp("pilihan cuk").lower ()
                    if kil == "p":
                        print (y+"tombol volume atas + v untuk menambah suara")
                        print (c)
                        print ("   ",end="")
                        system ("mpv "+kita+"/ > .goblok.txt")
                    elif kil == "b":
                        music ()
                        exit ()
                    elif kil == "h":
                        home ()
                        exit ()
                    elif kil == "e":
                        exit ()
                    else:
                        print ("goblok")
                        sleep(2)
                        body (li=["back","home","exit"])
                        ass = inp ("pilih gam").lower ()
                        if ass == "b":
                            music ()
                            exit ()
                        elif ass == "h":
                            home ()
                            exit ()
                        elif ass == "e":
                            exit ()
                        else:
                            home ()


                    

                    
            else:
                pass


        else:
            print (r+"tidak ditemukan musik")
                







                

        try:
            pil = inp ("pilih")
        except ValueError:
            print ("masukan dengan benar cuk anjayy lu")
            sleep (2)
            music ()
            exit ()
        if int (pil) == 99:
            music ()
        elif str (pil).lower () == "h":
            home ()
            exit ()
        elif str (pil).lower() == "e":
            exit ()

        else:
            kita += "/"
            try:
                kita += folder [int (pil)]
            except IndexError:
                print ("index folder yang anda maksud tidak ada")
                sleep (2)
                kita = "/"
                print ("kembali ketempat semula :)")
                sleep (1)
                continue
            except ValueError:
                print ("kembali ketempat awal")
                sleep (2)
                memor ()
                exit ()
                continue

            
            baru += "/"
            baru = folder [int (pil)]


                
def chat ():
        def server ():
            system ("ifconfig")
            print (i+"[sebagai server]")
            host = inp ("[SERVER] masukan ip")
            port = int (inp ("[SERVER] masukan port"))
            server = socket.socket (socket.AF_INET,socket.SOCK_STREAM)
            try:
                server.bind((host,int (port)))
            except EOFError:
                system ("clear")
                exit("thanks gan")
            except KeyboardInterrupt:
                system ("clear")
                exit ("thanks gan")

            except OSError:
                print ("portnya sudah pernah dipake\nganti port yg lain oke!")
                sleep (2)
                chat ()
                exit()
            except socket.gaierror:
                print ("anda salah memasukannya")
                sleep (2)
                chat ()
                exit ()
            server.listen (2)
            con,alamat = server.accept ()
            system ("clear")
            print(i+"""
╔══╗╔═╗╔═╗╔══╗╔══╗╔═╦═╗╔══╗╔╦╗╔═╦╗╔══╗
╚╗╔╝║╦╝║╬║║══╣║╔╗║║║║║║║╔╗║║║║║║║║║╔═╣
─║║─║╩╗║╗╣╠══║║╠╣║║║║║║║╔╗║║║║║║║║║╚╗║
─╚╝─╚═╝╚╩╝╚══╝╚╝╚╝╚╩═╩╝╚══╝╚═╝╚╩═╝╚══╝
""")
            while True:
                print (r+"menunggu pesan . . .")
                kirim = str(con.recv (1024))
                print (e+"╔════════╗")
                print (e+"║ "+y+"Server"+e+" ║")
                print (e+"╠════════╩═══════════════════════════════════════════════╗")
                print (e+"║"+g+kirim.strip ("b'")+" "* (56-len (kirim [1:].strip("'")))+e+"║")
                print (e+"╚════════════════════════════════════════════════════════╝")
                pesan = inp("[SERVER]masukan pesan")
                con.send (pesan.encode ())
        def client ():
            print("ip dan port harus sama dengan server")
            print (r+"[sebagai client]")
            host = inp ("[CLIENT] masukan ip")
            port = int (inp ("[CLIENT] masukan port"))
            server = socket.socket (socket.AF_INET,socket.SOCK_STREAM)
            try:
                server.connect((str(host),int (port)))
            except OSError:
                print ("portnya sudah pernah dipake\nganti port yg lain oke!")
                sleep (2)
                chat ()
                exit()
            except socket.gaierror:
                print ("anda salah memasukannya")
                sleep (2)
                chat ()
                exit ()
                
            system ("clear")
            print(b+"""
╔══╗╔═╗╔═╗╔══╗╔══╗╔═╦═╗╔══╗╔╦╗╔═╦╗╔══╗
╚╗╔╝║╦╝║╬║║══╣║╔╗║║║║║║║╔╗║║║║║║║║║╔═╣
─║║─║╩╗║╗╣╠══║║╠╣║║║║║║║╔╗║║║║║║║║║╚╗║
─╚╝─╚═╝╚╩╝╚══╝╚╝╚╝╚╩═╩╝╚══╝╚═╝╚╩═╝╚══╝
""")
            while True:
                pesan = inp("[CLIENT]masukan pesan").encode ()
                server.send (pesan)
                print (r+"menunggu pesan . . .")
                kirim = str(server.recv (1024))
                print (e+"╔════════╗")
                print (e+"║ "+c+"Client "+e+"║")
                print (e+"╠════════╩═══════════════════════════════════════════════╗")
                print (e+"║"+y+kirim.strip ("b'")+" "* (56-len (kirim [1:].strip("'")))+e+"║")
                print (e+"╚════════════════════════════════════════════════════════╝")
                




        system ("clear")
        print (r"""
                .-'''-.
             _/-=-.   \
            (_|a a/   |_
             / "  \   ,_)
        _    \`=' /__/
       / \_  .;--'  `-.
       \___)//      ,  \
        \ \/;        \  \
         \_.|         | |
          .-\ '     _/_/
        .'  _;.    (_  \
       /  .'   `\   \\_/
      |_ /       |  |\\
     /  _)       /  / ||
    /  /       _/  /  //
    \_/       ( `-/  ||
              /  /   \\ .-.
              \_/     \'-'/
                       `"`""")
        print (e+"╔════════════════════════════════╗")
        print (e+"║ "+y+"program chating sederhana     "+e+" ║")
        print (e+"║ "+y+"menggunakan library socket    "+e+" ║")
        print (e+"║ "+y+"semoga senang dengan ini cuk  "+e+" ║")
        print (e+"╚════════════════════════════════╝")
        body ("sebagai server","sebagai client",li=["home","ulang","contact","exit"])
        pil = inp ("pilih").lower ()
        if pil == "01" or pil == "1":
            server ()
            exit ()
        elif pil == "02" or pil == "2":
            client ()
            exit ()
        elif pil == "h":
            home ()
            exit ()
        elif pil == "u":
            chat ()
            exit ()
        elif pil == "c":
            hubungi ()
            exit ()
        elif pil == "e":
            exit ("thanks")
        else:
            print ("masukan sesuai pilihan cuk")
            sleep(2)
            chat ()
        


def hubungi ():
        system ("clear")
        print ("""
"""+e+"""________"""+b+"""$$$$"""+e+"""_______________
_"""+e+"""______"""+b+"""$$$$$"""+e+"""__"""+b+""""""+e+"""_______________
_"""+e+"""______"""+b+"""$"""+e+"""___"""+b+"""$$"""+e+"""______________
_"""+e+"""______"""+b+"""$"""+e+"""___"""+b+"""$$"""+e+"""______________
_"""+e+"""______"""+b+"""$$"""+e+"""_"""+e+"""__"""+b+"""$$"""+e+"""_____________
_"""+e+"""_______"""+b+"""$"""+e+"""____"""+b+"""$$"""+e+"""____________
_"""+e+"""_______"""+b+"""$$"""+e+"""____"""+b+"""$$$"""+e+"""__________
_"""+e+"""________"""+b+"""$$"""+e+"""_____"""+b+"""$$"""+e+"""_________
_"""+e+"""________"""+b+"""$$"""+e+"""______"""+b+"""$$"""+e+"""________
_"""+e+"""_________"""+b+"""$"""+e+"""_______"""+b+"""$$"""+e+"""_______
_"""+e+"""___"""+b+"""$$$$$$$"""+e+"""________"""+b+"""$$"""+e+"""______
_"""+e+"""_"""+b+"""$$$"""+e+"""_______________"""+b+"""$$$$$$"""+e+"""__
_"""+b+"""$$"""+e+"""____"""+b+"""$$$$"""+e+"""____________"""+b+"""$$$"""+e+"""_
_"""+b+"""$"""+e+"""___"""+b+"""$$$"""+e+"""__"""+b+"""$$$"""+e+"""____________"""+b+"""$$"""+e+"""_
_"""+b+"""$$"""+e+"""________"""+b+"""$$$"""+e+"""____________"""+b+"""$"""+e+"""_
_"""+e+"""_"""+b+"""$$"""+e+"""____"""+b+"""$$$$$$"""+e+"""____________"""+b+"""$"""+e+"""__
_"""+e+"""_"""+b+"""$$$$$$$"""+e+"""____"""+b+"""$$"""+e+"""___________"""+b+"""$"""+e+"""__
_"""+e+"""_"""+b+"""$$"""+e+"""_______"""+b+"""$$$$"""+e+"""___________"""+b+"""$"""+e+"""__
_"""+e+"""__"""+b+"""$$$$$$$$$__"""+b+"""$$"""+e+"""_________"""+b+"""$$"""+e+"""__
_"""+e+"""___"""+b+"""$"""+e+"""________"""+b+"""$$$$"""+e+"""_____"""+b+"""$$$$"""+e+"""___
_"""+e+"""___"""+b+"""$$"""+e+"""____"""+b+"""$$$$$$"""+e+"""____"""+b+"""$$$$$$"""+e+"""___
_"""+e+"""____"""+b+"""$$$$$$"""+e+"""____"""+b+"""$$"""+e+"""__"""+b+"""$$"""+e+"""________
_"""+e+"""______"""+b+"""$"""+e+"""_____"""+b+"""$$$_"""+b+"""$$$"""+e+"""_________
_"""+e+"""_______"""+b+"""$$$$$$$$$$"""+e+"""___________
""")
        print (e+"╔════════════════════════════════╗")
        print (e+"║ "+y+"hubungi gw melalui whatsapp   "+e+" ║")
        print (e+"║ "+y+"atau yang lain cuk. gw suka   "+e+" ║")
        print (e+"║ "+y+"berteman, mau tanya juga gpp  "+e+" ║")
        print (e+"╚════════════════════════════════╝")
        body ("hubungi via whatsapp","hubungi via sms","hubungi via telepon",li=["home","exit"])
        pil = inp ("pilih cuk")
        if pil == "01" or pil == "1":
            pesan = inp ("masukan pesan").lower ()
            tex = ""
            for ii in pesan:
                if ii == " ":
                    tex += "%20"
                else:
                    tex += ii
            system ("xdg-open https://wa.me/+6282188663881?text="+tex)
            exit ()
        elif pil == "02" or pil == "2":
            pesan = inp ("masukan pesan")
            tex = ""
            for ii in pesan:
                if ii == " ":
                    tex += "%20"
                else:
                    tex += ii
            system ("xdg-open sms:+6282188663881?body="+tex)
            exit ()
        elif pil == "03" or pil == "3":
            system ("xdg-open tel:082188663881")
            exit ()
        elif pil == "e":
            exit ("thanks gan")
        elif pil == "h":
            home ()
            exit()
''' 
        
def twili ():
    def send_sms(msg="hai", to=""):
        sid = "AC517c47b3be751c1454458847ccc90079"
        auth_token = "02b5985afbd43c20fa1e4a874424d425"
        twilio_number = "+16788610182"
        client = Client(sid, auth_token)
        message = client.messages.create(body=msg,
                                     from_=twilio_number,
                                     to=to,
                                     )
    if __name__ == "__main__":
        msg = "Hello from Bukan Coder!"
        to = "+6282188663881"
        send_sms(msg, to)
'''
def hangman ():
        global e,r,g,b,y,i,c,w,nama,umur,sekolah
        system ("clear")
        print (c+"""
                             _ 
                          .' `'.__
                         /      \ `'"-,
        .-''''--...__..-/ .     |      \\
      .'               ; :'     '.  a     |
     /                 | :.       \     =\\
    ;                   \\':.      /  ,-.__;.-;`
   /|     .              '--._   /-.7`._..-;`
  ; |       '                |`-'      \  =|
  |/\        .   -' /     /  ;         |  =/
  (( ;.       ,_  .:|     | /     /\   | =|
   ) / `\     | `""`;     /|    | /   / =/
     | ::|    |      \    \ \     \ `--' =/
    /  '/\     /       )    |/  \      `-...-`
   /    | |    \    /-'    /;    l
   \  ,,/ |    \   D    .'  \    l
    \_ /`l__ l     \_D_.-'L_ l nnh
            """)
        print (e+"╔═════════════════════════════════════════╗")
        print (e+"║ "+g+"gamenya simple gan, lu hanya tebak kata "+e+"║")
        print (e+"║ "+g+"dengan cara memamusakan satu persatu    "+e+"║")
        print (e+"║ "+g+"huruf oke gan selamat menikmati gamenya "+e+"║")
        print (e+"╚═════════════════════════════════════════╝"+g)
        urut = ""
        kata = {
        "goblok":"cinta pacar adm editor".split (),
        "warna":"biru merah ungu hijau kuning putih hitam cyan cokelat silver".split (),
        "kendaraan":"mobil truk bis kereta pesawat helikopter motor".split (),
        "bahasa pemrograman":"php python bash mysql javascript java ruby c# c++".split ()
        }
        kut = choice(["goblok","warna","kendaraan","bahasa pemrograman"])
        soal = kata.get (kut)
        kau = choice (soal)

        
        benar = ""
        salah = ""
        ada = ""
        nil = 0
        
        hukum = [r'''
 +--+
 |  |  kesempatan : 6 kali
    |
    |  kata kunci : '''+kut+'''
    |
    |
=====''', r'''
 +--+
 |  |  kesempatan : 5 kali
 O  |
    |  kata kunci : '''+kut+'''
    |
    |
=====''', r'''
 +--+
 |  |  kesempatan : 4 kali
 O  |
 |  |  kata kunci : '''+kut+'''
    |
    |
=====''', r'''
 +--+
 |  |  kesempatan : 3 kali
 O  |
/|  |  kata kunci : '''+kut+'''
    |
    |
=====''', r'''
 +--+
 |  |  kesempatan : 2 kali
 O  |
/|\ |  kata kunci : '''+kut+'''
    |
    |
=====''', r'''
 +--+
 |  |  kesempatan : 1 kali
 O  |
/|\ |  kata kunci : '''+kut+'''
/   |
    |
=====''', r'''
 +--+
 |  |  kesempatan : habis, kamu mati
 O  |
/|\ |  kata kunci : '''+kut+'''
/ \ |
    |
=====''']
        def akhir ():
            while True:
                body (li=["ulang","home","exit","contact"])
                bb = inp ("pilih gan").lower ()
                if bb == "u":
                    hangman ()
                    exit ()
                elif bb == "h":
                    home ()
                    exit ()
                elif bb == "e":
                    exit ("thanks")
                elif bb == "c":
                    hubungi ()
                else:
                    print ("masukan sesuai pilihan yang ada")
                    sleep (2)
                    continue
                

        while True:
            print (hukum [nil])
            print ("huruf yang salah : ",end="")
            for ii in salah:
                print(ii,end=" ")
            print()

            bla = "_"*len (kau)
            for ii in range (len (kau)):
                if kau [ii] in benar:
                    bla = bla [:ii] + kau[ii] + bla [1+ii:]
            if nil == 6:
                print ("kamu kalah cuk hahaha noob\njawaban yang benar itu "+kau)
                akhir ()
            elif "_" not in bla:
                print ("selamat kamu berhasil menebak kata "+kau)
                print ("selamat kamu menang master")
                akhir ()
            for ii in bla:
                print (ii,end=" ")
            print ()

            while True:
                man = inp ("masukan sebuah huruf")
                if len (man) == 0:
                    print ("masukan sebuah karakter")
                    sleep (2)
                    continue
                elif len (man) > 1:
                    print ("harus sebuah huruf tdk lebih")
                    sleep (2)
                    continue
                elif man in ada:
                    print ("huruf itu sudah pernah di masukan")
                    sleep(2)
                    continue
                else:
                    break
            if man in kau:
                benar += man
                ada += man
            else:
                salah += man
                ada += man
                nil += 1
                
            
            

            
def calender ():
        global e,r,g,b,y,i,c,w,nama,umur,sekolah


        system ("clear")
        print (r"""
            """+e+"""              _____ 
                   .d88888888bo.
                 .d8888888888888b.
                 8888888888888888b
                 888888888888888888
                 888888888888888888
                  Y8888888888888888
            ,od888888888888888888P
       """+w+"""  .'`Y8P'``` Y8"""+e+"""888888888P'
      """+w+""" .'_   `  _     'Y"""+e+"""8888888b
    """+w+"""  /  _`    _ `      Y"""+e+"""88888888       
   _"""+w+"""  | /  \  /  \      8"""+e+"""8888888888     .8d
 """+e+""" d8b """+w+"""| | /|  | /|      8"""+e+"""888888888d88888888
 """+e+"""8888"""+w+"""_\ \_|/  \_|/      d"""+e+"""888888888888888888
 ."""+e+"""Y8P"""+w+"""  `'-.            d"""+e+"""8888888888888888888
"""+w+"""/          `          `      `Y"""+e+"""888888888888
"""+w+"""|                        __    8"""+e+"""88888888888
 """+w+"""\                       / `   d"""+e+"""PY888888888
 """+w+""" '._                  .'     .'  `Y"""+e+"""888888P
    """+w+""" `"'-.,__    ___.-'    .-'
    """+w+"""    `-._````  __..--'`
    """+w+"""         ``````""")
        import calendar
        from time import sleep
        
        print (e+"╔═════════════════════════════════════════╗")
        print (e+"║"+y+" dengan adanya alat ini ente bisa tau  "+e+"  ║")
        print (e+"║ "+y+"hari apa ente di lahirkan, ente hanya   "+e+"║")
        print (e+"║ "+y+"tinggal menuliskan tahun bulan dan     "+e+" ║")
        print (e+"║ "+y+"tanggal lahir ente                      "+e+"║")
        print (e+"╚═════════════════════════════════════════╝")
        print ()
        while True:
            tahun = int (inp ("masukan tahun"))
            if len (str (tahun)) != 4:
                print ("masukan yang benar cuk")
                print ("contoh : 2019 ")
                sleep (2)

                continue
            else:
                while True:
                    bulan = int (inp ("masukan bulan"))
                    if bulan not in [f for f in range(1,13)]:
                        print ("masukan bulan yg benar")
                        print("contoh : 6")
                        sleep (2)
                        continue
                    else:
                        while True:
                            tanggal = int (inp ("masukan tanggal"))
                            if tanggal not in [f for f in range (1,32)]:
                                print ("jangan ngaur lah cuk")
                                sleep (2)
                                continue
                            else:
                                tanggal = str (tanggal)
                                break
                        break
                break
        
        aa = calendar.month (tahun,bulan).rstrip ("\n").split ("\n")
        system ("clear")
        print (e+"""
# ########################
#--------"""+e+"""-"""+c+""" ✬ '✧ `✬"""+e+"""------- """+e+"""#
#---"""+e+"""------"""+c+""" ♜=♜=♜"""+e+"""---------"""+e+"""-#
#---"""+e+"""----"""+c+""" {_♥_✿_♥_}"""+e+"""------"""+e+"""--#
#---"""+e+"""---"""+c+"""✩ `✫{=✰=✰==}"""+e+"""✫----"""+e+"""--#
#---"""+e+"""-"""+c+"""♖.{♖___♖_♖___♖}.♖"""+e+"""---"""+e+""" #
#---"""+c+"""-"""+c+"""{===============}"""+e+"""---"""+e+"""-#
#---"""+c+"""{✿_❤_❀_♥_✿_♥_❀_❤_✿}"""+e+"""--"""+e+"""-#
#-- """+c+"""{=================}"""+e+"""--"""+e+"""-#
#---"""+c+"""{_✿_❤_❀_♥_✿_♥_❀_❤_✿_}"""+e+"""-"""+e+"""#
###########################""")


        print (e+"╔═══════════════════════╗")
        for ii in aa:
            print (e+"║ "+i+ii+" "*(21-len (ii))+e+" ║")
        print ("╠═══════════════════════╣")
        tim = (int(tahun),int (bulan),int (tanggal),0,0,0,0,0,0)
        wis = ctime (mktime (tim))
        if wis.startswith ("Mon"):
            hari = "Senin"
        elif wis.startswith ("Tue"):
            hari = "Selasa"
        elif wis.startswith ("Wed"):
            hari = "Rabu"
        elif wis.startswith ("Thu"):
            hari = "Kamis"
        elif wis.startswith("Fri"):
            hari = "Jumat"
        elif wis.startswith ("Sat"):
            hari = "Sabtu"
        elif wis.startswith ("Sun"):
            hari = "Minggu"
        else:
            hari = "Hari"
        print (e+"║"+c+"lu lahir di hari "+g+hari+" "*(6-len (hari))+e+"║")
        print (e+"╚═══════════════════════╝")
        print (wis)
        print ()
        body (li=["home","ulang","exit","contact"])
        print ()
        while True:
            pil = str (inp ("masukan pilihan")).lower ()
            if pil == "h":
                home ()
                exit ()
            elif pil == "u":
                calender ()
                exit ()
            elif pil == "e":
                exit ("thanks")
            elif pil == "c":
                hubungi()
            else:
                print ("masukan yang ada bang")
                sleep (2)
                continue
        


if hashlib.sha1 (executable.encode ()).hexdigest () != "c12fa1b987048613e57eb095f8516bb60cb3e907":exit ("file ini hanya bisa di buka ditermux\nsilahkan download termux digoogle dan cobalah buka")
def body (*arg,li=[]):
        global e,r,g,b,y,i,c,w,nama,umur,sekolah
        print (e+"▥▥▥▥▥▥▥▥▥▥▥▥▥▥▥▥▥▥▥▥▥▥▥▥▥▥▥▥▥▥▥▥▥▥\x1b[0m")
        nil = 0
        awal = 0
        for ing in arg:
            nil += 1
            if nil > 9:
                awal += 1
                nil = 0
            print (e+"#\x1b[0m "+b+"{"+c+str (awal)+str (nil)+b+"} "+g+ing)   
            
        if len(li) > 0:
            print ()
            for ing in li:
                print (e+"# "+r+"{"+y+ing [0]+r+"}"+c+ing)

def home ():
        from zlib import decompress
        from os import system
        system ("clear")
        global e,r,g,b,y,i,c,w,nama,umur,sekolah
        exec (decompress (b'x\x9c\x85\x92M\n\xc20\x10\x85\xf7\x9e\xe21\x9b(1\xcd\x01\xbc\xca\xc0\xd0\x82\xa0P\x9b\x12\xdc\x88\xf1\xee\xa6M\xa5\x1a\x13}\xbb\xc9|\xf3\xe6\x87\x8c\xfe<\\\xb1\xf5D\xfa\xa6\t%\t@\xbb\xcdX\x04-x\x81\x8c\x8aA\x06v\x0b(v.\n\x00\xa7W\xa3\x94\x89\xbe\xc9\xcaN\xc8W\xa1\xc8dyGX\x07\xe1"\x98\xc6\xf8\x14\xff\x03I{ML\xae\x01\x82K\xd9\x07p:\xf6\xbd\x8b\xb9\xa1\xbd\xb4\x9a\x8a\x06!ot\xa8-\x9dI\xed\xeb \xcbzl\xa9\xce\x9el\x94\x99an\xac\xfd\tN\xbbFVD\xa1z\xb6\x17\xf7\xae*\xb8\x18\xd5\xc1\xd8k\xfe\x06\xb9"\xf8\x04*b{\xe4'))
        exec (decompress (b'x\x9c+(\xca\xcc+Q\xd0H\xd6VR&\x01(ir\x15 4*(i\xa7k+\xe5%\xe6&*\x00\x81\x15\x90[\xa9\r\xe2i+)(ii\x18\x1b\xea\xe6\xa4\xe6)h\x80D45\xb5A\x1a\xb0i/\xcd--Bh\x07\xf1\xe0\xda\x15\xc0\xfaABx\xf4\x17\xa7f\xe7\xe7$f@\xf5Cy\xa8.\x80\nb5\x84,\xcfkr\x01\x00S>H\xc2'))
        body("cek hari lahir lu","game hangman","chatting sederhana","putar musik di memori ["+r+"terdapat kesalahan"+g+"]","ecrypt python 3.8","hashkiller",r+"warning!!","zigzag","update",li=["contact me","exit"])
        print ()
        try:
            pil = inp ("masukan pilihan").lower ()
        except Exception:
            from os import system 
            system ("xdg-open https://wa.me/+6282188663881?text=halo%20admin%20ganteng")
            exit ()
        if pil == "01" or pil == "1":
            calender ()
            exit ()
        elif pil == "02" or pil == "2":
            hangman ()
            exit ()
        elif pil == "03" or pil == "3":
            chat ()
            exit ()
        elif pil == "04" or pil == "4":
            music ()
            exit ()
        elif pil == "05" or pil == "5":
            exit (enci())
        elif pil == "06" or pil == "6":
            exit (hashkiller ())
        elif pil == "07" or pil == "7":
            exit (awas ())
        elif pil == "08" or pil == "8":
            exit (zigzag ())
        elif pil == "09" or pil == "9":
            exit (update ())
        elif pil == "e" or pil == "E":
            exit ()
        elif pil == "c":
            hubungi ()
            exit ()
        else:
            print ("masukan yg ada bang")
            sleep (2)
            home ()

home ()
