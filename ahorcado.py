#Juego de ahorcado
print("*** BIENVENIDO AL JUEGO DE AHORCADO ***")
Palabra=input("Digite una palabra: ").upper()
Palabra=list(Palabra)
Vidas=5
Acerto=False

def isLetra():
    while True:
        try:
            Letra = input("\n\n Ingrese una letra: ")
            if len(Letra) == 1 and Letra.isalpha():
                print("Ingreso válido.")
                break
            else:
                print("\nSe detectó más de una letra o caracteres no alfabéticos.")
        except ValueError:
            None
    return Letra
    
Letra=''

for i in range(5):
    for j in range(len(Palabra)):
        Letra=isLetra()