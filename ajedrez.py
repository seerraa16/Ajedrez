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
        fila = int(input("fila: "))
        print("ingrese la columna")
        columna = int(input("columna: "))
   

    

           


    

           




