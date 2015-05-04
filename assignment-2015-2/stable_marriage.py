import sys
import json
from collections import OrderedDict
args = str(sys.argv)
synolo = len(sys.argv)
f = open(str(sys.argv[2]) , 'r')
j = json.load(f)
f.close()
#apothikevoume tis protimiseis antrwn arxika kai gynaikwn sti synexeia
protimiseisantrwn = j[protimiseis_antrwn]
protimiseisgynaikwn = j[protimiseis_gynaikwn]
antres = sorted(protimiseisantrwn.keys())
gynaikes = sorted(protimiseisgynaikwn.keys())
if str(sys.argv[1]) == -m : 
 def tairiasma():
     eleftheroi = antres[:]
	 desmeumenoi = {}
	 while eleftheroi:
	  antras = eleftheroi.pop(0)
	  onomataantrwn = protimiseisantrwn[antras]
	  gynaika = onomataantrwn.pop(0)
	  nyngynaika = desmeumenoi.get(gynaika)
	  if not nyngynaika:
         desmeumenoi[gynaika] = antras
      else:
         onomatagynaikwn = protimiseisgynaikwn[gynaika]
         if onomatagynaikwn.index(nyngynaika) > onomatagynaikwn.index(antras):
             desmeumenoi[gynaika]=antras		   
             if protimiseisantrwn[nyngynaika]:
				eleftheroi.append(nyngynaika)
		 else:
             if onomataantrwn:
				eleftheroi.append(antras)
	 return desmeumenoi
 if synolo == 3:
     f = open('stable_marriage.json', 'w')
     json.dump(stable_marriage, f)
     f.close()	 
 if synolo == 5:
      outputfile = open(str(sys.argv[4])) , 'w')
	  apotelesma.write(desmeumenoi)
	  apotelesma.close()
#kaname ti lysi gia tous antres kai sti synexeia ginetai to idio gia tis gynaikes
 else:
    def tairiasma():
     eleftheres = gynaikes[:]
	 desmeumenoi = {}
	 while eleftheres:
	  gynaika = eleftheres.pop(0)
	  onomatagynaikwn = protimiseisgynaikwn[gynaika]
	  antras = onomatagynaikwn.pop(0)
	  nyngynaika = desmeumenoi.get(antras)
	  if not nyngynaika:
         desmeumenoi[antras] = gynaika
      else:
         onomataantrwn = protimiseisantrwn[antras]
         if onomataantrwn.index(nyngynaika) > onomataantrwn.index(gynaika):
             desmeumenoi[antras]=gynaika		   
             if protimiseisgynaikwn[nyngynaika]:
			    eleftheres.append(nyngynaika)
		 else:
             if onomatagynaikwn:
                 eleftheres.append(gynaika)
	 return desmeumenoi

    if synolo == 4:
      f = open('stable_marriage.json', 'w')
      json.dump(stable_marriage, f)
      f.close()
	
    if synolo == 6:		
	  outputfile = open(str(sys.argv[5])) , 'w')
	  apotelesma.write(desmeumenoi)
	  apotelesma.close()
	  
	  

		
	 
	 