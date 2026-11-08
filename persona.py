# sistema de gestión de empleados 
class persona: 
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def saludar(self):
        return f"Hola, soy {self.nombre} y tengo {self.edad} años"
    
    def cumplir_años(self): 
        self.edad += 1
        print(f"Acabo de cumplir años, ahora tengo {self.edad} años")
        
Raúl = persona("Raúl", 40)
Fernando = persona("Fernando", 30)
print(Raúl.saludar())
print(Fernando.saludar())