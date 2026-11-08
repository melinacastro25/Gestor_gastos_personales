def saludar (nombre, apellido, profesión="Estudiante"): 
    print(f"Hola, {nombre} {apellido}! Bienvenido/a")

saludar(apellido="González", nombre="Aziel")

def nombre_funcion (parámetros): 
    #aquí va la lógica de la función
    return Valor 
    
def calculo_area_rectangulo(base,altura): 
    area = base * altura
    return area

resultado = calculo_area_rectangulo(9,40)
print(f"El área del rectángulo es: {resultado}")

def crear_perfil(nombre, edad, profesión="Estudiante"): 
    return f"Perfil: {nombre}, edad: {edad}, {profesión}"

print(crear_perfil("Aziel", 29))
print(crear_perfil("Aziel", 29, "Ingeniero"))

#valores de retorno
def mostrar_mensaje(): 
    print("¡Hola!. Este es un mensaje de retorno")
    
resultado_mensaje = mostrar_mensaje()
print(resultado_mensaje)

#funciones con múltiples retornos

def analizar_numero(numero): 
    es_par = numero % 2 == 0 
    es_positivo = numero > 0 
    return es_par, es_positivo

es_par, es_positivo = analizar_numero(36)
print(f"¿es par? {es_par}")
print(f"¿es positivo? {es_positivo}")

#alcance de variables
nombre_curso = "Python" #Variable global

def mostrar_curso():
    instructor = "Aziel" #Variable local
    print(f"Curso: {nombre_curso}")
    print(f"Instructor: {instructor}")
    
mostrar_curso()

contador = 0 #variable global

def incrementar():
    global contador
    contador += 1
    
print(contador)
incrementar()
print(contador)



