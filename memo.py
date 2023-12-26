import json

def sumcl(clave):
    return clave[0]+clave[1]

class Archivo: #objeto para leer el archivo (sólo vuelca en un diccionario a un JSON)
        
        
    def actualizar(self): #funcion que sirve para volver a extraer la info del archivo 
        try:
            with open(self.nombre, "r") as archivo:
                self.__base = json.load(archivo)
                # Ahora 'base' contiene la lista de diccionarios
        except FileNotFoundError:
            print("Error en el archivo")
        
    def __init__(self,nombre="baseMemo.json") -> None:
        self.__nombre = nombre
        self.actualizar()

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def base(self):
        return self.__base
        
    def extraer(self):
        self.actualizar()
        return self.base
    
    def extraerCampo(self,indx):
        self.actualizar()
        return self.base[indx]

    
    def volcar(self,newbase):      
        self.__base = newbase
        try:
            with open(self.nombre, "w") as archivo:
                json.dump(self.base, archivo)
            print(f"Se ha guardado correctamente en '{self.nombre}'.")
        except FileNotFoundError:
            print(f"El directorio del archivo '{self.nombre}' no existe.")
        except Exception as e:
            print(f"Ocurrió un error: {e}")
        """
        """
class Estructura:
    def __init__(self,mod = 0) -> None:
        self._mod = 0 


class Campo:
    def __init__(self,base) -> None:
        self.__base = base

    @property
    def base(self):
        return self.__base
        
    def aggClav(self,clav,ty):
        # se agrega la clave y se pide la nueva palabra 
        self.__base[ty][clav]= input("ingresa la palabra: ")
    
    def valClav(self,clave,ty):#validar las palabras
        if clave in self.base[ty].keys():
            print(self.base[ty][clave])
        else:
            self.aggClav(clave,ty)
            

class imagen:
    def __init__(self,sujeto,verbo,predicado) -> None:
        pass
    
def buc(l): #funcion para comparar mientras pides un dato
    l[0]=input("ingresa 2 letras: ")
    return l[0]

if __name__ == "__main__":
    Archi = Archivo()
    base  = Campo(Archi.extraer())
    personaje = 0
    accion = 0
    esq_memo = 0 #por defecto sólo 2 diccionarios 
    if esq_memo == 0:
        personaje  = base.base[0]
        accion = base.base[1]
        
    bufEsq = "aer"
    bufVer = "aq"
        
    print("Bienvenido al asistente de memorización de BLD 3x3")
    bf=1
    bfl = [0] #esta es porque las listas se pasan por referencia, no por valor
    per = False
    while(buc(bfl) != "0"):
        bf = bfl[0]
        base.valClav(bf,per)

        per = not per

    Archi.volcar(base.base)
        