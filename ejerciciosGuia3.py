#N°3

X=int(input("Ingrese el ángulo 1: "))
Y=int(input("Ingrese el ángulo 2: "))
Z=180-(X+Y)
if X==90 or Y==90 or Z==90:
    print("Es un triángulo rectángulo")
elif X<90 and Y<90 and Z<90:
    print("Es un triángulo acutángulo")
elif X>90 or Y>90 or Z>90:
    print("Es un triángulo obtusángulo")