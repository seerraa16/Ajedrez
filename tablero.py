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
    for i in range(8):
        print(i+1, end=" ")
        for j in range(8):
            print(tablero[i][j], end=" ")
        print(i+1)





