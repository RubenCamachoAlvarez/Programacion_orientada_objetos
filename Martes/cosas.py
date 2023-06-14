#Ejercicio de las diapositivas

class Alumno:
    facultad="FES Aragon"
    ''' Self --> es la llamada al propio objeto
     pass -->rellenar por si falta algo  '''
    def __init__(self,nom,edad, carr):
       # print("Constructor: ", type(self))
        self.nombre=nom
        self.carrera=carr
        self.edad=edad
