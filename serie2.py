#quitar los signos iguales de más
mail = input("Ingrese un mail:")
cantidad = 0
x= 0

while x < len(mail):
    if mail[x] == "@" or mail[x] == "@":
        cantidad = cantidad + 1
    x = x + 1 #el cambio fue quitarle un signo +

if cantidad == 1:
    print("El mail ingresado contiene solo un caracter '@'")
else:
    print("Incorrecto") #le hacia falta cerrar las comillas
