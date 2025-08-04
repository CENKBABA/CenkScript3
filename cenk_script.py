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
		syctt+=int(a[tt[i][0]+1:tt[i+1][0]])*(-int(tt[i][1]=="-")+int(tt[i][1]=="+"))
	syctt+=int(a[tt[-1][0]+1:])*(-int(tt[-1][1]=="-")+int(tt[-1][1]=="+"))
	return syctt
	

def çarp_böl(a):
	tt=sorted(bulucu(a,"*")+bulucu(a,"/"))
	n=1
	syctt=int(a[0:tt[0][0]])
	for i in range(len(tt)-1):
		if tt[i][1]=="*":
			syctt*=int(a[tt[i][0]+1:tt[i+1][0]])
		elif tt[i][1]=="/":
			syctt/=int(a[tt[i][0]+1:tt[i+1][0]])
	if tt[-1][1]=="*":
		syctt*=int(a[tt[-1][0]+1:])
	elif tt[-1][1]=="/":
		syctt/=int(a[tt[-1][0]+1:])
	
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
			syc+=int(tt2[0])
	for i in range(1,len(tt2)):
		if "*" in tt2[i] or "/" in tt2[i]:
			syc+=çarp_böl(tt2[i])*(1-2*int(tt3[i-1][1]=="-"))
		else:
			syc+=int(tt2[i])*(1-2*int(tt3[i-1][1]=="-"))
	return syc

def _4işlem_v2(a):
	pass
def değerler_f(a,b):
	tt=a
	
	for e in sorted(b,key=len)[::-1]:
		tt=tt.replace(e,str(b[e]))
	return tt
	
kod="""
a=100

eğer(a>10){
tekrarla(a/25){
yazdır 31*31
}
}
eğer(a<10){
tekrarla(3){
yazdır 69
}
}
"""



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


kod2="""
a=100

tekrarla(a-99){
eğer(a-99==1){
yazdır 31
}
eğer(a-99==2){
yazdır 69
}
}
"""
kod3="""
a=-1-1+40
yazdır a+100
a=a+10
sürece(a>10){
eğer(a==31){
	yazdır 69
}
yazdır a
a=a-1
}
"""
#kod_oku(kod3)
