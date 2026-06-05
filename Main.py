from Validacion import *
from Funciones import *
from colorama import Fore


matriz_magica = [[2,9,4],
                 [7,5,3],
                 [6,1,8]]

matriz_normal = [[5,8,4],
                 [7,2,6],
                 [3,1,9]]

matriz_repetida = [[5,8,4],
                   [7,2,6],
                   [8,1,9]]


def main():
    n = pedir_entero("Ingrese el orden de filas de la matriz" , 1, 32, "Orden invalido. Ingrese el orden nuevamente: ")
    m = pedir_entero("Ingrese el orden de columnas de la matriz" , 1, 32, "Orden invalido. Ingrese el orden nuevamente: ")


    matriz = crear_matriz_vacia(n, m, None)
    mostrar_martiz(matriz)

    cargar_matriz(matriz)
    mostrar_martiz(matriz)

    if validar_matriz(matriz) == True:
        if es_magico(matriz) == True:
            print("La matriz es un cuadrado magico.")
        else:
            print("La matriz no es un cuadrado magico.")
    elif validar_matriz(matriz) == False:
        print("La matriz no tiene un orden cuadrado, tiene numeros repetidos o los valores ingresados son incorrectos.")

if __name__ == "__main__":
    main()