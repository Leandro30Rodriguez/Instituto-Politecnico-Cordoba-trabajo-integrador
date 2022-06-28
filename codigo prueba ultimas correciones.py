def funcion_ingresar_datos():
    List_Number = []
    for numbers in range (5):
        numbers_add = int(input("Ingrese un numero:"))
        List_Number.append (numbers_add)
    return List_Number

def funcion_promedio(List_number):
    avg = 0
    for numbers in range (5):
        avg += List_number[numbers]
    avg /= 5
    avg = int(avg)
    return avg

def funcion_suma(List_number):
    suma = 0
    for numbers in range (5):
        suma += List_number [numbers]
    return suma

def funcion_maximo(List_number):
    maximo = List_number[0]
    for x in List_number:
        if x > maximo :
            maximo = x 
    return maximo 

lista = funcion_ingresar_datos()

promedio = funcion_promedio(lista)
suma = funcion_suma(lista)
maximo = funcion_maximo(lista)

print(promedio)
print(suma)
print(maximo)



