class Asiento:
    def __init__ (self,color,precio,registro):
        self.color = color
        self.precio = precio
        self.registro = registro
    
    def cambiarColor(self,x):
        colores=["rojo","verde","amarillo","negro","blanco"]
        for i in colores:
            if i==x:
                self.color=x

class Motor:
    def __init__ (self,numeroCilindros,registro,tipo):
        self.numeroCilindros= numeroCilindros
        self.registro= registro
        self.tipo= tipo
    
    def cambiarRegistro (self,registro):
        if type(registro) == int:
            self.registro=registro 
    
    def asignarTipo (self,tipo):
        if type(tipo)== str:
            if(tipo == "electrico" or tipo == "gasolina"):
                self.tipo=tipo

class Auto:
    def __init__(self,modelo,precio,asientos,marca,motor,registro,acientos,cantidadCreados):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
      # self.acientos = acientos
        self.cantidadCreados= cantidadCreados
        
    def cantidadAsientos(self):
        acientos=0
        for i in asientos:
            if i != None:
                acientos+=1
        return acientos 
    
    def verificarIntegridad (self):
        aviso="Auto original"
        if self.registro==motor.registro:
             for i in asientos:
                if i != None:
                    aviso="Las piezas no son originales"
                    break
        else:
             aviso="Las piezas no son originales"
             
        return aviso
                
                
