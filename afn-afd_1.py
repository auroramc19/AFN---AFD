from itertools import chain, combinations

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(
        combinations(s,r)
        for r in range(len(s)+1))

#print(list(poerset(['q0', 'q1', 'q2'])))

Q = ['q0','q1']
Sigma = ['a','b']
s = 'q0'
F = ['q1']
DELTA = {
        ('q0','a'): ['q0','q1'],
        ('q0','b'): ['q1'],
        ('q1','b'): ['q0','q1']
        }

Qprima = list(powerset(Q))
sprima = (s,)
Sigmaprima = Sigma
Fprima = []

for q in Qprima:
    for x in q:
        if x in F:
            Fprima.append(q)

Dprima = {}
for q in Qprima:
    for x in Sigmaprima:
        d = []
        for y in q:
            if (y,x) in DELTA.keys():
                for r in DELTA[(y,x)]:
                    if r not in d:
                        d.append(r)
        d.sort()
        Dprima[(q,x)] = tuple(d)


                        
print(Dprima)
print("Qprima", Qprima)
print("Sigmaprima", Sigmaprima)
print("sprima", sprima)
print("Fprima", Fprima)


Ejemplos_L=['a','b','aa','ab','bb','bba']
Ejemplos_Lc=['','ba','baa','bab']


def transicion(estado,Sigmaprima):
    #print("estado=",estado,"sigma=",Sigmaprima)
    estado_siguiente = Dprima[(tuple(estado),Sigmaprima)]
    #print("estado_siguiente=",tuple(estado_siguiente))
    return tuple(estado_siguiente)

for w in Ejemplos_L:
    estado = sprima
    for Sigmaprima in w: #para cada simblo de la cadena
        estado=transicion(estado,Sigmaprima)

    if estado in Fprima:
        print(w,"es aceptada")
    else:
        print(w, "no es aceptada")

for w in Ejemplos_Lc:
    estado = sprima
    for Sigmaprima in w: #para cada simblo de la cadena
        estado=transicion(estado,Sigmaprima)

    if estado in Fprima:
        print(w,"es aceptada")
    else:
        print(w, "no es aceptada")


