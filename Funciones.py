from colorama import Fore

def sumar_fila(matriz, fila):
    suma = 0
    for i in range(len(matriz[fila])):
        suma += matriz[fila][i]
    return suma

def sumar_columna(matriz, columna):
    suma = 0
    for i in range(len(matriz)):
        suma += matriz[i][columna]
    return suma

def sumar_diagonal_principal(matriz):
    suma = 0
    for i in range(len(matriz)):
        suma += matriz[i][i]
    return suma

def sumar_diagonal_secundaria(matriz):
    suma = 0
    for i in range(len(matriz)):
        suma += matriz[i][len(matriz) -1 -i]
    return suma

def recorrer_filas(matriz, constante_magica):
    for i in range(len(matriz)):
        if sumar_fila(matriz, i) != constante_magica:        
            return False

def recorrer_columnas(matriz, constante_magica):
    for j in range(len(matriz)):
        if sumar_columna(matriz, j) != constante_magica:
            return False

def es_magico(matriz):
    n = len(matriz)
    constante_magica = n * (n ** 2 + 1) // 2
    
    bandera = True
    if recorrer_filas(matriz, constante_magica) == False:
        bandera = False
    if recorrer_columnas(matriz, constante_magica) == False:
        bandera = False
    if sumar_diagonal_principal(matriz) != constante_magica:
        bandera = False        
    if sumar_diagonal_secundaria(matriz) != constante_magica:
        bandera = False
    
    return bandera

# ==================================================================

def mostrar_martiz(matriz):
    for i in range(len(matriz)):        # Filas
        for j in range(len(matriz[i])): # Columnas
            # print(f"{matriz[i][j]:<8}", end = "")
            if matriz[i][j] != None:
                print(matriz[i][j], end = "\t\t")
            else:
                print("X", end = "\t\t")
        print("")

def crear_matriz_vacia(cantidad_filas: int, cantidad_columnas: int, valor_inicial: any) -> list:
    matriz_creada = []
    for i in range(cantidad_filas):
        fila = [] # [0,0,0,0]
        for j in range(cantidad_columnas):
            fila.append(valor_inicial)
        matriz_creada.append(fila)

    return matriz_creada

def cargar_matriz(matriz: list):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            numero = int(input(f"Ingrese un numero [{i + 1},{j + 1}]: "))
            matriz[i][j] = numero

# ==================================================================

def pedir_entero(mensaje: str, minimo: int, maximo: int, mensaje_error: str) -> int:
    while True:
        valor = int(input(f"{mensaje} [{minimo}-{maximo}]: "))

        if valor >= minimo and valor <= maximo:
            return valor

        print(Fore.RED + mensaje_error + Fore.RESET)


def pedir_str(mensaje: str) -> str:
    while True:
        texto = input(f"{mensaje}")

        if texto != "":
            return texto

        print("Error. No puede estar vacio.")
