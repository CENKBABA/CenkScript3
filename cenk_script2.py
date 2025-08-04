import re,time


def çoklu_bölücü(st,lst):
	dnd=st.split(lst[0])
	for e in range(1,len(lst)):
		tt=[]
		for i in dnd:
			tt+=i.split(lst[e])
		dnd=tt
	return dnd
def bulucu(st,a):
	tt=[]
	syc=0
	for i in st:
		if i==a:
			tt.append((syc,a))
		syc+=1
	return tt

def bulucu_v2(st,ara):
	kaç_kere=st.count(ara)
	if kaç_kere==0:
		return []
	tt=st.find(ara)
	lst=[tt]
	for i in range(kaç_kere-1):
		tt=st.find(ara,tt+1)
		lst.append(tt)
	return lst
	
#def bulucu_v2(st,a):
#	tt=[]
#	syc=0
#	for i in range(len(st)-len(a),len(a)):
#		print(st)
#		syc+=1
#	return tt
a="12+3-12+1000"

def topla_çıkar(a):
	tt=sorted(bulucu(a,"+")+bulucu(a,"-"))
	
	n=1
	syctt=int(a[0:tt[0][0]])
	for i in range(len(tt)-1):
		syctt+=float(a[tt[i][0]+1:tt[i+1][0]])*(-int(tt[i][1]=="-")+int(tt[i][1]=="+"))
	syctt+=float(a[tt[-1][0]+1:])*(-int(tt[-1][1]=="-")+int(tt[-1][1]=="+"))
	return syctt
	

def çarp_böl(a):
	tt=sorted(bulucu(a,"*")+bulucu(a,"/"))
	n=1
	syctt=float(a[0:tt[0][0]])
	for i in range(len(tt)-1):
		if tt[i][1]=="*":
			syctt*=float(a[tt[i][0]+1:tt[i+1][0]])
		elif tt[i][1]=="/":
			syctt/=float(a[tt[i][0]+1:tt[i+1][0]])
	if tt[-1][1]=="*":
		syctt*=float(a[tt[-1][0]+1:])
	elif tt[-1][1]=="/":
		syctt/=float(a[tt[-1][0]+1:])
	
	return syctt


def _4işlem(a):
	tt=a.split("+")
	tt2=[]
	tt3=sorted(bulucu(a,"+")+bulucu(a,"-"))
	for i in tt:
		tt2+=i.split("-")
	
	syc=0
	if "*" in tt2[0] or "/" in tt2[0]:
		syc+=çarp_böl(tt2[0])
	else:
		if tt2[0]=="":
			pass
		else:
			syc+=float(tt2[0])
	for i in range(1,len(tt2)):
		if "*" in tt2[i] or "/" in tt2[i]:
			syc+=çarp_böl(tt2[i])*(1-2*int(tt3[i-1][1]=="-"))
		else:
			syc+=float(tt2[i])*(1-2*int(tt3[i-1][1]=="-"))
	return syc

def _4işlem_v2(a):
	pass
def değerler_f(a,b):
	ttt=[" ","+","-","*","/"]
	tt=a
	for e in sorted(b,key=len)[::-1]:
		kn=a.find(e)
		tt=tt.replace(e,str(b[e]))
	return tt


def tek_sorgu_çözücü(st):
	dztt=st
	krs=[]
	isaret=""
		
	if "<" in dztt:
		krs=dztt.split("<")
		return _4işlem(krs[0])<_4işlem(krs[1])
	elif ">" in dztt:
		krs=dztt.split(">")
		return _4işlem(krs[0])>_4işlem(krs[1])
	elif "==" in dztt:
		krs=dztt.split("==")
		return _4işlem(krs[0])==_4işlem(krs[1])
	elif "!=" in dztt:
		krs=dztt.split("!=")
		return _4işlem(krs[0])!=_4işlem(krs[1])
	else:
		return _4işlem(dztt)
def lojik_çözücü(st):
	tt=st.split(" ")
	for i in range(tt.count("")):
		tt.remove("")
	döndür=tek_sorgu_çözücü(tt[0])
	if len(tt)>1:
		for i in range(1,len(tt)-1,2):
			if tt[i]=="ve":
				döndür=döndür and tek_sorgu_çözücü(tt[i+1])
			elif tt[i]=="veya":
				döndür=döndür or tek_sorgu_çözücü(tt[i+1])
	return döndür
	
def kod_oku(kod):
	satırlar=kod.split("\n")
	değerler={"__ALLAH":1}
	satır=0
	döngüye_dön={}
	döngü_sonu={}
	döngü_sonu_ters={}
	eğerler=[]
	süreceler=[]
	
	syc=0
	tta=[]
	
	for i in satırlar:
		if "{" in i:
			if "eğer" in i:
				eğerler.append(syc)
			if "sürece" in i:
				süreceler.append(syc)
			tta.append(syc)
		if "}" in i:
			döngü_sonu.update({syc:tta[-1]})
			döngü_sonu_ters.update({tta[-1]:syc})
			tta.remove(tta[-1])
		syc+=1
	
	içiçe=1
	while satır<len(satırlar):
		i=satırlar[satır]
		ti=i.split("\n")
		for i in range(ti.count("\n")):
			ti.remove("\n")
		i="".join(ti)
		for i in range(ti.count(" ")):
			ti.remove(" ")
		
		if "==" not in i and "!=" not in i and "=" in i:
			tt=i.split("=")
			değerler.update({tt[0]:_4işlem(değerler_f(tt[1],değerler))})
		elif "yazdır" in i:
			print(_4işlem(değerler_f(i.split(" ")[1],değerler)))
		elif "tekrarla" in i:
			dtt=_4işlem(değerler_f(i.split("(")[-1][:-2],değerler))
			döngüye_dön.update({satır:dtt})
		elif "eğer" in i:
			koşul=lojik_çözücü(değerler_f(i.split("(")[-1][:-2],değerler))
			if(not koşul):
				satır=döngü_sonu_ters[satır]
		elif "sürece" in i:
			koşul=lojik_çözücü(değerler_f(i.split("(")[-1][:-2],değerler))
			if(not koşul):
				satır=döngü_sonu_ters[satır]
		elif "}" in i:
			if döngü_sonu[satır] not in eğerler:
				tetikleme=True
				if döngü_sonu[satır] in süreceler:
					satır=döngü_sonu[satır]
					satır-=1
					tetikleme=False
				if döngüye_dön!={} and tetikleme:
					if döngüye_dön[döngü_sonu[satır]]>1:
						döngüye_dön[döngü_sonu[satır]]-=1
						satır=döngü_sonu[satır]
			else:
				pass
				#print("geçti",satır)
			#print("asd",satır,döngü_sonu,döngüye_dön)
		satır+=1
	
def fonksiyonla(dt,fnkler,değerler):
	tekrar_drm=True
	silinecek=[]
	while tekrar_drm:
		degistir=[]
		for hng in fnkler:
			lstt=bulucu_v2(dt,hng)
			for i in lstt:
				stt=""
				dvm=False
				for e in dt[i+len(hng)+1:]:
					if e==")":
						break
					elif e=="(":
						dvm=True
						tekrarlanacak=True
						break
					else:
						stt+=e
				if not dvm:
					parametreler=stt.split(",")
					parametre_ls=[]
					for i in parametreler:
						gcctt=_4işlem(değerler_f(i,değerler))
						parametre_ls.append(gcctt)
					degistir.append([hng+"("+stt+")",str(fnkler[hng](parametre_ls))])
		for i,j in degistir:
			dt=dt.replace(i,j)
		tekrar_drm=False
		for i in fnkler:
			gctt=bulucu_v2(dt,i)
			ek_kontrol=bool(gctt!=[])
			if gctt!=[]:
				for e in gctt:
					for j in dt[e+len(i)+1:]:
						if j==")":
							break
						if j=="(":
							#print("eben")
							ek_kontrol=False
							break
			tekrar_drm=tekrar_drm or ek_kontrol
			
		#print(dt,tekrar_drm)
	return dt
	
def parantez_çözücü(dt1,dgler):
	stt=""
	drm=True
	degistir=[]
	tt=[0]
	while tt!=[]:
		tt=bulucu_v2(dt1,"(")
	
		ttfnk=[]
		for i in fnkler:
			ttfnk+=list(e+len(i) for e in bulucu_v2(dt1,i))
		
		for i in ttfnk:
			tt.remove(i)
		tekrar_drm=False
		silinecek=[]
		for i in tt:
			for e in dt1[i+1:]:
				if e=="(":
					drm=False
					break
				elif e==")":
					break
				else:
					stt+=e
			if drm:
				kntrol=False
				for i in fnkler:
					tekrar_drm=tekrar_drm or i in dt
				degistir.append(("("+stt+")",_4işlem(değerler_f(stt,dgler))))
			else:
				silinecek.append(i)
			drm=True
			stt=""
		for j,i in degistir:
			dt1=dt1.replace(j,str(i))
		for i in silinecek:
			tt.remove(i)
	return dt1
	
def lojik_ama_değerli(st,a):
	print(a)

fnkler={"mod":lambda i:i[0]%i[1],"topla":lambda i:i[0]+i[1]}
değerler={"a":11}
dt="a+mod(topla(13,mod(5,3)),2)+mod(mod(11,3),2)+topla(10,5)"
	

dt1="(10+mod((30/10),2)+31)*(10-8/(20-(9*2)+2))"

def mutlak_basitleyici(st,fnkler,dgler):
	while "(" in st or ")" in st:
		st=parantez_çözücü(st,dgler)
		st=fonksiyonla(st,fnkler,dgler)
	print(st)
	print(_4işlem(st))
	
#mutlak_basitleyici("mod((topla(20,20)/2-15)*(4-(mod(3,2))*2),20)+mod(13,10)",fnkler,değerler)

mod_alma="""
a=41
b=6
sürece(a>b){
a=a-b
}
yazdır a

"""
tek_mi_çift_mi="""
girdi=16
sayac=0
sürece(girdi>2 veya girdi==2){
girdi=girdi-2
sayac=sayac+1
}
eğer(girdi==0){
yazdır 31
}
eğer(girdi==1){
yazdır 69
}
yazdır sayac
"""

kod2="""

s=0

sürece(s<5 veya s==5){
yazdır s
s=s+1
}
a=12
aba=31
ab=a+aba
yazdır ab
eğer(ab!=43){
yazdır 103
}
"""

int_dönüştürücü="""
a=3.5
tt=0
art=0.5
sürece(a>art veya a==art){
a=a-art
tt=tt+art
}
yazdır tt

"""
#print("----")
#kod_oku(tek_mi_çift_mi)
#print("---")
#kod_oku(mod_alma)
#print("---")
#kod_oku(kod2)


print("---")
kod_oku(int_dönüştürücü)



print("____")
mutlak_basitleyici("(12+(30-9*3))*(4-2)",fnkler,değerler)