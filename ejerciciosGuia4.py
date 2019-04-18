#N°4

Nombre=input("Ingrese el nombre del clavadista: ")
D=float(input("Ingrese la dificultad del clavado: "))
Jueces=7
X=0
i=0
L=0
puntajes=[]
for i in range(0,Jueces):
    X=float(input("Ingrese puntaje del juez: "))
    X=X+L
    puntajes.append(X)
    if L==0:
        L=1/2
puntajes.sort()

puntajes.pop(-1)

puntajes.pop(0)

R=(puntajes[0]+puntajes[1]+puntajes[2]+puntajes[3]+puntajes[4])*(3/5)
R=R*D
print("El puntaje del clavadista es: ",R)