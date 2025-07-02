# creacion de un script para ingreso de datos
# consigna crear un diccionario con los datos nombre, apellido, edad
# mediante el ingreso por consola, solicitar la nacionalidad y agregarla al diccionario
# mostrar por pantalla los datos del diccionario, nombre, apellido, edad, nacionalidad
diccionario={"Nombre":"Juan","Apellido":"Perez","Edad":42}

def ingresar_nacionalidad():
    while True:
        nacionalidad=input("Ingrese la Nacionalidad: ")
        # verifico que en la entrada de datos no haya numeros
        if any(caracter.isdigit() for caracter in nacionalidad):
            print("El dato no debe contener numeros, vuelva a intentar")
        else:
            return nacionalidad
    
# llamo a la funcion de ingreso de datos
nacionalidad = ingresar_nacionalidad()  

diccionario['Nacionalidad']=nacionalidad.upper()

print("------- Datos del Cliente -------\n")
print("Nombre: ",diccionario['Nombre'])
print("Apellido: ",diccionario['Apellido'])
print("Edad: ",diccionario['Edad'])
print("Nacionalidad: ",diccionario['Nacionalidad'])
print("---------------------------------\n")



