import re,time

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

def değerle3(a,b):
	kt=" +-*/()><!=,"
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
				dgst=str(gerekli_float(float(b[e])))
				a=a[0:i]+dgst+a[i+len(e):]
				artt+=len(dgst)-len(e)
	return a

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
		#print("___",dztt)
		return bool(_4işlem(dztt))
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
			degis=str(gerekli_float(_4işlem(i[0][1:-1])))
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
		if i=="=" and not ard and not est:
			dd=syc
			est=True
		if syc-dd==1 and est and not ard:
			if i!="=":
				eksl=1
				break
			else:
				print("loo")
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
		if i.isnumeric() or i in "().,+-*/<>!= ":
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
			if fnb and prsy==dısy and i in ".,+-*/<>!= ":
				fnb=False
				fbt=True
				fn=""
			if icf and  i in ".,+-*/<>!= ":
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
		if i.isdigit() or i in "().,+-*/<>!= ":
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
			kntls=fnk_ayıkla2(değerle3(asdtt,değerler))
			
			#print("hassss",asdtt)
			
			if kntls=="":
				#değerler.update({tt[0]:_4işlem(değerle3(parantez_çözücü(tt[1],değerler),değerler))})
				satır=fnk_git[-1]-1
				if lojik_mi(asdtt):
					fnk_çözüm.append(str(int(lojik_çözücü(değerle3(parantez_çözücü2(asdtt,değerler),değerler)))))
					#print("ananhass",asdtt,"ve",str(_4işlem(değerle3(parantez_çözücü2(asdtt,değerler),değerler))))
				else:
					fnk_çözüm.append(str(_4işlem(parantez_çözücü2(değerle3(asdtt,değerler)))))
				
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
						if lojik_mi(ifd):
							fnk_çözüm.append(str(int(lojik_çözücü(değerle3(parantez_çözücü2(ifd,değerler),değerler)))))
						else:
							fnk_çözüm.append(str(_4işlem(parantez_çözücü2(değerle3(ifd,değerler)))))
				
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
						fnkpr=knt2[len(fnkad)+1:-1].split(",")
						sycc=0
						lokal_parametreler.append({})
						for i in fnkpr:
							ttt=fnk_parametreler[fonksiyonlar[fnkad]][sycc]
							#lokal_parametreler[-1].update({ttt:_4işlem(parantez_çözücü2(i,değerler))})
							if lojik_mi(i):
								lokal_parametreler[-1].update({ttt:int(lojik_çözücü(parantez_çözücü2(i)))})
							else:
								lokal_parametreler[-1].update({ttt:_4işlem(parantez_çözücü2(i))})
							sycc+=1
						fnk_git.append(satır)
						satır=fonksiyonlar[fnkad]
				else:
					fnk_ifade.append(değerle3(asdtt,değerler))
					fnkad=kntls.split("(")[0]
					fnkpr=kntls[len(fnkad)+1:-1].split(",")
					#print(fnkad,fnkpr)
					fnk_çözülecek.append(kntls)
					sycc=0
					lokal_parametreler.append({})
					for i in fnkpr:
						ttt=fnk_parametreler[fonksiyonlar[fnkad]][sycc]
						#lokal_parametreler[-1].update({ttt:_4işlem(parantez_çözücü2(i,değerler))})
						if lojik_mi(i):
							lokal_parametreler[-1].update({ttt:int(lojik_çözücü(parantez_çözücü2(i)))})
						else:
							lokal_parametreler[-1].update({ttt:_4işlem(parantez_çözücü2(i))})
						sycc+=1
					fnk_git.append(satır)
					satır=fonksiyonlar[fnkad]
			
			
			
		elif "fonksiyon" in i:
			satır=döngü_sonu_ters[satır]
		elif "yazdır" in i:
			tt=i[len("yazdır")+1:]
			kntls=fnk_ayıkla2(değerle3(tt,değerler))
			
			
			if kntls=="":
				#değerler.update({tt[0]:_4işlem(değerle3(parantez_çözücü(tt[1],değerler),değerler))})
				gecici=parantez_çözücü2(değerle3(tt,değerler))
				
				if lojik_mi(gecici):
					print(lojik_çözücü(parantez_çözücü2(değerle3(tt,değerler))))
				else:
					print(_4işlem(parantez_çözücü2(değerle3(tt,değerler))))
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
						if lojik_mi(gecici):
							#print("hass",ifd)
							print(lojik_çözücü(gecici))
						else:
							print(_4işlem(gecici))
						
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
						fnkpr=knt2[len(fnkad)+1:-1].split(",")
						sycc=0
						lokal_parametreler.append({})
						for i in fnkpr:
							ttt=fnk_parametreler[fonksiyonlar[fnkad]][sycc]
							if lojik_mi(i):
								lokal_parametreler[-1].update({ttt:int(lojik_çözücü(parantez_çözücü2(i)))})
							else:
								lokal_parametreler[-1].update({ttt:_4işlem(parantez_çözücü2(i))})
							sycc+=1
						fnk_git.append(satır)
						satır=fonksiyonlar[fnkad]
				else:
					fnk_ifade.append(değerle3(tt,değerler))
					fnkad=kntls.split("(")[0]
					fnkpr=kntls[len(fnkad)+1:-1].split(",")
					#print(fnkad,fnkpr)
					fnk_çözülecek.append(kntls)
					sycc=0
					lokal_parametreler.append({})
					for i in fnkpr:
						ttt=fnk_parametreler[fonksiyonlar[fnkad]][sycc]
						if lojik_mi(i):
							lokal_parametreler[-1].update({ttt:int(lojik_çözücü(parantez_çözücü2(i)))})
						else:
							lokal_parametreler[-1].update({ttt:_4işlem(parantez_çözücü2(i))})
						sycc+=1
					fnk_git.append(satır)
					satır=fonksiyonlar[fnkad]
			
		elif "tekrarla" in i:
			itt=i[bulucu_v2(i,"(")[0]+1:-2]
			kntls=fnk_ayıkla2(değerle3(itt,değerler))
			
			#print("looo",kntls,itt)
			if kntls=="":
				#değerler.update({tt[0]:_4işlem(değerle3(parantez_çözücü(tt[1],değerler),değerler))})
				#print(_4işlem(değerle3(parantez_çözücü(tt[1],değerler),değerler)))
				dtt=0
				gecici=parantez_çözücü2(değerle3(itt,değerler))
				if lojik_mi(itt):
					dtt=int(lojik_çözücü(gecici))
				else:
					dtt=_4işlem(gecici)
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
						if lojik_mi(gecici):
							dtt=int(lojik_çözücü(gecici))
						else:
							dtt=_4işlem(gecici)
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
						fnkpr=knt2[len(fnkad)+1:-1].split(",")
						sycc=0
						lokal_parametreler.append({})
						for i in fnkpr:
							ttt=fnk_parametreler[fonksiyonlar[fnkad]][sycc]
							if lojik_mi(i):
								lokal_parametreler[-1].update({ttt:int(lojik_çözücü(parantez_çözücü2(i)))})
							else:
								lokal_parametreler[-1].update({ttt:_4işlem(parantez_çözücü2(i))})
							sycc+=1
						fnk_git.append(satır)
						satır=fonksiyonlar[fnkad]
				else:
					fnk_ifade.append(değerle3(itt,değerler))
					fnkad=kntls.split("(")[0]
					fnkpr=kntls[len(fnkad)+1:-1].split(",")
					#print(fnkad,fnkpr)
					fnk_çözülecek.append(kntls)
					sycc=0
					lokal_parametreler.append({})
					for i in fnkpr:
						ttt=fnk_parametreler[fonksiyonlar[fnkad]][sycc]
						if lojik_mi(i):
							lokal_parametreler[-1].update({ttt:int(lojik_çözücü(parantez_çözücü2(i)))})
						else:
							lokal_parametreler[-1].update({ttt:_4işlem(parantez_çözücü2(i))})
						sycc+=1
					fnk_git.append(satır)
					satır=fonksiyonlar[fnkad]
		elif "sürece" in i:
			itt=i[i.find("(")+1:bulucu_v2(i,")")[-1]]
			kntls=fnk_ayıkla2(değerle3(itt,değerler))
			#print("anan",kntls)
			if kntls=="":
				#değerler.update({tt[0]:_4işlem(değerle3(parantez_çözücü(tt[1],değerler),değerler))})
				#print(_4işlem(değerle3(parantez_çözücü(tt[1],değerler),değerler)))
				koşul=0
				
				gecici=parantez_çözücü2(değerle3(itt,değerler))
				if lojik_mi(gecici):
					koşul=lojik_çözücü(gecici)
				else:
					koşul=_4işlem(gecici)
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
						if lojik_mi(gecici):
							dtt=int(lojik_çözücü(gecici))
						else:
							dtt=_4işlem(gecici)
						
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
						fnkpr=knt2[len(fnkad)+1:-1].split(",")
						sycc=0
						lokal_parametreler.append({})
						for i in fnkpr:
							ttt=fnk_parametreler[fonksiyonlar[fnkad]][sycc]
							if lojik_mi(i):
								lokal_parametreler[-1].update({ttt:int(lojik_çözücü(parantez_çözücü2(i)))})
							else:
								lokal_parametreler[-1].update({ttt:_4işlem(parantez_çözücü2(i))})
							sycc+=1
						fnk_git.append(satır)
						satır=fonksiyonlar[fnkad]
				else:
					fnk_ifade.append(değerle3(itt,değerler))
					fnkad=kntls.split("(")[0]
					fnkpr=kntls[len(fnkad)+1:-1].split(",")
					#print(fnkad,fnkpr)
					fnk_çözülecek.append(kntls)
					sycc=0
					lokal_parametreler.append({})
					for i in fnkpr:
						ttt=fnk_parametreler[fonksiyonlar[fnkad]][sycc]
						if lojik_mi(i):
							lokal_parametreler[-1].update({ttt:int(lojik_çözücü(parantez_çözücü2(i)))})
						else:
							lokal_parametreler[-1].update({ttt:_4işlem(parantez_çözücü2(i))})
						sycc+=1
					fnk_git.append(satır)
					satır=fonksiyonlar[fnkad]
			
		elif "eğer" in i:
			itt=i[i.find("(")+1:bulucu_v2(i,")")[-1]]
			kntls=fnk_ayıkla2(değerle3(itt,değerler))
			#print("anan",kntls)
			if kntls=="":
				#değerler.update({tt[0]:_4işlem(değerle3(parantez_çözücü(tt[1],değerler),değerler))})
				#print(_4işlem(değerle3(parantez_çözücü(tt[1],değerler),değerler)))
				koşul=0
				
				gecici=parantez_çözücü2(değerle3(itt,değerler))
				if lojik_mi(itt):
					koşul=int(lojik_çözücü(gecici))
				else:
					koşul=_4işlem(gecici)
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
						if lojik_mi(itt):
							koşul=int(lojik_çözücü(gecici))
						else:
							koşul=_4işlem(gecici)
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
						fnkpr=knt2[len(fnkad)+1:-1].split(",")
						sycc=0
						lokal_parametreler.append({})
						for i in fnkpr:
							ttt=fnk_parametreler[fonksiyonlar[fnkad]][sycc]
							if lojik_mi(i):
								lokal_parametreler[-1].update({ttt:int(lojik_çözücü(parantez_çözücü2(i)))})
							else:
								lokal_parametreler[-1].update({ttt:_4işlem(parantez_çözücü2(i))})
							sycc+=1
						fnk_git.append(satır)
						satır=fonksiyonlar[fnkad]
				else:
					fnk_ifade.append(değerle3(itt,değerler))
					fnkad=kntls.split("(")[0]
					fnkpr=kntls[len(fnkad)+1:-1].split(",")
					#print(fnkad,fnkpr)
					fnk_çözülecek.append(kntls)
					sycc=0
					lokal_parametreler.append({})
					for i in fnkpr:
						ttt=fnk_parametreler[fonksiyonlar[fnkad]][sycc]
						if lojik_mi(i):
							lokal_parametreler[-1].update({ttt:int(lojik_çözücü(parantez_çözücü2(i)))})
						else:
							lokal_parametreler[-1].update({ttt:_4işlem(parantez_çözücü2(i))})
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
			
			#print(dgri,"***",tt)
			kntls=fnk_ayıkla2(değerle3(tt,değerler))
				
				
			#print("anan3131",kntls)
			if kntls=="":
				gecici=parantez_çözücü2(değerle3(tt,değerler))
				#print("hızzz",değerle3(tt,değerler))
				#print(dgri,"ve",gecici)
				if lokal_parametreler!=[]:
					if dgri in lokal_parametreler[-1]:
						if lojik_mi(gecici):
							lokal_parametreler[-1].update({dgri:lojik_çözücü(gecici)})
						else:
							lokal_parametreler[-1].update({dgri:_4işlem(gecici)})
					else:
						if lojik_mi(gecici):
							değerler_global.update({dgri:lojik_çözücü(gecici)})
						else:
							değerler_global.update({dgri:_4işlem(gecici)})
				else:
					if lojik_mi(gecici):
						değerler_global.update({dgri:lojik_çözücü(gecici)})
					else:
						değerler_global.update({dgri:_4işlem(gecici)})
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
								if lojik_mi(gecici):
									lokal_parametreler[-1].update({dgri:lojik_çözücü(gecici)})
								else:
									lokal_parametreler[-1].update({dgri:_4işlem(gecici)})
							else:
								if lojik_mi(gecici):
									değerler_global.update({dgri:lojik_çözücü(gecici)})
								else:
									değerler_global.update({dgri:_4işlem(gecici)})
						else:
							if lojik_mi(gecici):
								değerler_global.update({dgri:lojik_çözücü(gecici)})
							else:
								değerler_global.update({dgri:_4işlem(gecici)})
						#değerler.update({dgri:_4işlem(değerle3(parantez_çözücü2(ifd,değerler),değerler))})
						
						
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
						fnkpr=knt2[len(fnkad)+1:-1].split(",")
						sycc=0
						lokal_parametreler.append({})
						for i in fnkpr:
							ttt=fnk_parametreler[fonksiyonlar[fnkad]][sycc]
							if lojik_mi(i):
								lokal_parametreler[-1].update({ttt:int(lojik_çözücü(parantez_çözücü2(i)))})
							else:
								lokal_parametreler[-1].update({ttt:_4işlem(parantez_çözücü2(i))})
							sycc+=1
						fnk_git.append(satır)
						satır=fonksiyonlar[fnkad]
				else:
					fnk_ifade.append(değerle3(tt,değerler))
					fnkad=kntls.split("(")[0]
					fnkpr=kntls[len(fnkad)+1:-1].split(",")
					#print(fnkad,fnkpr)
					fnk_çözülecek.append(kntls)
					sycc=0
					lokal_parametreler.append({})
					for i in fnkpr:
						ttt=fnk_parametreler[fonksiyonlar[fnkad]][sycc]
						if lojik_mi(i):
							lokal_parametreler[-1].update({ttt:int(lojik_çözücü(parantez_çözücü2(i)))})
						else:
							lokal_parametreler[-1].update({ttt:_4işlem(parantez_çözücü2(i))})
						sycc+=1
					fnk_git.append(satır)
					satır=fonksiyonlar[fnkad]
		else:
			pass
		satır+=1
		#print("değerler>",değerler)
#		print("satır:",satırlar[satır])
	
	
	
st="(24==faktör(1 ve (10==12)) ve asd(10==10))"
st="topla((10>2 ve 10==12-2) veya (20<30 ve 10>8)) ve faktör(3)"
print(fnk_ayıkla(st))



denem="""

dd=30
a=300

fonksiyon faktör(a){
eğer(a==1){
döndür 1
}
döndür a*faktör(a-1)
}
fonksiyon deneme(a,b){
a=a+100
yazdır a
yazdır b
döndür 3169
}

yazdır faktör(5)

yazdır deneme(10,20)
yazdır a

fonksiyon değil(a){
eğer(a==0){
döndür 1
}
döndür 0
}
syc=0+1

eğer(değil(syc==1) ve syc<10){
yazdır 4131
}

fonksiyon üs(a,b){
dnd=1
tekrarla(b){
dnd=dnd*a
}
döndür dnd
}

fonksiyon kaç_basamaklı(a){
bsmk=1
üs_no=1
sürece(bsmk*10<a){
bsmk=bsmk*10
üs_no=üs_no+1
}
döndür üs_no
}

fonksiyon böl(a,b){
syc=0
sürece(a>b veya a==b){
a=a-b
syc=syc+1
}
döndür syc
}

fonksiyon kalan(a,b){
sürece(a>b veya a==b){
a=a-b
}
döndür a
}

fonksiyon sayı_ters_çevir(a){
basamak_sayı=kaç_basamaklı(a)
on_kuvvet=üs(10,basamak_sayı-1)
dnd=0
üs_art=0

sürece(on_kuvvet>1 veya on_kuvvet==1){
dnd=dnd+böl(a,on_kuvvet)*üs(10,üs_art)
a=kalan(a,on_kuvvet)
üs_art=üs_art+1
on_kuvvet=on_kuvvet/10
}

döndür dnd
}

fonksiyon asal_mı(a){
dnd=1
blnn=2
eğer(a<2){
döndür 0
}
sürece(a/blnn>blnn veya a/blnn==blnn){
eğer(kalan(a,blnn)==0){
dnd=0
kır
}
blnn=blnn+1
}
döndür dnd
}

yazdır sayı_ters_çevir(78)

yazdır değil(1) veya değil(0)-1

yazdır asal_mı(9+2)+4000

syc=0
tekrarla(1000){
yazdır syc
syc=syc+1
}

syc1=0
tekrarla(100){
eğer(asal_mı(syc1)){
yazdır syc1
}
syc1=syc1+1
}
"""


kod_oku(denem)


#print("başla bizim")
#zmn=time.time()
#print(_4işlem(parantez_çözücü2("(10-8)*(4+1)")))
#print("sürdü bizim",100*(time.time()-zmn))

#print("başla hızlı")
#zmn=time.time()
#print(_4işlem(parantez_çözücü2_hızlı("(10-8)*(4+1)")))
#print("sürdü hızlı",100*(time.time()-zmn))


#print("başla")
#zmn=time.time()
#print((10-8)*(4+1))
#print("sürdü",100*(time.time()-zmn))



