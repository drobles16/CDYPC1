suma=0
n=int(input("¿Alturas a introducir?"))
for x in range(n):
    altura=float(input("Introduce una altura:"))
    suma=suma+altura
media=suma/n
print("La altura media es ",media)
                 
