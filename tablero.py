def tablero ():
    piezas = [["torre",    "caballo",     "alfil",    "reina",    "rey",     "alfil",    "caballo",  "torre"],
              ["peon",      "peon",         "peon",     "peon",     "peon",     "peon",     "peon",     "peon"],
                ["",          "",             "",         "",         "",         "",         "",         ""],
                ["",          "",             "",         "",         "",         "",         "",         ""],
                ["",          "",             "",         "",         "",         "",         "",         ""],
                ["",          "",             "",         "",         "",         "",         "",         ""],
                ["peon",      "peon",         "peon",     "peon",     "peon",     "peon",     "peon",     "peon"],
                ["torre",    "caballo",     "alfil",    "reina",    "rey",     "alfil",    "caballo",  "torre"]]
    for i in range(8):
        print(piezas[i])
tablero()

