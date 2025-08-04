import re,time
from listeler import listeli_ifade_çözücü,ls_basitle
from listeler import ls_eleman_degistir,ls_eleman_elde
from listeler import ls_eleman_uzunluk

def değer_parametre(dgl,prmt):
	dnd=dict(dgl)
	for i in prmt:
		dnd|=i
	return dnd
def gerekli_float(sy):
	if sy%1==0:
		return int(sy)
	return sy
def işleyici(a):
	tt=1
	syc=0
	for i in a:
		if i.isnumeric():
			break
		elif i=="-":
			tt*=-1
		syc+=1
	return float(a[syc:])*tt
def çarpböl(a):
	st=""
	syc=0
	sy=0
	işrt=""
	for i in a:
		if i.isnumeric() or i=="+" or i=="-" or i==".":
			st+=i
		elif i=="*" or i=="/":
			işrt=i
			syc+=1
			break
		syc+=1
	sy=işleyici(st)
	
	
	a=a[syc:]
	st=""
	sc=0
	for i in a:
		if i=="*" or i=="/":
			if işrt=="*":
				sy*=işleyici(st)
			elif işrt=="/":
				sy/=işleyici(st)
			işrt=i
			st=""
		if sc==len(a)-1:
			st+=i
			if işrt=="*":
				sy*=işleyici(st)
			elif işrt=="/":
				sy/=işleyici(st)
		if i.isnumeric() or i=="+" or i=="-" or i==".":
			st+=i
		sc+=1
	return sy
def _4işlem(a):
	st=""
	syd=a[0].isnumeric()
	çbd=False
	sy=0
	for i in range(len(a)):
		if a[i] in "*/":
			st+=a[i]
			çbd=True
		if i==len(a)-1:
			st+=a[i]
			sy+=çarpböl(st)
		if a[i].isnumeric() or a[i]==".":
			st+=a[i]
			syd=True
			if çbd:
				çbd=False
		if a[i] in "+-":
			if syd:
				if not çbd:
					sy+=çarpböl(st)
					st=a[i]
				else:
					st+=a[i]
					çbd=False
				syd=False
			else:
				st+=a[i]
	return gerekli_float(sy)
	

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
	
	return gerekli_float(syctt)


def _4işlem_v1(a):
	while "--" in a or "++" in a or "+-" in a or "-+" in a:
		a=a.replace("--","+")
		a=a.replace("++","+")
		a=a.replace("-+","-")
		a=a.replace("+-","-")
		
	if a[0]=="+":
		a=a[1:]
	tt=a.split("+")
	tt2=[]
	tt3=sorted(bulucu(a,"+")+bulucu(a,"-"))
	if a[0]=="-":
		tt3.remove(tt3[0])
	for i in tt:
		if "*-" not in i and i[0]!="-":
			tt2+=i.split("-")
		elif i[0]=="-" and "*-" not in i:
			gg=i[1:].split("-")
			gg[0]="-"+gg[0]
			tt2+=gg
		else:
			tt2.append(i)
	syc=0
	if "*" in tt2[0] or "/" in tt2[0]:
		syc+=çarp_böl(tt2[0])
	else:
		syc+=float(tt2[0])
	for i in range(1,len(tt2)):
		if "*" in tt2[i] or "/" in tt2[i]:
			if tt3[i-1][1]=="-":
				syc-=çarp_böl(tt2[i])
			else:
				syc+=çarp_böl(tt2[i])
		else:
			if tt3[i-1][1]=="-":
				syc-=float(tt2[i])
			else:
				syc+=float(tt2[i])
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
	
def değerle2(a,b):
	kt=" +-*/()"
	for e in b:
		artt=0
		tt=bulucu_v2(a,e)
		sil=[]
		for i in tt:
			if i>0 and i+len(e)<len(a):
				if a[i+len(e)] not in kt or a[i-1] not in kt:
					sil.append(i)
			elif i==0:
				if a[i+len(e)] not in kt:
					sil.append(i)
			elif  i+len(e)==len(a):
				if a[i-1] not in kt:
					sil.append(i)
		for i in sil:
			tt.remove(i)
		for i in tt:
			i=i+artt
			dgst=str(b[e])
			a=a[0:i]+dgst+a[i+len(e):]
			artt+=len(dgst)-len(e)
			
	return a

def değerle3_beta(a,b):
	kt=" +-*/()><!=,[]:"
	for e in b:
		artt=0
		tt=bulucu_v2(a,e)
		sil=[]
		for i in tt:
			drm=True
			if i+artt>0 and i+artt+len(e)<len(a):
				if a[i+artt+len(e)] not in kt or a[i+artt-1] not in kt:
					drm=False
			elif i+artt==0 and i+artt+len(e)!=len(a):
				if a[i+artt+len(e)] not in kt:
					drm=False
			elif  i+artt+len(e)==len(a) and i+artt!=0:
				if a[i+artt-1] not in kt:
					drm=False
			elif i+artt==0 and i+artt+len(e)==len(a):
				pass
			if drm:
				i=i+artt
				if b[e].isnumeric():
					dgst=str(gerekli_float(float(b[e])))
				else:
					dgst=b[e]
				print("hasssssss31",dgst,a,e)
				a=a[0:i]+dgst+a[i+len(e):]
				print("hasssssss69",dgst,a,e)
				artt+=len(dgst)-len(e)
	return a

def değerle3_2(a,b):
	kt=" +-*/()><!=,[]:"
	dnd=""
	değişecek=""
	sayıda=False
	değerde=False
	for i in a:
		if i in kt:
			if değerde:
				#print(değişecek)
				#print("eklenecek",dnd)
				dnd+=str(b[değişecek])
				değişecek=""
			sayıda=False
			değerde=False
			dnd+=i
		elif i.isnumeric():
			if not sayıda and not değerde:
				sayıda=True
			elif değerde:
				değişecek+=i
				sayıda=False
			if sayıda:
				dnd+=i
		else:
			if not değerde:
				değerde=True
			if değerde:
				değişecek+=i
	if değerde:
		dnd+=str(b[değişecek])
	#print("son hali",dnd)
	return dnd
	
def değerle3(a,b):
	kt=" +-*/()><!=,[]:"
	dnd=""
	değişecek=""
	sayıda=False
	değerde=False
	for i in a:
		if i in kt:
			if değerde and i=="(":
				değerde=False
				dnd+=değişecek
				değişecek=""
				pass
			elif değerde:
				#print(değişecek)
				#print("değişti",değişecek,dnd)
				dnd+=str(b[değişecek])
				değişecek=""
			sayıda=False
			değerde=False
			dnd+=i
		elif i.isnumeric():
			if not sayıda and not değerde:
				sayıda=True
			elif değerde:
				değişecek+=i
				sayıda=False
			if sayıda:
				dnd+=i
		else:
			if not değerde:
				değerde=True
			if sayıda:
				#print(dnd,"ve",değişecek)
				dnd+="*"
			if değerde:
				değişecek+=i
	if değerde:
		dnd+=str(b[değişecek])
	#print("son hali",dnd)
	return dnd

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
						gcctt=_4işlem(değerle3(i,değerler))
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
	fnkler={"mod":lambda i:i[0]%i[1],"topla":lambda i:i[0]+i[1]}
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
					tekrar_drm=tekrar_drm or i in dt1
				degistir.append(("("+stt+")",_4işlem(değerle3(stt,dgler))))
			else:
				silinecek.append(i)
			drm=True
			stt=""
		for j,i in degistir:
			dt1=dt1.replace(j,str(i))
		for i in silinecek:
			tt.remove(i)
	return dt1
	
	

	
def fnk_ayıkla_beta2(a):
	dndls=[]
	fn=""
	dr=False
	fidr=False
	prsy=0
	st_dv=False
	for i in a:
		if i.isnumeric() or i in "().,+-*/<>= ":
			if i in "().,+-*/<>= ":
				st_dv=False
			if i=="(":
				prsy+=1
			if i==")":
				prsy-=1
			if fidr:
				if not st_dv:
					fidr=False
		else:
			st_dv=True
			if not dr:
				fidr=True
				dr=True
				prsy=0
			if not fidr and dr:
				fidr=True
				prsy=0
				fn=""
		#print(i,prsy,fidr)
		if dr:
			fn+=i
			if i==")" and prsy==0:
				dr=False
				dndls.append(fn)
				fn=""
	return dndls
def fnk_ayıkla_beta(a):
	dndls=[]
	fn=""
	dr=False
	fidr=False
	prsy=0
	for i in a:
		if i.isnumeric() or i in "().,+-*/!=<>":
			if i=="(":
				prsy+=1
			if i==")":
				prsy-=1
			if fidr:
				fidr=False
		else:
			if not dr:
				fidr=True
				dr=True
				prsy=0
			if not fidr and dr:
				fidr=True
				prsy=0
				fn=""
		#print(i,prsy,fidr)
		if dr:
			fn+=i
			if i==")" and prsy==0:
				dr=False
				dndls.append(fn)
				fn=""
	return dndls
	
def parantez_çözücü2_hızlı(st):
	stack = []
	for i, c in enumerate(st):
		if c == '(':
			stack.append(i)
		elif c == ')':
			start = stack.pop()
			iç = st[start+1:i]
			sonuç = str(gerekli_float(_4işlem(iç)))
			st = st[:start] + sonuç + st[i+1:]
			return parantez_çözücü2_hızlı(st)
	return st

def parantez_çözücü2(st):
	knm=[]
	drm=True
	ifd=""
	bsl=False
	degis=""
	while drm:
		syc=0
		for i in st:
			if i=='(':
				ifd=""
				bsl=True
			if i==')':
				if bsl:
					ifd+=")"
					knm.append([ifd,syc-len(ifd)+1])
					ifd=""
				bsl=False
			if bsl:
				ifd+=i
			syc+=1
		fark=0
		for i in knm:
			ifade=i[0][1:-1]
			degis=str(listeli_ifade_çözücü(ifade))
			st=st[0:i[1]+fark]+degis+st[i[1]+len(i[0])+fark:]
			fark=fark-len(i[0])+len(degis)
		#print("son hali ->",st)
		knm=[]
		drm="(" in st
	return st

def parantez_çözücü22(dt1,dgler):
	stt=""
	drm=True
	degistir=[]
	tt=[0]
	fnkler={"mod":lambda i:i[0]%i[1],"topla":lambda i:i[0]+i[1]}
	ljk_elemanlar=["<",">","==","=!","ve","veya"]
	while tt!=[]:
		tt=bulucu_v2(dt1,"(")
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
					tekrar_drm=tekrar_drm or i in dt1
				
				if lojik_mi(stt):
					degistir.append(("("+stt+")",int(lojik_çözücü(değerle3(stt,dgler)))))
				else:
					degistir.append(("("+stt+")",_4işlem(değerle3(stt,dgler))))
					
			else:
				silinecek.append(i)
			drm=True
			stt=""
		for j,i in degistir:
			dt1=dt1.replace(j,str(i))
		for i in silinecek:
			tt.remove(i)
	return dt1
	
def eşittir_bulucu(a):
	dd=0
	est=False
	ard=False
	eksl=-1
	syc=0
	for i in a:
		if ard and i!="=":
			ard=False
		if (i=="=" or i=="<" or i==">") and not ard and not est:
			dd=syc
			est=True
		if syc-dd==1 and est and not ard:
			if i!="=":
				eksl=1
				break
			else:
				#print("loo")
				ard=True
				est=False
		syc+=1
	return dd*eksl
	

def lojik_mi(stt):
	return "<" in stt or ">" in stt or "==" in stt or "!=" in stt or " ve " in stt or " veya " in stt

def fnk_ayıkla_beta3(a):
	dndls=[]
	fn=""
	fnb=False
	fbt=False
	prsy=0
	dısy=0
	ici=False
	for i in a:
		if i.isnumeric() or i in "().,+-*/<>!= ":
			if i=="(":
				prsy+=1
			if i==")":
				prsy-=1
			if not fnb:
				dısy=prsy
			if fnb and prsy==dısy and i in ".,+-*/<>!= ":
				fnb=False
				fbt=True
				fn=""
		else:
			if not fnb:
				fnb=True
			if fnb and prsy>dısy:
				fn=""
				dısy=prsy
		if fnb:
			fn+=i
			if i==")" and prsy==dısy:
				dndls.append(fn)
				fn=""
				fnb=False
	return dndls
	
def fnk_ayıkla(a):
	dndls=[]
	fn=""
	fnb=False
	fbt=False
	prsy=0
	dısy=0
	ici=False
	icf=False
	icfn=""
	for i in a:
		if i.isnumeric() or i in "().,+-*/<>!=[]: ":
			if i=="(":
				if icf:
					fn=icfn
					icf=False
					dısy=prsy
					icfn=""
				prsy+=1
			if i==")":
				prsy-=1
			if not fnb:
				dısy=prsy
			if fnb and prsy==dısy and i in ".,+-*/<>!=[]: ":
				fnb=False
				fbt=True
				fn=""
			if icf and  i in ".,+-*/<>!=[]: ":
				icf=False
				icfn=""
		else:
			if not fnb:
				fnb=True
			if fnb and prsy>dısy:
				#print(i,"asas")
				#fn=""
#				dısy=prsy
				icf=True
				
		if fnb:
			fn+=i
			if icf:
				icfn+=i
			if i==")" and prsy==dısy:
				dndls.append(fn)
				fn=""
				fnb=False
	return dndls
def fnk_ayıkla2(st):
	dnd=""
	gcc=""
	fnk_başladı=False
	prmt_başladı=False
	içte_var=False
	ilk_içte_var=False
	psy=0
	disy=0
	for i in st:
		if i.isdigit() or i in "().,+-*/<>!=[] ":
			if i=="(":
				if not prmt_başladı and fnk_başladı:
					prmt_başladı=True
					disy=psy
				if içte_var:
					gcc=""
					prmt_başladı=True
					içte_var=False
					disy=psy
				psy+=1
			elif i==")":
				psy-=1
				if içte_var:
					içte_var=False
					dnd=gcc
					prmt_başladı=True
					fnk_başladı=False
				if prmt_başladı and disy==psy:
					dnd+=i
					break
			elif i.isdigit():
				if not prmt_başladı:
					dnd+=i
			else:
				if içte_var:
					içte_var=False
					dnd=gcc
					prmt_başladı=True
					fnk_başladı=False
				if fnk_başladı:
					fnk_başladı=False
			if prmt_başladı:
					dnd+=i
			if içte_var:
					gcc+=i
		else:
			if not fnk_başladı and not prmt_başladı:
				fnk_başladı=True
				prmt_başladı=False
				dnd=""
				dnd+=i
			else:
				dnd+=i
			if prmt_başladı:
				içte_var=True
				fnk_başladı=True
				prmt_başladı=False
				gcc=dnd
				dnd=""
				dnd+=i
				ilk_içte_var=True
			if içte_var:
				if not ilk_içte_var:
					gcc+=i
				else:
					ilk_içte_var=False
	if prmt_başladı:
		return dnd
	else:
			return ""
			
def tek_sorgu_çözücü(st):
	#print("sorgu ifadesi",st)
	dztt=st
	krs=[]
	isaret=""
	if "<=" in dztt:
		#print("loo1")
		krs=dztt.split("<=")
		return _4işlem(krs[0])<=_4işlem(krs[1])
	elif ">=" in dztt:
		krs=dztt.split(">=")
		print("loo2",krs[0],krs[1])
		return _4işlem(krs[0])>=_4işlem(krs[1])
	elif "<" in dztt:
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
		#print("___",dztt)
		return bool(_4işlem(dztt))
def lojik_çözücü(st):
	tt=st.split(" ")
	for i in range(tt.count("")):
		tt.remove("")
	döndür=tek_sorgu_çözücü(tt[0])
	#print("cccc",tt)
	if len(tt)>1:
		for i in range(1,len(tt),2):
			if tt[i]=="ve":
				#print("hadi aq",tt[i],tt[i+1])
				döndür=döndür and tek_sorgu_çözücü(tt[i+1])
				#print("hadi işte aq",tt[i+1])
			elif tt[i]=="veya":
				döndür=döndür or tek_sorgu_çözücü(tt[i+1])
	return döndür
	
def parametre_kesici(a):
	psy=0
	dnd=[]
	parça=""
	for i in a:
		if i=="[":
			psy+=1
		elif i=="]":
			psy-=1
		if psy==0 and i==",":
			dnd.append(parça)
			parça=""
		else:
			parça+=i
	dnd.append(parça)
	return dnd
	
def değer_index_ayırıcı(st):
	psy=0
	ifade=""
	dnd=[]
	for i in st:
		if i=="[":
			psy+=1
		elif i=="]":
			psy-=1
			if psy==0:
				dnd.append(ifade)
				ifade=""
		if (i=="[" and psy!=1) or (i=="]" and psy!=0) or i not in "[]":
			ifade+=i
	return dnd

def kod_oku(kod):
	satırlar=kod.split("\n")
	değerler_global={"__ALLAH":1}
	değerler={}
	lokal_parametreler=[]
	fnk_gcc_değer={}
	satır=0
	döngüye_dön={}
	döngü_sonu={}
	döngü_sonu_ters={}
	eğerler=[]
	süreceler=[]
	
	
	fonksiyonlar={}
	fnk_parametreler={}
	
	fnk_sıra=[]
	fnk_çözülecek=[]
	fnk_çözüm=[]
	fnk_git=[]
	fnk_ifade=[]
	fnk_ifd=False
	
	
	indexte_fonksiyon=False
	indexte_fonksiyon_bitti=False
	indexte_fonksiyon_çözülmüş=[]
	
	syc=0
	tta=[]
	
	for i in satırlar:
		if "{" in i:
			if "eğer" in i:
				eğerler.append(syc)
			if "sürece" in i:
				süreceler.append(syc)
			if "fonksiyon" in i:
				gccst=(i.split(" ")[1].split("(")[0])
				prmt=i.split(" ")[1].split("(")[1].split(")")[0].split(",")
				fonksiyonlar.update({gccst:syc})
				fnk_parametreler.update({syc:prmt})
				
				
			tta.append(syc)
		if "}" in i:
			döngü_sonu.update({syc:tta[-1]})
			döngü_sonu_ters.update({tta[-1]:syc})
			tta.remove(tta[-1])
		syc+=1
	
	içiçe=1
	döngü_id=[]
	#print(fnk_parametreler,fonksiyonlar,döngü_sonu)
	while satır<len(satırlar):
		değerler=değer_parametre(değerler_global,lokal_parametreler)
		i=satırlar[satır]
		ti=i.split("\n")
		for i in range(ti.count("\n")):
			ti.remove("\n")
		i="".join(ti)
		for i in range(ti.count(" ")):
			ti.remove(" ")
		
		if "döndür" in i:
			asdtt=i[len("döndür")+1:]
			değerlenmiş=değerle3(asdtt,değerler)
			kntls=fnk_ayıkla2(değerlenmiş)
			
			#print("hassss",asdtt)
			
			if kntls=="":
				#değerler.update({tt[0]:_4işlem(değerle3(parantez_çözücü(tt[1],değerler),değerler))})
				satır=fnk_git[-1]-1
				gecici=parantez_çözücü2(değerlenmiş)
				
				fnk_çözüm.append(str(listeli_ifade_çözücü(gecici)))
					#print("ananhass",asdtt,"ve",str(_4işlem(değerle3(parantez_çözücü2(asdtt,değerler),değerler))))
				
				fnk_git.remove(fnk_git[-1])
				lokal_parametreler.pop(-1)
			else:
				if fnk_çözüm!=[]:
					#print("babam",fnk_ifade,fnk_çözüm)
					ifd=fnk_ifade[-1]
					
					ifd=ifd.replace(fnk_çözülecek[-1],fnk_çözüm[-1])
					
					
					fnk_ifade[-1]=ifd
					knt2=fnk_ayıkla2(ifd)
					if knt2=="":
						#print(ifd,",",fnk_çözüm,",","anan")
						#değerler.update({tt[0]:_4işlem(değerle3(parantez_çözücü(ifd,değerler),değerler))})
						fnk_ifade.remove(fnk_ifade[-1])
						fnk_çözülecek.remove(fnk_çözülecek[-1])
						fnk_çözüm.remove(fnk_çözüm[-1])
						
						satır=fnk_git[-1]-1
						#print("loooo",ifd)
						gecici=parantez_çözücü2(ifd)
						
						fnk_çözüm.append(str(listeli_ifade_çözücü(gecici)))
						
						#fnk_çözüm.append(str(_4işlem(değerle3(parantez_çözücü2(ifd,değerler),değerler))))
						fnk_git.remove(fnk_git[-1])
						lokal_parametreler.pop(-1)
						
						#fnk_çözüm=[]
					else:
						#print("deneme tata",knt2)
						#fnk_çözülecek.append(knt2[0])
						fnk_çözülecek[-1]=knt2
						fnk_çözüm.remove(fnk_çözüm[-1])
						fnkad=knt2.split("(")[0]
						fnkpr=parametre_kesici(knt2[len(fnkad)+1:-1])
						sycc=0
						lokal_parametreler.append({})
						for i in fnkpr:
							ttt=fnk_parametreler[fonksiyonlar[fnkad]][sycc]
							#lokal_parametreler[-1].update({ttt:_4işlem(parantez_çözücü2(i,değerler))})
							lokal_parametreler[-1].update({ttt:listeli_ifade_çözücü(parantez_çözücü2(i))})
							
							sycc+=1
						fnk_git.append(satır)
						satır=fonksiyonlar[fnkad]
				else:
					fnk_ifade.append(değerle3(asdtt,değerler))
					fnkad=kntls.split("(")[0]
					fnkpr=parametre_kesici(kntls[len(fnkad)+1:-1])
					#print(fnkad,fnkpr)
					fnk_çözülecek.append(kntls)
					sycc=0
					lokal_parametreler.append({})
					for i in fnkpr:
						ttt=fnk_parametreler[fonksiyonlar[fnkad]][sycc]
						#lokal_parametreler[-1].update({ttt:_4işlem(parantez_çözücü2(i,değerler))})
						lokal_parametreler[-1].update({ttt:listeli_ifade_çözücü(parantez_çözücü2(i))})
						
						sycc+=1
					fnk_git.append(satır)
					satır=fonksiyonlar[fnkad]
			
			
		elif "fonksiyon" in i:
			satır=döngü_sonu_ters[satır]
		elif "yazdır" in i:
			tt=i[len("yazdır")+1:]
			#print("hasss")
			değerlenmiş=değerle3(tt,değerler)
			kntls=fnk_ayıkla2(değerlenmiş)
			
			#print("hasssss",değerlenmiş)
			
			if kntls=="":
				#değerler.update({tt[0]:_4işlem(değerle3(parantez_çözücü(tt[1],değerler),değerler))})
				#print("başı",tt)
				gecici=parantez_çözücü2(değerlenmiş)
				#print("sonu",tt,değerler,değerlenmiş,değerle3(tt,değerler),"hasss")
				print(listeli_ifade_çözücü(gecici))
			else:
				if fnk_çözüm!=[]:
					#print("babam",fnk_ifade,fnk_çözüm)
					ifd=fnk_ifade[-1]
					
					ifd=ifd.replace(fnk_çözülecek[-1],fnk_çözüm[-1])
					
					
					fnk_ifade[-1]=ifd
					knt2=fnk_ayıkla2(ifd)
					if knt2=="":
						#print(ifd,",",fnk_çözüm,",","anan")
						#değerler.update({tt[0]:_4işlem(değerle3(parantez_çözücü(ifd,değerler),değerler))})
						#print("hort",ifd)
						
						gecici=parantez_çözücü2(ifd)
						
						print(listeli_ifade_çözücü(gecici))
						
						#print(_4işlem(değerle3(parantez_çözücü2(ifd,değerler),değerler)))
						
						fnk_ifade.remove(fnk_ifade[-1])
						fnk_çözülecek.remove(fnk_çözülecek[-1])
						fnk_çözüm.remove(fnk_çözüm[-1])
						#fnk_çözüm=[]
					else:
						#print("deneme tata",knt2)
						#fnk_çözülecek.append(knt2[0])
						fnk_çözülecek[-1]=knt2
						fnk_çözüm.remove(fnk_çözüm[-1])
						fnkad=knt2.split("(")[0]
						fnkpr=parametre_kesici(knt2[len(fnkad)+1:-1])
						sycc=0
						lokal_parametreler.append({})
						for i in fnkpr:
							ttt=fnk_parametreler[fonksiyonlar[fnkad]][sycc]
							lokal_parametreler[-1].update({ttt:listeli_ifade_çözücü(parantez_çözücü2(i))})
							sycc+=1
						fnk_git.append(satır)
						satır=fonksiyonlar[fnkad]
				else:
					fnk_ifade.append(değerle3(tt,değerler))
					fnkad=kntls.split("(")[0]
					fnkpr=parametre_kesici(kntls[len(fnkad)+1:-1])
					
					#print("looooo",fnkpr,kntls[len(fnkad)+1:-1])
					#print(fnkad,fnkpr)
					fnk_çözülecek.append(kntls)
					sycc=0
					lokal_parametreler.append({})
					for i in fnkpr:
						ttt=fnk_parametreler[fonksiyonlar[fnkad]][sycc]
						
						
						lokal_parametreler[-1].update({ttt:listeli_ifade_çözücü(parantez_çözücü2(i))})
						sycc+=1
					fnk_git.append(satır)
					satır=fonksiyonlar[fnkad]
			
		elif "tekrarla" in i:
			itt=i[bulucu_v2(i,"(")[0]+1:-2]
			değerlenmiş=değerle3(itt,değerler)
			kntls=fnk_ayıkla2(değerlenmiş)
			
			#print("looo",kntls,itt)
			if kntls=="":
				#değerler.update({tt[0]:_4işlem(değerle3(parantez_çözücü(tt[1],değerler),değerler))})
				#print(_4işlem(değerle3(parantez_çözücü(tt[1],değerler),değerler)))
				dtt=0
				gecici=parantez_çözücü2(değerlenmiş)
				
				dtt=int(listeli_ifade_çözücü(gecici))
				
				
				if(dtt>0):
					döngüye_dön.update({satır:dtt})
					döngü_id.append(satır)
				else:
					#print("omrg",satır,döngü_sonu_ters)
					satır=döngü_sonu_ters[satır]
			else:
				if fnk_çözüm!=[]:
					#print("babam",fnk_ifade,fnk_çözüm)
					ifd=fnk_ifade[-1]
					
					ifd=ifd.replace(fnk_çözülecek[-1],fnk_çözüm[-1])
					
					
					fnk_ifade[-1]=ifd
					knt2=fnk_ayıkla2(ifd)
					if knt2=="":
						#print(ifd,",",fnk_çözüm,",","anan")
						#değerler.update({tt[0]:_4işlem(değerle3(parantez_çözücü(ifd,değerler),değerler))})
						#print(_4işlem(değerle3(parantez_çözücü(ifd,değerler),değerler)))
						#print(ifd,"anan")
						dtt=0
						gecici=parantez_çözücü2(ifd)
						
						dtt=int(listeli_ifade_çözücü(gecici))
							
						#if lojik_mi(ifd):
#							dtt=int(lojik_çözücü(değerle3(ifd,değerler)))
#						else:
#							dtt=_4işlem(değerle3(ifd,değerler))
							
						if dtt>0:
							döngüye_dön.update({satır:dtt})
							döngü_id.append(satır)
						else:
							satır=döngü_sonu_ters[satır]
						#döngüye_dön.update({satır:dtt})
#						döngü_id.append(satır)
						
						fnk_ifade.remove(fnk_ifade[-1])
						fnk_çözülecek.remove(fnk_çözülecek[-1])
						fnk_çözüm.remove(fnk_çözüm[-1])
						#fnk_çözüm=[]
					else:
						#print("deneme tata",knt2)
						#fnk_çözülecek.append(knt2[0])
						fnk_çözülecek[-1]=knt2
						fnk_çözüm.remove(fnk_çözüm[-1])
						fnkad=knt2.split("(")[0]
						fnkpr=parametre_kesici(knt2[len(fnkad)+1:-1])
						sycc=0
						lokal_parametreler.append({})
						for i in fnkpr:
							ttt=fnk_parametreler[fonksiyonlar[fnkad]][sycc]
							
							lokal_parametreler[-1].update({ttt:listeli_ifade_çözücü(parantez_çözücü2(i))})
							
							sycc+=1
						fnk_git.append(satır)
						satır=fonksiyonlar[fnkad]
				else:
					fnk_ifade.append(değerle3(itt,değerler))
					fnkad=kntls.split("(")[0]
					fnkpr=parametre_kesici(kntls[len(fnkad)+1:-1])
					#print(fnkad,fnkpr)
					fnk_çözülecek.append(kntls)
					sycc=0
					lokal_parametreler.append({})
					for i in fnkpr:
						ttt=fnk_parametreler[fonksiyonlar[fnkad]][sycc]
						
						lokal_parametreler[-1].update({ttt:listeli_ifade_çözücü(parantez_çözücü2(i))})
						
						sycc+=1
					fnk_git.append(satır)
					satır=fonksiyonlar[fnkad]
		elif "sürece" in i:
			itt=i[i.find("(")+1:bulucu_v2(i,")")[-1]]
			değerlenmiş=değerle3(itt,değerler)
			kntls=fnk_ayıkla2(değerlenmiş)
			#print("anan",kntls)
			if kntls=="":
				#değerler.update({tt[0]:_4işlem(değerle3(parantez_çözücü(tt[1],değerler),değerler))})
				#print(_4işlem(değerle3(parantez_çözücü(tt[1],değerler),değerler)))
				koşul=0
				
				gecici=parantez_çözücü2(değerlenmiş)
				
				koşul=listeli_ifade_çözücü(gecici)
				
				#if lojik_mi(itt):
#					koşul=lojik_çözücü(değerle3(parantez_çözücü2(itt,değerler),değerler))
#				else:
#					koşul=_4işlem(değerle3(parantez_çözücü2(itt,değerler),değerler))
				if(not koşul):
					satır=döngü_sonu_ters[satır]
					if döngü_id!=[]:
						döngü_id.remove(döngü_id[-1])
				else:
					if satır not in döngü_id:
						döngü_id.append(satır)
			else:
				if fnk_çözüm!=[]:
					#print("babam",fnk_ifade,fnk_çözüm)
					ifd=fnk_ifade[-1]
					
					ifd=ifd.replace(fnk_çözülecek[-1],fnk_çözüm[-1])
					
					
					fnk_ifade[-1]=ifd
					knt2=fnk_ayıkla2(ifd)
					if knt2=="":
						#print(ifd,",",fnk_çözüm,",","anan")
						#değerler.update({tt[0]:_4işlem(değerle3(parantez_çözücü(ifd,değerler),değerler))})
						#print(_4işlem(değerle3(parantez_çözücü(ifd,değerler),değerler)))
						#print(ifd,"anan")
						gecici=parantez_çözücü2(ifd)
						
						koşul=listeli_ifade_çözücü(gecici)
						
						
						#if lojik_mi(itt):
#							koşul=lojik_çözücü(değerle3(parantez_çözücü2(ifd,değerler),değerler))
#						else:
#							koşul=_4işlem(değerle3(parantez_çözücü2(ifd,değerler),değerler))
						#koşul=lojik_çözücü(değerle3(parantez_çözücü2(ifd,değerler),değerler))
						if(not koşul):
							satır=döngü_sonu_ters[satır]
							if döngü_id!=[]:
								döngü_id.remove(döngü_id[-1])
						else:
							if satır not in döngü_id:
								döngü_id.append(satır)
						
						fnk_ifade.remove(fnk_ifade[-1])
						fnk_çözülecek.remove(fnk_çözülecek[-1])
						fnk_çözüm.remove(fnk_çözüm[-1])
						#fnk_çözüm=[]
					else:
						#print("deneme tata",knt2)
						#fnk_çözülecek.append(knt2[0])
						fnk_çözülecek[-1]=knt2
						fnk_çözüm.remove(fnk_çözüm[-1])
						fnkad=knt2.split("(")[0]
						fnkpr=parametre_kesici(knt2[len(fnkad)+1:-1])
						sycc=0
						lokal_parametreler.append({})
						for i in fnkpr:
							ttt=fnk_parametreler[fonksiyonlar[fnkad]][sycc]
							
							lokal_parametreler[-1].update({ttt:listeli_ifade_çözücü(parantez_çözücü2(i))})
							
							sycc+=1
						fnk_git.append(satır)
						satır=fonksiyonlar[fnkad]
				else:
					fnk_ifade.append(değerle3(itt,değerler))
					fnkad=kntls.split("(")[0]
					fnkpr=parametre_kesici(kntls[len(fnkad)+1:-1])
					#print(fnkad,fnkpr)
					fnk_çözülecek.append(kntls)
					sycc=0
					lokal_parametreler.append({})
					for i in fnkpr:
						ttt=fnk_parametreler[fonksiyonlar[fnkad]][sycc]
						
						lokal_parametreler[-1].update({ttt:listeli_ifade_çözücü(parantez_çözücü2(i))})
						
						sycc+=1
					fnk_git.append(satır)
					satır=fonksiyonlar[fnkad]
			
		elif "eğer" in i:
			itt=i[i.find("(")+1:bulucu_v2(i,")")[-1]]
			değerlenmiş=değerle3(itt,değerler)
			kntls=fnk_ayıkla2(değerlenmiş)
			#print("anan",kntls)
			if kntls=="":
				#değerler.update({tt[0]:_4işlem(değerle3(parantez_çözücü(tt[1],değerler),değerler))})
				#print(_4işlem(değerle3(parantez_çözücü(tt[1],değerler),değerler)))
				koşul=0
				
				gecici=parantez_çözücü2(değerlenmiş)
				
				koşul=listeli_ifade_çözücü(gecici)
				
				#if lojik_mi(itt):
#					koşul=lojik_çözücü(değerle3(parantez_çözücü2(itt,değerler),değerler))
#				else:
#					koşul=_4işlem(değerle3(parantez_çözücü2(itt,değerler),değerler))
				if(not koşul):
					satır=döngü_sonu_ters[satır]
			else:
				if fnk_çözüm!=[]:
					#print("babam",fnk_ifade,fnk_çözüm)
					ifd=fnk_ifade[-1]
					
					ifd=ifd.replace(fnk_çözülecek[-1],fnk_çözüm[-1])
					
					
					fnk_ifade[-1]=ifd
					knt2=fnk_ayıkla2(ifd)
					#print("ebeeeen",ifd,knt2,değerler)
					if knt2=="":
						#print(ifd,",",fnk_çözüm,",","anan")
						#değerler.update({tt[0]:_4işlem(değerle3(parantez_çözücü(ifd,değerler),değerler))})
						#print(_4işlem(değerle3(parantez_çözücü(ifd,değerler),değerler)))
						#print(ifd,"anan")
						
						#print("hasssss",ifd)
						gecici=parantez_çözücü2(ifd)
						
						
						koşul=listeli_ifade_çözücü(gecici)
						
						#koşul=lojik_çözücü(değerle3(parantez_çözücü2(ifd,değerler),değerler))
						if(not koşul):
							satır=döngü_sonu_ters[satır]
						
						fnk_ifade.remove(fnk_ifade[-1])
						fnk_çözülecek.remove(fnk_çözülecek[-1])
						fnk_çözüm.remove(fnk_çözüm[-1])
						#fnk_çözüm=[]
					else:
						#print("deneme tata",knt2)
						#fnk_çözülecek.append(knt2[0])
						fnk_çözülecek[-1]=knt2
						fnk_çözüm.remove(fnk_çözüm[-1])
						fnkad=knt2.split("(")[0]
						fnkpr=parametre_kesici(knt2[len(fnkad)+1:-1])
						sycc=0
						lokal_parametreler.append({})
						for i in fnkpr:
							ttt=fnk_parametreler[fonksiyonlar[fnkad]][sycc]
							
							lokal_parametreler[-1].update({ttt:listeli_ifade_çözücü(parantez_çözücü2(i))})
							
							sycc+=1
						fnk_git.append(satır)
						satır=fonksiyonlar[fnkad]
				else:
					fnk_ifade.append(değerle3(itt,değerler))
					fnkad=kntls.split("(")[0]
					fnkpr=parametre_kesici(kntls[len(fnkad)+1:-1])
					#print(fnkad,fnkpr)
					fnk_çözülecek.append(kntls)
					sycc=0
					lokal_parametreler.append({})
					for i in fnkpr:
						ttt=fnk_parametreler[fonksiyonlar[fnkad]][sycc]
						
						lokal_parametreler[-1].update({ttt:listeli_ifade_çözücü(parantez_çözücü2(i))})
						
						sycc+=1
					fnk_git.append(satır)
					satır=fonksiyonlar[fnkad]
		elif "kır" in i:
			if döngü_id!=[]:
				if döngü_id[-1] in döngü_sonu_ters:
					satır=döngü_sonu_ters[döngü_id[-1]]
					if döngü_id!=[]:
						döngü_id.remove(döngü_id[-1])
		elif "devam" in i:
			if döngü_id!=[]:
				if döngü_id[-1] in döngü_sonu_ters:
					#print("loooo",döngü_id[-1],döngü_sonu_ters)
					satır=döngü_sonu_ters[döngü_id[-1]]-1
		elif "}" in i:
			#print("hasss",döngüye_dön)
			if döngü_sonu[satır] not in eğerler:
				tetikleme=True
				if döngü_sonu[satır] in süreceler:
					satır=döngü_sonu[satır]
					satır-=1
					tetikleme=False
				if döngüye_dön!={} and tetikleme and döngü_sonu[satır] in döngüye_dön:
					if döngüye_dön[döngü_sonu[satır]]>1:
						döngüye_dön[döngü_sonu[satır]]-=1
						satır=döngü_sonu[satır]
					else:
						if döngü_id!=[]:
							döngü_id.remove(döngü_id[-1])
							#döngü_id=döngü_id[:-1]
		elif eşittir_bulucu(i)>0:
			tt=i[eşittir_bulucu(i)+1:]
			dgri=i[:eşittir_bulucu(i)]
			
			index_konum=dgri.find("[")
			if index_konum!=-1:
				dgri_2=dgri[:index_konum]
				ifade=dgri[index_konum:]
				
				ifade=değerle3(ifade,değerler)
				
				kntls=fnk_ayıkla2(ifade)
				#print("değeri",dgri_2,"ve",ifade)
				katmanlar=değer_index_ayırıcı(ifade)
				if kntls=="":
					gecici=değerle3(tt,değerler)
					index_id_ls=[]
					for i in katmanlar:
						index_id_ls.append(listeli_ifade_çözücü(i))
					
					if lokal_parametreler!=[]:
						if dgri in lokal_parametreler[-1]:
							lokal_parametreler[-1].update({dgri_2:ls_eleman_degistir(lokal_parametreler[dgri_2],index_id_ls,listeli_ifade_çözücü(gecici))})
						else:
							değerler_global.update({dgri_2:ls_eleman_degistir(değerler_global[dgri_2],index_id_ls,listeli_ifade_çözücü(gecici))})
					else:
						#print("loooo31",ls_eleman_degistir(değerler_global[dgri_2],index_id_ls,listeli_ifade_çözücü(gecici)))
						değerler_global.update({dgri_2:ls_eleman_degistir(değerler_global[dgri_2],index_id_ls,listeli_ifade_çözücü(gecici))})
					
				else:
					if fnk_ifade==[]:
						indexte_fonksiyon=True
					#print("indexte fonksiyon var")
					if indexte_fonksiyon:
						if fnk_çözüm!=[]:
							#print("babam",fnk_ifade,fnk_çözüm)
							ifd=fnk_ifade[-1]
							
							ifd=ifd.replace(fnk_çözülecek[-1],fnk_çözüm[-1])
								
								
							fnk_ifade[-1]=ifd
							knt2=fnk_ayıkla2(ifd)
							if knt2=="":
								
								#print("hassss",ifd)
								gecici=parantez_çözücü2(ifd)
								
								katmanlar=değer_index_ayırıcı(gecici)
								
								
								indexte_fonksiyon=False
								indexte_fonksiyon_bitti=True
								
								indexte_fonksiyon_çözülmüş=[]
								
								for i in katmanlar:
									#print("hassss69",i)
									indexte_fonksiyon_çözülmüş.append(listeli_ifade_çözücü(i))
								
								
								fnk_ifade.remove(fnk_ifade[-1])
								fnk_çözülecek.remove(fnk_çözülecek[-1])
								fnk_çözüm.remove(fnk_çözüm[-1])
								#fnk_çözüm=[]
							else:
								
								fnk_çözülecek[-1]=knt2
								fnk_çözüm.remove(fnk_çözüm[-1])
								fnkad=knt2.split("(")[0]
								fnkpr=parametre_kesici(knt2[len(fnkad)+1:-1])
								sycc=0
								lokal_parametreler.append({})
								for i in fnkpr:
									ttt=fnk_parametreler[fonksiyonlar[fnkad]][sycc]
									lokal_parametreler[-1].update({ttt:listeli_ifade_çözücü(parantez_çözücü2(i))})
									sycc+=1
								fnk_git.append(satır)
								
								
								
								satır=fonksiyonlar[fnkad]
						else:
							fnk_ifade.append(değerle3(ifade,değerler))
							fnkad=kntls.split("(")[0]
							fnkpr=parametre_kesici(kntls[len(fnkad)+1:-1])
							#print(fnkad,fnkpr)
							fnk_çözülecek.append(kntls)
							sycc=0
							lokal_parametreler.append({})
							for i in fnkpr:
								ttt=fnk_parametreler[fonksiyonlar[fnkad]][sycc]
								lokal_parametreler[-1].update({ttt:listeli_ifade_çözücü(parantez_çözücü2(i))})
								sycc+=1
							fnk_git.append(satır)
							satır=fonksiyonlar[fnkad]
						#bitti
					if indexte_fonksiyon_bitti:
						print("index bitti",indexte_fonksiyon_çözülmüş)
						if fnk_çözüm!=[]:
							#print("babam",fnk_ifade,fnk_çözüm)
							ifd=fnk_ifade[-1]
							
							ifd=ifd.replace(fnk_çözülecek[-1],fnk_çözüm[-1])
								
								
							fnk_ifade[-1]=ifd
							knt2=fnk_ayıkla2(ifd)
							if knt2=="":
								
								#print("hassss",ifd)
								gecici=parantez_çözücü2(ifd)
								
								katmanlar=değer_index_ayırıcı(gecici)
								
								
								indexte_fonksiyon=False
								indexte_fonksiyon_bitti=False
								
								if lokal_parametreler!=[]:
									if dgri in lokal_parametreler[-1]:
										lokal_parametreler[-1].update({dgri_2:ls_eleman_degistir(lokal_parametreler[dgri_2],indexte_fonksiyon_çözülmüş,listeli_ifade_çözücü(gecici))})
									else:
										değerler_global.update({dgri_2:ls_eleman_degistir(değerler_global[dgri_2],indexte_fonksiyon_çözülmüş,listeli_ifade_çözücü(gecici))})
								else:
									#print("loooo31",ls_eleman_degistir(değerler_global[dgri_2],index_id_ls,listeli_ifade_çözücü(gecici)))
									değerler_global.update({dgri_2:ls_eleman_degistir(değerler_global[dgri_2],indexte_fonksiyon_çözülmüş,listeli_ifade_çözücü(gecici))})
								
								fnk_ifade.remove(fnk_ifade[-1])
								fnk_çözülecek.remove(fnk_çözülecek[-1])
								fnk_çözüm.remove(fnk_çözüm[-1])
								#fnk_çözüm=[]
							else:
								
								fnk_çözülecek[-1]=knt2
								fnk_çözüm.remove(fnk_çözüm[-1])
								fnkad=knt2.split("(")[0]
								fnkpr=parametre_kesici(knt2[len(fnkad)+1:-1])
								sycc=0
								lokal_parametreler.append({})
								for i in fnkpr:
									ttt=fnk_parametreler[fonksiyonlar[fnkad]][sycc]
									lokal_parametreler[-1].update({ttt:listeli_ifade_çözücü(parantez_çözücü2(i))})
									sycc+=1
								fnk_git.append(satır)
								
								
								
								satır=fonksiyonlar[fnkad]
						else:
							fnk_ifade.append(değerle3(tt,değerler))
							fnkad=kntls.split("(")[0]
							fnkpr=parametre_kesici(kntls[len(fnkad)+1:-1])
							#print(fnkad,fnkpr)
							fnk_çözülecek.append(kntls)
							sycc=0
							lokal_parametreler.append({})
							for i in fnkpr:
								ttt=fnk_parametreler[fonksiyonlar[fnkad]][sycc]
								lokal_parametreler[-1].update({ttt:listeli_ifade_çözücü(parantez_çözücü2(i))})
								sycc+=1
							fnk_git.append(satır)
							satır=fonksiyonlar[fnkad]
					#bitti2
			else:
				kntls=fnk_ayıkla2(değerle3(tt,değerler))
					
				print("kaç kere oldu",kntls,fnk_git)
					
				#print("anan3131",kntls)
				if kntls=="":
					gecici=parantez_çözücü2(değerle3(tt,değerler))
					#print("hassss",gecici)
					#print("hızzz",değerle3(tt,değerler))
					#print(dgri,"ve",gecici)
					if lokal_parametreler!=[]:
						if dgri in lokal_parametreler[-1]:
							lokal_parametreler[-1].update({dgri:listeli_ifade_çözücü(gecici)})
						else:
							değerler_global.update({dgri:listeli_ifade_çözücü(gecici)})
					else:
						değerler_global.update({dgri:listeli_ifade_çözücü(gecici)})
				else:
					if fnk_çözüm!=[]:
						#print("babam",fnk_ifade,fnk_çözüm)
						ifd=fnk_ifade[-1]
						
						ifd=ifd.replace(fnk_çözülecek[-1],fnk_çözüm[-1])
							
							
						fnk_ifade[-1]=ifd
						knt2=fnk_ayıkla2(ifd)
						if knt2=="":
							#print(ifd,",",fnk_çözüm,",","anan")
							
							gecici=parantez_çözücü2(ifd)
							if lokal_parametreler!=[]:
								if dgri in lokal_parametreler[-1]:
									lokal_parametreler[-1].update({dgri:listeli_ifade_çözücü(gecici)})
								else:
									değerler_global.update({dgri:listeli_ifade_çözücü(gecici)})
							else:
								değerler_global.update({dgri:listeli_ifade_çözücü(gecici)})
							#değerler.update({dgri:_4işlem(değerle3(parantez_çözücü2(ifd,değerler),değerler))})
							
							
							fnk_ifade.remove(fnk_ifade[-1])
							fnk_çözülecek.remove(fnk_çözülecek[-1])
							fnk_çözüm.remove(fnk_çözüm[-1])
							#fnk_çözüm=[]
						else:
							#print("deneme tata",knt2)
							#fnk_çözülecek.append(knt2[0])
							
							#print("test amaçlı",fnk_ifade)
							#print("test amaçlı2",fnk_çözülecek)
							#print("test amaçlı3",fnk_çözüm)
							
							
							fnk_çözülecek[-1]=knt2
							fnk_çözüm.remove(fnk_çözüm[-1])
							fnkad=knt2.split("(")[0]
							fnkpr=parametre_kesici(knt2[len(fnkad)+1:-1])
							sycc=0
							lokal_parametreler.append({})
							for i in fnkpr:
								ttt=fnk_parametreler[fonksiyonlar[fnkad]][sycc]
								lokal_parametreler[-1].update({ttt:listeli_ifade_çözücü(parantez_çözücü2(i))})
								sycc+=1
							fnk_git.append(satır)
							
							
							
							satır=fonksiyonlar[fnkad]
					else:
						fnk_ifade.append(değerle3(tt,değerler))
						fnkad=kntls.split("(")[0]
						fnkpr=parametre_kesici(kntls[len(fnkad)+1:-1])
						#print(fnkad,fnkpr)
						fnk_çözülecek.append(kntls)
						sycc=0
						lokal_parametreler.append({})
						for i in fnkpr:
							ttt=fnk_parametreler[fonksiyonlar[fnkad]][sycc]
							lokal_parametreler[-1].update({ttt:listeli_ifade_çözücü(parantez_çözücü2(i))})
							sycc+=1
						fnk_git.append(satır)
						satır=fonksiyonlar[fnkad]
		else:
			pass
		satır+=1
		#print("değerler>",değerler)
#		print("satır:",satırlar[satır])


	
print(lojik_çözücü("90<=90 ve 10<20 ve 31>=32"))
	
st="(24==faktör(1 ve (10==12)) ve asd(10==10))"
st="a[topla(1==1 veya 2<=3,2)][2][çarp(2,3)-çarp(5,6)]=çarp(20,3)+100"
print(fnk_ayıkla(st))

print(listeli_ifade_çözücü("[10,20,[3]+[(10-8)*(4+1)]*2+[3],50][2][1:][-1]+300/200"))

denem="""

fonksiyon topla(a,b){
döndür a+b
}
fonksiyon çarp(a,b){
döndür a*b
}

a=topla(2,3)+çarp(8,7)

yazdır a
"""


kod_oku(denem)

#print(parantez_çözücü2("topla(10,20)+10"))
