import random
ob= "("
cb= ")"
numcentral = "x"
posi = ["Na","L","K","Mg","Ca","Be"," "]
numposi = [" ","2","3"]
numpos = random.choice(numposi)
counter = random.choice(posi)
if counter == " ":
    cation = (counter)
else :
    cation =(f"{counter}{numpos}")
metal = ["Fe","Co","Zn","Ni","Cu","Mn","Pt"]
central = (random.choice(metal))
nega = ["SO4","F","Cl","Br","I","S","O","NO2","NO3","ONO","OH","PO4","CO3"," "]
numnega = [" ","2","3"]
numnegative = random.choice(numnega)
neg = random.choice(nega)
if neg == " ":
    anion = (neg)
else :
    anion = (f"{ob}{neg}{cb}{numnegative}")
lign = ["Cl","Br","I","F","CN","NO2","ONO","OH","SO4","C2O4","O2","NH2","NO3","CO3","NH","EDTA"]
numlign = [" ","2","3","4"]
numligandn1 = random.choice(numlign)
numligandn2 = random.choice(numlign)
numligandn3 = random.choice(numlign)
neglig1 = random.choice(lign)
neglig2 = random.choice(lign)
neglig3 = random.choice(lign)
nlig = ["NH3","CO","NO","H2O","CS","en"]
numnlig = [" ","2","3","4"]
numnligand1 = random.choice(numnlig)
numnligand2 =  random.choice(numnlig)
numnligand3 =  random.choice(numnlig)
neulig1 = random.choice(nlig)
neulig2 = random.choice(nlig)
neulig3 = random.choice(nlig)
ligand10 = (f"{ob}{neulig1}{cb}{numnligand1}")
ligand20 = (f"{ob}{neulig1}{cb}{numnligand1}{ob}{neulig2}{cb}{numnligand2}")
ligand30 = (f"{ob}{neulig1}{cb}{numnligand1}{ob}{neulig2}{cb}{numnligand2}{ob}{neulig3}{cb}{numnligand3}")
ligand01 = (f"{ob}{neglig1}{cb}{numligandn1}")
ligand02 = (f"{ob}{neglig1}{cb}{numligandn1}{ob}{neglig2}{cb}{numligandn2}")
ligand03 = (f"{ob}{neglig1}{cb}{numligandn1}{ob}{neglig2}{cb}{numligandn2}{ob}{neglig3}{cb}{numligandn3}")
ligand11 = (f"{ob}{neulig1}{cb}{numnligand1}{ob}{neglig1}{cb}{numligandn1}")
ligand12 = (f"{ob}{neulig1}{cb}{numnligand1}{ob}{neulig2}{cb}{numnligand2}{ob}{neglig1}{cb}{numligandn1}")
ligand21 = (f"{ob}{neulig1}{cb}{numnligand1}{ob}{neglig1}{cb}{numligandn1}{ob}{neglig2}{cb}{numligandn2}")
mainligand = (ligand01,ligand02,ligand03,ligand10,ligand20,ligand30,ligand11,ligand12,ligand21)
choseligand = random.choice(mainligand)
obra = "["
cbra = "]"

print(f"{cation}{obra}{central}{numcentral}{choseligand}{cbra}{anion}")

