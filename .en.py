from sys import argv
from os import system
import bz2
import base64 as a
import lzma
import zlib
pesan = open (argv [2],"r").read ()
if argv [1] == "b16":
    gg = "import base64"
    hh = "base64.b16decode("
    cc = "))"
    hasil = a.b16encode (pesan.encode ())
elif argv [1] == "b32":
    gg = "import base64"
    hh = "base64.b32decode("
    cc = "))"
    hasil = a.b32encode (pesan.encode ())
elif argv [1] == "b64":
    gg = "import base64"
    hh = "base64.b64decode("
    cc = "))"
    hasil = a.b64encode (pesan.encode ())
elif argv [1] == "b85":
    gg = "import base64"
    hh = "base64.b85decode("
    cc = "))"
    hasil = a.b85encode (pesan.encode ())
elif argv [1] == "a85":
    gg = "import base64"
    hh = "base64.a85decode("
    cc = "))"
    hasil = a.a85encode (pesan.encode ())
elif argv [1] == "z2":
    gg = "import bz2"
    hh = "bz2.decompress ("
    cc = "))"
    hasil = bz2.compress (pesan.encode())
elif argv [1] == "zlib":
    gg = "import zlib"
    hh = "zlib.decompress ("
    cc = "))"
    hasil = zlib.compress (pesan.encode ())
elif argv [1] == "lzma":
    gg = "import lzma"
    hh = "lzma.decompress ("
    cc = "))"
    hasil = lzma.compress (pesan.encode ())
elif argv [1] == "lzma1":
    gg = "import lzma"
    hh = "lzma.decompress ("
    cc = "))"
    hasil = lzma.compress (pesan.encode (),format=2)
elif argv [1] == "allb":
    gg = "import base64 as a"
    hh = "a.a85decode (a.b64decode(a.b32decode (a.b16decode (a.a85decode ("
    hasil = a.a85encode (a.b16encode (a.b32encode  (a.b64encode (a.a85encode(pesan.encode ())))))
    cc = "))))))"
elif argv[1] == "allc":
    gg = "import zlib,bz2,lzma"
    hh = "lzma.decompress (zlib.decompress (bz2.decompress("
    hasil = bz2.compress (zlib.compress (lzma.compress (pesan.encode ())))
    cc = "))))"

print ("# compile by gumball watterson\n\n# jangan lupa kasih bintang github gw\n\n# https://github.com/gumball1w/myproject")
print (gg)
print ("exec ("+hh,end="")
print (hasil,end="")
print (cc)


