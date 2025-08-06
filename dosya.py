import sys
from cenksp3 import kod_optimize,kod_oku

# print(sys.argv)

kodlama=""
if len(sys.argv)>=3 and sys.argv[2].lower()=="türkçe":
	kodlama="utf-8"
else:
	kodlama="ansi"
dosya=open(sys.argv[1],"r",encoding=kodlama)

kod=""


satır=dosya.readline()
while len(satır)>0:
	kod+=satır
	satır=dosya.readline()
	
kod=kod_optimize(kod)

# print("anan",kod)

kod_oku(kod)