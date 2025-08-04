from cenksp import *


def işlem_mi(st):
	return "*" in st or "/" in st or "+" in st or "-" in st
def ls_eleman_elde(a,knm):
	for e in knm:
		tt=""
		drt=0
		basla=False
		syc=0
		for i in a:
			if i=="[" and not basla:
				basla=True
			elif i=="[" and basla:
				tt=tt+i
				drt+=1
			elif i=="]" and drt==0:
				if syc==e:
					a=tt
					break
				syc+=1
			elif i=="]" and drt!=0:
				tt+=i
				drt-=1
			elif i=="," and not drt!=0:
				if syc==e:
					a=tt
					break
				syc+=1
				#print(tt)
				tt=""
			elif i=="," and not drt==0:
				tt+=i
			else:
				tt+=i
	return a

def ls_eleman_uzunluk(a):
	tt=""
	drt=0
	basla=False
	syc=0
	dnd=0
	for i in a:
		if i=="[" and not basla:
			basla=True
		elif i=="[" and basla:
			drt+=1
		elif i=="]" and drt==0:
			dnd+=1
		elif i=="]" and drt!=0:
			tt+=i
			drt-=1
		elif i=="," and not drt!=0:
			dnd+=1
		elif i=="," and not drt==0:
			pass
		else:
			pass
	return dnd
def ls_eleman_sırala(a):
	tt=""
	drt=0
	basla=False
	syc=0
	for i in a:
		if i=="[" and not basla:
			basla=True
		elif i=="[" and basla:
			tt=tt+i
			drt+=1
		elif i=="]" and drt==0:
			print(tt)
		elif i=="]" and drt!=0:
			tt+=i
			drt-=1
		elif i=="," and not drt!=0:
			print(tt)
			tt=""
		elif i=="," and not drt==0:
			tt+=i
		else:
			tt+=i



#st="[1,3,5,[1,2],10]*3*10+[10,[15,5]]*10+[1,2,3]"

def ls_carp2(st):
	print("tt",st)
	ls=""
	çs=""
	psy=0
	çbs=False
	syc=0
	çrp=1
	for i in st:
		if i=="[":
			psy+=1
		elif i=="]":
			psy-=1
		elif i=="*" and psy==0 and not çbs:
			print("looo",ls)
			çbs=True
		elif i=="*" and çbs:
			çrp*=int(float(çs))
			çs=""
		if not çbs:
			ls+=i
		elif i!="*":
			çs+=i
		if syc==len(st)-1 and çbs:
			çrp*=int(float(çs))
		syc+=1
	#print("ccc",ls)
	if çbs:
		if çrp==0:
			return "[]"
		else:
			return "["+(ls[1:-1]+",")*(çrp-1)+ls[1:-1]+"]"
	else:
		return ls




def ls_altı(st):
	#print("hadidayı",st)
	ls=""
	id=""
	psy=0
	syc=0
	bsl=False
	bsl2=False
	bsl3=False
	for i in st:
		if i=="[":
			if bsl:
				bsl2=True
			if psy==0 and bsl2:
				if bsl3:
					#print("index",id)
					ls=ls_altı_mini(ls,id)
					id=""
			psy+=1
		elif i=="]":
			psy-=1
			if not bsl and psy==0:
				bsl=True
			if bsl2 and psy==0:
				bsl3=True
		if not bsl2:
			ls+=i
		else:
			id+=i
		if syc==len(st)-1:
			#print("index",id)
			#print("hığğğ",ls)
			ls=ls_altı_mini(ls,id)
		syc+=1
	#print("neden",ls)
	return ls
def ls_altı_mini(dz,id):
	#print("işlenecek",dz,id)
	syc=0
	psy=0
	tt=""
	ls=[]
	id=id[1:-1]
	#print("hass",id)
	for i in id:
		if i=="[":
			psy+=1
		elif i=="]":
			psy-=1
		if i==":" and psy==0:
			ls.append(tt)
			tt=""
		if i!=":":
			tt+=i
		if syc==len(id)-1:
			ls.append(tt)
		syc+=1
	başla=0
	son=0
	art=1
	if len(ls)==1:
		başla=i4işlem(parantez_çözücü(ls[0],{}))#bura
		if başla<0:
			başla+=ls_eleman_uzunluk(dz)
		return ls_eleman_elde(dz,[başla])
	elif len(ls)==2:
		if ls[0]=="":
			başla=0
		else:
			başla=i4işlem(parantez_çözücü(ls[0],{}))#bura
		if ls[1]=="":
			son=ls_eleman_uzunluk(dz)
		else:
			son=i4işlem(parantez_çözücü(ls[1],{}))#bura
			if son<0:
				son+=ls_eleman_uzunluk(dz)
		#print("işlenecek2",başla,son)
		if son>başla:
			döndür="["+ls_eleman_elde(dz,[başla])
		else:
			döndür="["
		başla+=1
		while başla<son:
			döndür+=","+ls_eleman_elde(dz,[başla])
			başla+=1
		döndür+="]"
		return döndür

#print(ls_altı_mini("[1,2,[3,6,9],4,5]","[0:3]"))
#print(ls_altı("[1,2,[3,6,9],4][2][1]"))


st="[5,6][0]+[1,[2,5,9][2],10][0]"

	
def parantez_çözücü32(dt1,dgler):
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
				stt1=değerle3(stt,dgler)
				for i in fnkler:
					tekrar_drm=tekrar_drm or i in dt1
				
				if lojik_mi(stt):
					degistir.append(("("+stt+")",int(lojik_çözücü(değerle3(stt,dgler)))))
				elif "[" in stt1 or "]" in stt1:
					#print("deneme",stt1)
					ikinci=index_çözücü(stt1)
					#print("deneme2",ikinci)
					if "[" in ikinci or "]" in ikinci:
						degistir.append(("("+stt+")",ls_islem(ikinci)))
					else:
						#print("hasssssss")
						degistir.append(("("+stt+")",i4işlem(ikinci)))
				else:
					degistir.append(("("+stt+")",i4işlem(değerle3(stt,dgler))))
					
			else:
				silinecek.append(i)
			drm=True
			stt=""
		for j,i in degistir:
			dt1=dt1.replace(j,str(i))
		for i in silinecek:
			tt.remove(i)
	return dt1
#st="[1,2,3,41,5,6,7,(7+2)*9][5+([10,0][0]-[2,3][0])/4]"

#print(parantez_çözücü(st,{}))
#idx=index_çözücü(st)
#print(i4işlem(parantez_çözücü(idx,{})))
#print(index_çözücü("[10,20,[1,2,3,5],20][[2,0][0]][-2]+5"))

#st="([1,2][(10-9):]+300)+(10*(([1,1]+[2,3])[0:3]*2)[2])"

#print("hassss",parantez_çözücü3(st,{}))


#st="[1,3+2,3,[4,[8,1]+[2]]*5+[2,5],10,[2,[2,20]+[1]*3,5],13]"
#ls_basitleyici(st)


#yeni
st="[1,[3,[5,[10,20]*3]*5+[17],7]+[1,2],4,5]"

def ifade_mi(st):
	ls=""
	psy=0
	bsl=False
	ara=""
	
	aralar=[]
	ifdlr=[]
	for i in st:
		if i=="[":
			if psy==0:
				bsl=True
				if ara!="":
					aralar.append(ara)
				ara=""
			psy+=1
		elif i=="]":
			psy-=1
			if psy==0:
				ls+=i
				ifdlr.append(ls)
				ls=""
				bsl=False
		if bsl:
			ls+=i
		elif i!="]" and psy==0:
			ara+=i
	if ara!="":
		aralar.append(ara)
	print(aralar)
	print(ifdlr)
	if len(ifdlr)>1:
		return True
	else:
		if "*" in "".join(aralar):
			return True
		else:
			return False
def ls_eleman_degistir(aa,id,degis):
	a=aa
	syc2=0
	bş,sn=0,0
	for e in id:
		tt=""
		drt=0
		basla=False
		syc=0
		kac=0
		ktmn=0
		ps=0
		if e<0:
			e+=ls_eleman_uzunluk(a)
		for i in a:
			if i=="[" and not basla:
				basla=True
			elif i=="[" and basla:
				tt=tt+i
				drt+=1
			elif i=="]" and drt==0:
				#print(tt,kac,"-",a[:syc])
				if kac==e:
					bş+=syc-len(tt)
					#print("loo",aa[:bş])
					a=tt
					if syc2==len(id)-1:
						sn=len(tt)
					break
			elif i=="]" and drt!=ps:
				tt+=i
				drt-=1
			elif i=="," and not drt!=0:
				#print(tt,"-",kac,"-",a[:syc-len(tt)])
				if kac==e:
					bş+=syc-len(tt)
					#print("loo",aa[:bş])
					a=tt
					if syc2==len(id)-1:
						sn=len(tt)
					break
				kac+=1
				tt=""
			elif i=="," and not drt==0:
				tt+=i
			else:
				tt+=i
			syc+=1
		syc2+=1
	return aa[:bş]+str(degis)+aa[bş+sn:]
st="[1,2,3,[8,[6,8,9],12,9,5],17]"
#print(ls_eleman_degistir(st,[3,4],"[10,20]"))

#print("________")



#print(ls_islem(index_çözücü(parantez_çözücü3("([1,3]+[7,6][:-1])*3+2*((2*[2,3]+[1])[3:]+[51])",{}))))
#print(ifade_mi(st))
#print(ls_basitleyici(parantez_çözücü3(st,{})))



	
def ls_basitleyici(st):
	
	gidilecek=[st]
	
	while gidilecek!=[]:
		gcc=[]
		#print("eses",gidilecek)
		değişecek=[]
		id=[]
		for e in gidilecek:
			tt=""
			drt=0
			basla=False
			syc=0
			for i in e:
				if i=="[" and not basla:
					basla=True
				elif i=="[" and basla:
					tt=tt+i
					drt+=1
				elif i=="]" and drt==0:
					print(tt)
					if "[" in tt or "]" in tt:
						print("deneme")
						sonuc=ls_islem(tt)
						değişecek.append((tt,sonuc))
						gcc.append(sonuc)
					elif lojik_mi(tt):
						pass
					else:
						pass
						#değişecek.append((tt,str(i4işlem(tt))))
				elif i=="]" and drt!=0:
					tt+=i
					drt-=1
				elif i=="," and not drt!=0:
					#print(tt)
					if "[" in tt or "]" in tt:
						#print("deneme")
						sonuc=ls_islem(tt)
						if (tt,sonuc) in değişecek:
							print("Cenkbb")
						else:
							değişecek.append((tt,sonuc))
							gcc.append(sonuc)
					elif lojik_mi(tt):
						pass
					else:
						#değişecek.append((tt,str(i4işlem(tt))))
						pass
					tt=""
				elif i=="," and not drt==0:
					tt+=i
				else:
					tt+=i
		#print("hass",gcc)
		for i,j in değişecek:
			#print("anan",i,j,"asd",st)
			st=st.replace(i,j)
			#print("ananhas",st)
		gidilecek=gcc
	print("son",st)
def index_çözücü2(st):
	bitti=True
	while bitti:
		syc=0
		ls=""
		iç_ls=[]
		psy=0
		onc=""
		goster=False
		alt=False
		altps=0
		değişecek=[]
		#print("anan",st)
		başı=0
		for i in st:
			if i=="[":
				if onc=="]":
					goster=True
					alt=True
					#print("hass",i)
					pass
				elif onc in "[,":
					pass
				else:
					if goster and psy<=altps:
						print("ooo1",st[başı:başı+len(ls)])
						değişecek.append((başı,ls))
						altps=psy
						alt=False
					
					ls=""
					goster=False
				if onc!="]":
					if alt:
						ls=""
						alt=False
						altps=psy
				psy+=1
			elif i=="]":
				psy-=1
				if psy==altps:
					ls+=i
					altps=psy
			
			if psy>altps:
				#print("anan",ls)
				if ls=="":
					başı=syc
				ls+=i
			
			if syc==len(st)-1:
				if goster and i!="":
					print("ooo",st[başı:başı+len(ls)],başı)
					değişecek.append((başı,ls))
			
			syc+=1
			onc=i
			
		#print("hass",st,değişecek)
		if değişecek==[]:
			#print(st)
			bitti=False
		else:
			#print("___",değişecek)
			fark=0
			for e,i in değişecek:
				st=st.replace(i,ls_altı(i))
				#dgcc=ls_altı(i)
#				st=st[:e+fark]+dgcc+st[e+fark+len(i):]
#				fark-=len(i)-len(dgcc)
			değişecek=[]
				
	return st


def parantez_çözücü3(dt1,dgler):
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
			başı=i
			for e in dt1[i+1:]:
				if e=="(":
					drm=False
					break
				elif e==")":
					break
				else:
					stt+=e
			if drm:
				#print("vavav",dt1[başı:başı+len(stt)+2],"¥",stt)
				kntrol=False
				stt1=değerle3(stt,dgler)
				for i in fnkler:
					tekrar_drm=tekrar_drm or i in dt1
				
				if lojik_mi(stt):
					degistir.append((başı,"("+stt+")",int(lojik_çözücü(değerle3(stt,dgler)))))
				elif "[" in stt1 or "]" in stt1:
					#print("deneme",stt1)
					ikinci=index_çözücü(stt1)
					#print("deneme2",ikinci)
					if "[" in ikinci or "]" in ikinci:
						degistir.append((başı,"("+stt+")",ls_islem(ikinci)))
					else:
						#print("hasssssss")
						degistir.append((başı,"("+stt+")",i4işlem(ikinci)))
				else:
					degistir.append((başı,"("+stt+")",i4işlem(değerle3(stt,dgler))))
					
			else:
				silinecek.append(i)
			drm=True
			stt=""
		fark=0
		#print("hass",degistir)
		for ı,j,i in degistir:
			#dt1=dt1.replace(j,str(i))
			#print("anan",i)
			#print("before",dt1,j,i,"has")
			dt1=dt1[:ı+fark]+str(i)+dt1[ı+fark+len(j):]
			#print("after",dt1)
			fark-=len(j)-len(str(i))
		degistir=[]
		for i in silinecek:
			tt.remove(i)
	return dt1
#print(parantez_çözücü3("10+((20-10)*(3-1+2)+10)*(2!=2)",{}))
#print(index_çözücü("[31,69][0+[1,1,0][-2]]+[1,2,3][[1,1][0]+[0,1][0]+1]+[20,30,35,50][[2,1,3,0][-2]]"))
def ls_basitleyici2(st):
	
	gidilecek=[(st,[])]
	
	while gidilecek!=[]:
		gcc=[]
		#print("eses",gidilecek)
		değişecek=[]
		#id=[[]]
		for e,id in gidilecek:
			tt=""
			drt=0
			basla=False
			syc=0
			for i in e:
				if i=="[" and not basla:
					basla=True
				elif i=="[" and basla:
					tt=tt+i
					drt+=1
				elif i=="]" and drt==0:
					#print("asd",tt,syc)
					if "[" in tt or "]" in tt:
						#print("önce",tt)
						sonuc=index_çözücü(tt)
						#print("sonra",sonuc)
						if "[" in sonuc or "]" in sonuc:
							#print("deneme")
							sonuc=ls_islem(sonuc)
							değişecek.append((id+[syc],sonuc))
							gcc.append((sonuc,id+[syc]))
						elif lojik_mi(sonuc):
							pass
						else:
							sonuc=str(i4işlem(parantez_çözücü3(sonuc,{})))
							
							değişecek.append((id+[syc],sonuc))
							gcc.append((sonuc,id+[syc]))
					elif lojik_mi(tt):
						pass
					else:
						sonuc=str(i4işlem(parantez_çözücü3(tt,{})))
						
						değişecek.append((id+[syc],sonuc))
						gcc.append((sonuc,id+[syc]))
						#değişecek.append((tt,str(i4işlem(tt))))
				elif i=="]" and drt!=0:
					tt+=i
					drt-=1
				elif i=="," and not drt!=0:
					#print(tt,syc)
					if "[" in tt or "]" in tt:
						#print("önce",tt)
						sonuc=index_çözücü(tt)
						#print("sonra",sonuc)
						if "[" in sonuc or "]" in sonuc:
							print("deneme")
							sonuc=ls_islem(sonuc)
							değişecek.append((id+[syc],sonuc))
							gcc.append((sonuc,id+[syc]))
						elif lojik_mi(sonuc):
							pass
						else:
							sonuc=str(i4işlem(parantez_çözücü3(sonuc,{})))
							
							değişecek.append((id+[syc],sonuc))
							gcc.append((sonuc,id+[syc]))
					elif lojik_mi(tt):
						pass
					else:
						sonuc=str(i4işlem(parantez_çözücü3(tt,{})))
						
						değişecek.append((id+[syc],sonuc))
						gcc.append((sonuc,id+[syc]))
						pass
					tt=""
					syc+=1
				elif i=="," and not drt==0:
					tt+=i
				else:
					tt+=i
		#print("hass",gcc)
		for i,j in değişecek:
			#print("anan",i,j,"asd",st)
			#print("___",i,j)
			st=ls_eleman_degistir(st,i,j)
			#print("ananhas",st)
		gidilecek=gcc
	print("son",st)


#print(parantez_çözücü3(st,{}))
#print(index_çözücü("[1,2,4,7,8][0:2]"))
#ls_basitleyici(parantez_çözücü3(st,{}))
#print([1,[[3,1]+[5],4,5][0]+[7]])

def ls_carp(st):
	#print("tt_knt",st)
	ls=""
	çs=""
	psy=0
	çbs=False
	syc=0
	çrp=1
	lss=[]
	kac=0
	for i in st:
		if i=="[":
			psy+=1
		elif i=="]":
			psy-=1
		elif i=="*" and psy==0:
			#print("bu",çs,psy)
			if "[" in çs or "]" in çs:
				ls=çs
			else:
				çrp*=float(çs)
			çs=""
			kac+=1
		elif i=="*" and psy!=0:
			çs+=i
		if i!="*":
			çs+=i
		if syc==len(st)-1:
			if "[" in çs or "]" in çs:
				ls=çs
			else:
				çrp*=float(çs)
			kac+=1
		syc+=1
	#print("ccc",ls,"-",çrp)
	if kac>1:
		if çrp==0:
			return "[]"
		else:
			return "["+(ls[1:-1]+",")*(int(çrp)-1)+ls[1:-1]+"]"
	else:
		return ls

def ls_islem(st):
	tt=""
	ls=0
	syc=0
	çd=False
	çpr=0
	çişr=False
	çzm=False
	snc=""
	for i in st:
		if i=="[":
			ls=ls+1
			tt+=i
		elif i=="]":
			tt+=i
			ls=ls-1
		elif i=="*":
			tt+=i
			çd=True
			if ls==0:
				çzm=True
		elif i=="(" and ls==0:
			çpr+=1
			tt+=i
		elif i==")" and ls==0:
			çpr=çpr-1
			tt+=i
		elif i=="+":
			if ls==0 and syc!=0 and çpr==0 and not çzm:
				#print("anan",tt)
				ttt=ls_carp(tt)
				if snc=="":
					snc=ttt
				else:
					#print("toplanan",snc,"ve",ttt)
					snc=snc[:-1]+","*int(snc!="[]" and ttt!="[]")+ttt[1:]
				tt=""
			else:
				tt+=i
		else:
			tt=tt+i
			if çzm:
				if i.isnumeric():
					çzm=False
					
		if syc==len(st)-1:
			#print("anan2",tt)
			ttt=ls_carp(tt)
			if snc=="":
				snc=ttt
			else:
				snc=snc[:-1]+","*int(snc!="[]" and ttt!="[]")+ttt[1:]
		syc+=1
	return snc
	


#st="[1,[[3,1]+[8]+[5],4,5][0]+[7],[10,[20,40,60]+[80,1]]+[30]]"

#st="[1,[20,[30,60,[90,9]+[10,5]]*3+[100,120]]+[4,5],90,71,[0,5,7]+[9,11],78]"

#st="[1,2,4,[6,7,[2,5,7]+[11,9]]*2+[1,1],[7,77]+[88]]"
#st="[1,[[3,1]+[5],4,5][0:2]+[7]]"
#st="[1,2,3,[10,20]==[10]+[10,[40,20]+[10]][1][1:2],78]"

#st="[1+[31,[3]+[2]][1][0],2,[[10,20]+[30],21,[1,2,3]+[7,8,10]]*2,90]"

#st="[1,[2,3,4][1:]*2,3][1]+[7]*2"
#print("___",st)
#print(ls_basitle(st)+"   işte")
#print("___karşılaştır___")
#print([1,[20,[30,60,[90,9]+[10,5]]*3+[100,120]]+[4,5],90,71,[0,5,7]+[9,11],78])

#print(ls_basitle("[1]*2+[2]*3"))


def index_çözücü2(st):
	bitti=True
	while bitti:
		syc=0
		ls=""
		iç_ls=[]
		psy=0
		onc=""
		goster=False
		alt=False
		altps=0
		değişecek=[]
		#print("anan",st)
		başı=0
		for i in st:
			if i=="[":
				if onc=="]":
					goster=True
					alt=True
					#print("hass",i)
					pass
				elif onc in "[,":
					pass
				else:
					if goster and psy<=altps:
						#print("ooo1",st[başı:başı+len(ls)])
						değişecek.append((başı,ls))
						altps=psy
						alt=False
					
					ls=""
					goster=False
				if onc!="]":
					if alt:
						ls=""
						alt=False
						altps=psy
				psy+=1
			elif i=="]":
				psy-=1
				if psy==altps:
					ls+=i
					altps=psy
			
			if psy>altps:
				#print("anan",ls)
				print("tt",ls)
				if ls=="":
					başı=syc
				ls+=i
			
			if syc==len(st)-1:
				if goster and i!="":
					#print("ooo",st[başı:başı+len(ls)],başı)
					değişecek.append((başı,ls))
			
			syc+=1
			onc=i
			
		print("hass",değişecek)
		if değişecek==[]:
			#print(st)
			bitti=False
		else:
			#print("___",değişecek)
			fark=0
			for e,i in değişecek:
				#st=st.replace(i,ls_altı(i))
				dgcc=ls_altı(i)
				print("gf",st)
				st=st[:e+fark]+dgcc+st[e+fark+len(i):]
				print("gf31",st)
				fark-=len(i)-len(dgcc)
			değişecek=[]
	return st
#print(index_çözücü2("[[1,2,3][1],2]"))

def index_çözücü(st):
	bitti=True
	while bitti:
		syc=0
		ls=""
		iç_ls=[]
		psy=0
		onc=""
		goster=False
		alt=False
		altps=0
		değişecek=[]
		#print("anan",st)
		başı=0
		has=""
		hasd=False
		sonps=0
		geriye=[]
		sonu=[]
		for i in st:
			if i=="[" and onc=="]" and not hasd:
				sonps=psy
				#print("nerde",syc,psy)
				geriye.append(syc)
				hasd=True
				
			#print(i,psy)
			#has durum
			if hasd and i=="," and psy==sonps:
				#print("virgül",has,psy)
				sonu.append(has)
				has=""
				hasd=False
			if hasd and i=="," and psy==sonps+1:
				#print("virgül",has,psy)
				has=""
				hasd=False
			if hasd and i=="[":
				pass
			elif hasd and i!="[" and psy==sonps:
				#print("dene1",has)
				sonu.append(has)
				has=""
				hasd=False
			if hasd and i=="[" and onc=="]" and psy==sonps+1:
				geriye=geriye[:-1]
				#print("nerde",syc,psy)
				#sonu.append(has)
				geriye.append(syc)
				hasd=True
				sonps=psy
				has=""
			if hasd and i=="]" and psy==sonps:
				#print(has,"eben")
				sonu.append(has)
				has=""
			if hasd:
				has+=i
			if hasd and syc==len(st)-1:
				#print("dene son",has)
				sonu.append(has)
			if i=="[":
				psy+=1
			if i=="]":
				psy-=1
			onc=i
			syc+=1
		#print("hadi aw",geriye,sonu)
		psy=0
		syc-=1
		syc1=len(geriye)
		gh=""
		ekle=False
		sonps=0
		ifadeler=[]
		while syc>=0:
			i=st[syc]
			if i=="[":
				psy-=1
			if i=="]":
				psy+=1
			if syc+1 in geriye:
				ekle=True
				gh=""
				sonps=psy
				syc1-=1
			if ekle and sonps<=psy:
				gh=i+gh
			if ekle and sonps>psy:
				gh=i+gh
				#print("ğğ",gh,syc1)
				başl=geriye[syc1]-len(gh)
				sonl=geriye[syc1]+len(sonu[syc1])
				ifadeler.append((gh+sonu[syc1],başl,sonl))
				
#				print("deneme",st[başl:sonl])
				gh=""
				ekle=False
			#print("ch",gh)
			#print(i,sonps,psy,syc)
			
			syc-=1
		#print(st)
		#print("yapma yaw",ifadeler)
		if ifadeler==[]:
			bitti=False
		gerile=0
		for i,b,s in ifadeler:
			st=st[:b]+ls_altı(i)+st[s:]
			gerile+=len(ls_altı(i))-len(i)
	return st
#print(index_çözücü("[[[2,4,6][[-1,-1,-1-1][2]],10][0],1,1,11]"))
#print(ls_basitle(parantez_çözücü4("[([([1]*4+[2]*3)[1:-2][-1],40,45])[-1]==45]+[10]*5",{})))

def parantez_çözücü4(dt1,dgler):
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
			başı=i
			for e in dt1[i+1:]:
				if e=="(":
					drm=False
					break
				elif e==")":
					break
				else:
					stt+=e
			if drm:
				#print("vavav",dt1[başı:başı+len(stt)+2],"¥",stt)
				#print("hhhhh",stt)
				kntrol=False
				stt1=değerle3(stt,dgler)
				for i in fnkler:
					tekrar_drm=tekrar_drm or i in dt1
				if lojik_mi(stt) and ("[" in stt1 or "]" in stt1):
					#print("dayın31",stt1)
					ikinci=index_çözücü(stt1)
					#print("deneme2",ikinci)
					if "[" in ikinci or "]" in ikinci:
						#print("anan",ls_basitle(ikinci))
						üçüncü=ls_basitle(ikinci)
						degistir.append((başı,"("+stt+")",int(lojik_çözücü(değerle3(üçüncü,dgler)))))
					else:
						#print("hasssssss")
						degistir.append((başı,"("+stt+")",int(lojik_çözücü(değerle3(ikinci,dgler)))))
				elif lojik_mi(stt):
					degistir.append((başı,"("+stt+")",int(lojik_çözücü(değerle3(stt,dgler)))))
				elif "[" in stt1 or "]" in stt1:
					#print("deneme",stt1)
					#print("dayın",stt1)
					ikinci=index_çözücü(stt1)
					#print("deneme2",ikinci)
					if "[" in ikinci or "]" in ikinci:
						#print("anan",ls_basitle(ikinci))
						degistir.append((başı,"("+stt+")",ls_basitle(ikinci)))
					else:
						#print("hasssssss")
						degistir.append((başı,"("+stt+")",i4işlem(ikinci)))
				else:
					degistir.append((başı,"("+stt+")",i4işlem(değerle3(stt,dgler))))
					
			else:
				silinecek.append(i)
			drm=True
			stt=""
		fark=0
		#print("hass",degistir)
		for ı,j,i in degistir:
			#dt1=dt1.replace(j,str(i))
			#print("anan",i)
			#print("before",dt1,j,i,"has")
			dt1=dt1[:ı+fark]+str(i)+dt1[ı+fark+len(j):]
			#print("after",dt1)
			fark-=len(j)-len(str(i))
		degistir=[]
		for i in silinecek:
			tt.remove(i)
	return dt1

def ifade_öncesi_bul(st, syc):
	syc2 = syc - 1
	eklenecek = ""
	while syc2 > -1 and st[syc2] not in ",[":
		eklenecek = st[syc2] + eklenecek
		syc2 -= 1
	return eklenecek



def lojik_liste_ayırıcı(st):
	#print("looo",st)
	syc=0
	psy=0
	tt=[]
	stt=""
	ekd=False
	for i in st:
		if i=="[":
			psy+=1
		if i=="]":
			psy-=1
		if psy==0 and i in "=<> veya":
			if stt!="":
				if "[" in stt or "]" in stt:
					tt.append(stt)
			stt=""
		elif psy!=0 and i in "=<> veya":
			stt+=i
		else:
			stt+=i
	if "[" in stt or "]" in stt:
		tt.append(stt)
	
	#print("loooo2",tt)
	return tt
#print(ls_basitle(parantez_çözücü4("[1,([0]*4)[1:]+[1]==[0,0,1],2]+[4]*2==[1,2,4] ve [9,99]==[9,99]",{})))

#print(lojik_çözücü(parantez_çözücü4("1+1<(3-2)*4",{})))

def gerekli_float(sy):
	if sy%1==0:
		return int(sy)
	return sy

def liste_içi_işlem(st):
	#print("liste içi",st)
	hes=""
	başl=False
	syc=0
	degisecek=[]
	for i in st:
		if i in "[],:":
			if hes!="" and (işlem_mi(hes) or lojik_mi(hes)):
				#print("has",hes)#syc,st[syc-len(hes):syc])
				degisecek.append([hes,syc])
			başl=True
			if i=="]":
				başl=False
			hes=""
		if başl and i not in "],[:":
			hes+=i
		syc+=1
	fark=0
	#print("başında",st,)
	for dz,i in degisecek:
		dgs=""
		if lojik_mi(dz):
			dgs=str(int(lojik_çözücü(dz)))
		elif işlem_mi(dz):
			dgs=str(gerekli_float(i4işlem(dz)))
		st=st[:i-len(dz)+fark]+dgs+st[i+fark:]
		#print(":",dz,dgs)
		fark+=len(dgs)-len(dz)
	#print("sonunda",st)
	return st

def listeli_ifade_çözücü(stt):
	#print("deneme listeli",stt)
	dnd=""
	if "[" in stt or "]" in stt:
		#print("lojik ls",stt)
		dnd=ls_basitle(parantez_çözücü4(stt,{}))
		#print("hasss",dnd)
	#elif ("[" in stt or "]") in stt and lojik_mi(stt):
#		return lojik_çözücü(stt)
	elif lojik_mi(stt):
		return lojik_çözücü(stt)
	else:
		dnd=parantez_çözücü4(stt,{})
	#print(dnd)
	if "[" in dnd or "]" in dnd:
		return dnd
	elif lojik_mi(dnd):
		#print("ahan da lojik",dnd)
		return lojik_çözücü(dnd)
	else:
		return i4işlem(dnd)
def ls_basitle(st):
	ifd=""
	psy=0
	psls=[]
	syc=0
	ifdls=[]
	hng=[]
	hsy=0
	syc=0
	for i in st:
		if i=="[":
			if ifdls==[]:
				eklenecek_ifade=ifade_öncesi_bul(st, syc)
				ifdls.append(eklenecek_ifade)
				hng.append((hsy,psy))
				hsy+=1
			else:
				#print("stt",hng,psy)
				if hng[-1][1]<psy:
					eklenecek_ifade=eklenecek_ifade=ifade_öncesi_bul(st, syc)
					ifdls.append(eklenecek_ifade)
					hng.append((hsy,psy))
					hsy+=1
			psy+=1
		elif i=="]":
			#print(hng,psy,ifdls[0])
			#print(psy,hng[-1])
			#print(psy,hng[-1])
			#if hng[-1][1]==psy:
			psy-=1
			if hng[-1][1]>psy:
				#ifdls[hng[-1][0]]+=i
				hng=hng[:-1]
		elif i==" ":
			pass
		elif i==":":
			#print("hass",psy,hng[-1],ifdls[0])
			if hng!=[]:
				if hng[-1][1]==psy:
					#ifdls[hng[-1][0]]+=i
					hng=hng[:-1]
		elif i==",":
			#print("hass",psy,hng[-1],ifdls[0])
			if hng!=[]:
				if hng[-1][1]==psy:
					#ifdls[hng[-1][0]]+=i
					hng=hng[:-1]
		if i in "+-*":
			#print("hassssss",syc,psy,ifdls)
			psls.append((syc,psy))
		for e,j in hng:
			ifdls[e]+=i
		syc+=1
	#print("ifdls",ifdls)
		
	#son lojik ifadeli parçalma
	syc=0
	fark=0
	#print("^^^^^",ifdls)
	#print("deneme",ifdls)
#	print("baş",st)
	#print("wwww",ifdls)
	for i in ifdls:
		if lojik_mi(i):
			eklenelj=lojik_liste_ayırıcı(i)
			#print("hadi baba vol",eklenelj)
			ifdls=ifdls[:syc+fark]+[i]+eklenelj+ifdls[syc+1+fark:]
			fark+=len(eklenelj)
		syc+=1
	#print("qqqq",ifdls)
	#print("deneme",ifdls)
#	print("son",st)
	#print("₺₺₺₺₺",ifdls)
	syc=len(ifdls)-1
	#print("neeeeden",ifdls)
	
	for i in range(len(ifdls)):
		ii=ifdls[syc]
		dgs=liste_içi_işlem(ii)
		dgs=index_çözücü(dgs)
		if ("[" in dgs or "]" in dgs) and not lojik_mi(dgs):
			dgs=ls_islem(dgs)
		elif lojik_mi(dgs):
			#print("haaaaadii",dgs)
			dgs=str(int(lojik_çözücü(dgs)))
		elif işlem_mi(dgs):
			#print("4 işlemlemek lazım")
			pass
			#print("noldu",dgs,ii)
		st=st.replace(ii,dgs)
		#print("asas",st,"hass",ii,"neyi",dgs)
#		print("___________")
		syc1=syc
		if syc>0:
			if ii in ifdls[syc-1]:
				#print("neeee")
				ifdls[syc-1]=ifdls[syc-1].replace(ii,dgs)
		syc1-=2
		#krldı_mı=False
		while syc1>=0:
			#print("anannı",ifdls[syc1],"sonu")
			if ii in ifdls[syc1]:
				ifdls[syc1]=ifdls[syc1].replace(ii,dgs)
			syc1-=1
	
		syc-=1
	#print("wwwww",ifdls,st)
	
	#print("son",st)
	return st
	#return ifdls

#st="[1,(4==2+2 veya 3>2+2)+20,5][0:6/2]*2+[11,[([22]+[50/2+1]==[23-1,25][0:[1,4/2,3][1]])+100]+[25],33]"
#print("dayııııığğ",listeli_ifade_çözücü(st))
#st="[10,20,[2,4,6][1]+10,34][:3+1]+[200]+[20==[30,10,40][0]+-10]"
#print("dayııııığğ",listeli_ifade_çözücü(st))

#print(parantez_çözücü4("topla(20,30)+10",{}))

#st="[10,20,30][([2,5,13]+[10])[0-(1==0+1)]-9+1]==[30,40][1]-10"
#print("dayııııığğ",listeli_ifade_çözücü(st))

#st="[31,69][20-10>[10,20,30][1-1]-1 ve 2==2 ve [2,5]==[2]+[5]]+[100,[200,400][1],350][1]"
#print("dayııııığğ",listeli_ifade_çözücü(st))

#st="[1,2,3]==[1,2]+[3]"
#print("dayııııığğ",listeli_ifade_çözücü(st))


#st="[5,10,20][[1,2,3]==[1,2]+[3] ve [5]*2==[5,5]]"
#print("dayııııığğ",listeli_ifade_çözücü(st))

#st="([2]*2+[3]+[2]*2)[1:5][1]+100"
#print("dayııııığğ",listeli_ifade_çözücü(st))

#st="40>[31,69][1]"
#print("dayııııığğ",listeli_ifade_çözücü(st))

#st="100+[10,20,30,40,50][[1,[2,3],10][1][1]+[8,10][1]-9]"
#print("dayııııığğ31",listeli_ifade_çözücü(st))

#print(liste_içi_işlem(st))



#print(listeli_ifade_çözücü("[20,30][[1,2,3][10]]"))