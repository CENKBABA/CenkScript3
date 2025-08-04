import sys
from cenksp3 import kod_optimize,kod_oku

# print(sys.argv)
dosya=open(sys.argv[1],"r")

kod=""


satır=dosya.readline()
while len(satır)>0:
	kod+=satır
	satır=dosya.readline()
	
kod=kod_optimize(kod)

kod_oku(kod)