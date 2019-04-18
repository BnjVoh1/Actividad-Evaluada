#N°2

print("Este edificio cuenta con 20 pisos")
A=int(input("Ingrese el numero de departamento: "))
Y=int(A/100)
X=int(((A/100)-Y)*100)
if(X==205,305,405,505,605,705,805,905,1105,1205,1305,1405,1505,1605,1705,1805,1905):
    X=X+1
    
B=250

if(Y==1):
    print("El precio del departamento es de: $ 100")
elif(Y==20):
    print("El precio del departamento es de: $ 400")
else:
    if(X==7 or X==3):
        print("El precio de este departamento es de: $",(250*1.15))
    elif(X==4 or X==0):
        print("El precio de este departamento es de: $",(B*0.8))
    else:
        print("El precio de este departamento es de: $",B)