#lista donde se almacenan los gastos que se registran en el sistema 
gastos = []

#variable para contar las operaciones de registros
contador_registros = 0

#función que muestre las opciones del menú
def mostrar_menu(): 
    print("\nGestor de Gastos Personales")
    print("1. Registrar gasto")
    print("2. Ver lista gastos")
    print("3. Ver resumen gastos")
    print("4. Salir")

#definir la función y sus parámetros
def registrar_gasto(gastos, moneda="₡"):
    
    #acceder a variable global
    global contador_registros 
    
    #solicitar datos del gasto registrado al usuario
    descripcion = input("Ingrese la descripción del gasto: ")
    monto = float (input("Ingrese el monto del gasto: "))
    
    #Verificar que el monto ingresado es mayor a cero. 
    if monto > 0: 
        #Guardar la descripción y monto ingresados
        gastos.append({
                "descripcion": descripcion, 
                "monto": monto
                })
        
        #actualizar el contador
        contador_registros += 1
        
        #Mensaje de confirmación
        print(f"\n¡Gasto registrado correctamente!")
        print(f"Descripción: {descripcion}")
        print(f"Monto: {moneda}{monto:.2f}")
        
    else: 
        #Mostrar mensaje si el monto es menor a cero
        print("Error: el monto debe ser mayor que cero")
        


#función para mostrar gastos registrados 
def mostrar_gastos(gastos, moneda="₡"): 
    
    #Verificar que existan gastos en la lista
    if len(gastos) == 0: 
        print("\nNo hay gastos registrados")
        
    else: 
        #Mostrar listado de gastos
        print("\nLista de gastos")
        
        #Iniciar el número del primer gasto
        numero_gasto = 1
        
        #Recorrer lista y mostrar gasto
        for gasto in gastos: 
            print(f"{numero_gasto}. {gasto ['descripcion']}: {moneda}{gasto['monto']:.2f}")
            
            #Aumentar el número para el siguiente gasto
            numero_gasto += 1

#Función para calcular el total
def calcular_total(gastos): 
    #Iniciar el acumulador
    total = 0 
    
    #Recorrer los gastos y sumar montos
    for gasto in gastos: 
        total += gasto["monto"]
        
    #Devolver el total calculado
    return total

#Función para calcular el resumen de gastos
def obtener_resumen(gastos): 
    
    #Verificar si existen registros de gastos
    if len(gastos) == 0: 
        return 0, 0, None
    
    #Obtener el total 
    total = calcular_total(gastos)
    
    #Calcular promedio de gastos
    promedio = total / len(gastos)
    
    #Iniciar el gasto mayor con el primer elemento
    gasto_mayor = gastos [0]
    
    #Recorrer la lista para identificar el gasto 
    for gasto in gastos: 
        if gasto["monto"] > gasto_mayor["monto"]: 
            gasto_mayor = gasto 
            
    #Devolver los tres resultados
    return total, promedio, gasto_mayor

#Función mostrar resumen de gastos
def mostrar_resumen(gastos, moneda="₡"):
    
    #Obtener los resultados de la función anterior
    total, promedio, gasto_mayor = obtener_resumen(gastos)
    
    #Verificar si existen gastos registrados
    if gasto_mayor == None: 
        print("\nNo hay gastos registrados para mostrar el resumen")
        
    else: 
        #Mostrar los resultados del resumen
        print("\nResumen de Gastos")
        print(f"Total gastado: {moneda}{total:.2f}")
        print(f"Promedio por gasto: {moneda}{promedio:.2f}")
        print(f"Gasto de mayor monto: {gasto_mayor['descripcion']} - {moneda}{gasto_mayor['monto']:.2f}")

#Función principal del programa        
def main():
    
    #Mantener el menú activo hasta que el usuario seleccione salir
    while True: 
        
        #Mostrar menú y solicitar seleccionar una opción
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        #Ejecutar la función correspondiente
        if opcion == "1": 
            registrar_gasto(gastos, moneda="₡")
            
        elif opcion == "2": 
            mostrar_gastos(gastos)
            
        elif opcion == "3": 
            mostrar_resumen(gastos)
            
        elif opcion == "4": 
            #Mostrar el contador y finalizar el programa 
            print(f"\nCantidad de registros: {contador_registros}")
            print("¡Gracias por utilizar nuestro gestor de gastos!")
            break
        
        else: 
            #Mensaje si se selecciona una opción incorrecta
            print("Opción no válida. Intente nuevamente")

#Ejecutar el programa principal 
main()
 
        