def validar_orden(matriz):
    bandera = True
    for i in range(len(matriz)):
        if len(matriz[i]) != len(matriz):
            bandera = False
    return bandera


def validar_valores(matriz):
    bandera = True
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if matriz[i][j] < 1 or matriz[i][j] > len(matriz) ** 2:
                bandera = False
    return bandera


def validar_repetidos(matriz):
    repetidos = []
    bandera = True

    for i in range(len(matriz)):
        for j in range(len(matriz)):
            for k in range(len(repetidos)):
                if repetidos[k] == matriz[i][j]:
                    bandera = False

            repetidos.append(matriz[i][j])

    return bandera



def validar_matriz(matriz):
    bandera = True

    if validar_orden(matriz) == False:
        bandera = False
    if validar_valores(matriz) == False:
        bandera = False
    if validar_repetidos(matriz) == False:
        bandera = False

    return bandera



# def validar_matriz(matriz):
#     bandera = True
#     if validar_orden(matriz) == False:
#         bandera = False
#         print("Error:  ")
#         print("La bandera no tiene un orden cuadrado")
#     if validar_valores(matriz) == False:
#         bandera = False
#         print("Error:  ")
#         print("Valores ingresados incorrectos. ")
#     if validar_repetidos(matriz) == False:
#         bandera = False
#         print("Error:  ")
#         print("Hay numero repetidos")



# def validar_repetidos(matriz):
#     bandera = True
#     repetidos = []
#     for i in range(len(matriz)):
#         for j in range(len(matriz)):
#             encontrados = False
#             for k in range(len(repetidos)):
#                 if repetidos(k) == matriz[i][j]:
#                     encontrados = True
#             if encontrados == True:
#                 bandera == False
#             else:
#                 repetidos.append
#     return bandera