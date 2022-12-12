

tablero = [[ "♜",   "♞",   "♝",   "♛",   "♚",   "♝",   "♞",  "♜"], #fchas negras
            ["♟",   "♟",   "♟",   "♟",   "♟",   "♟",   "♟",  "♟"],
            [" ",    " ",    " ",    " ",    " ",    " ",    " ",    " "],
            [" ",    " ",   " ",     " ",    " ",    " ",    " ",    " "],
            [" ",    " ",   " ",    " ",     " ",   " ",    " ",    " "],
            [" ",    " ",   " ",    " ",    " ",    " ",     " ",    " "],
            ["♙",   "♙",   "♙",   "♙",  "♙",   "♙",    "♙",  "♙"],
            ["♖",   "♘",   "♗",  "♕",   "♔",    "♗",    "♘",   "♖"]] #fichas blancas

def imprimir_tablero(tablero):      
    print("  a b c d e f g h")
    for i in range(8): #filas
        print(i+1, end=" ")
        for j in range(8): #columnas
            print(tablero[i][j], end=" ")
        print(i+1)
print(imprimir_tablero(tablero)) #mostrar tablero en pantalla
def movimiento(tablero):
    print("¿quiere hacer un movimiento?")
    respuesta = input("si/no: ")
    if respuesta == "si":
        print("ingrese la posicion de la ficha que desea mover")
        print("ingrese la fila")
        fila = int(input("fila: ")) #fila de la ficha a mover
        print("ingrese la columna")
        columna = int(input("columna: ")) #columna de la ficha a mover
        print("ingrese la posicion a la que desea mover la ficha")
        print("ingrese la fila")
        fila2 = int(input("fila: ")) #fila donde queremos que vaya la ficha 
        print("ingrese la columna")
        columna2 = int(input("columna: ")) #columna donde queremos que vaya la ficha
        tablero[fila2][columna2] = tablero[fila][columna] #movimiento de la ficha que hemos elegido
        tablero[fila][columna] = " " #al mover la ficha la posicion anterior se queda vacia
        print(imprimir_tablero(tablero)) #mostramos en pantalla los cambios
        
    else:
        print("Esa no es una respuesta valida")
print(movimiento(tablero))
while True: #bucle para hacer infinitos movimientos
    print("¿quiere hacer un movimiento?")
    respuesta = input("si/no: ")
    if respuesta == "si":
        print("ingrese la posicion de la ficha que desea mover")
        print("ingrese la fila")
        fila = int(input("fila: ")) 
        print("ingrese la columna")
        columna = int(input("columna: "))
        print("ingrese la posicion a la que desea mover la ficha")
        print("ingrese la fila")
        fila2 = int(input("fila: "))
        print("ingrese la columna")
        columna2 = int(input("columna: "))
        tablero[fila2][columna2] = tablero[fila][columna]
        tablero[fila][columna] = " "
        print(imprimir_tablero(tablero))
        
    elif respuesta == "no":
        print("Gracias por jugar")
        break
    #fin