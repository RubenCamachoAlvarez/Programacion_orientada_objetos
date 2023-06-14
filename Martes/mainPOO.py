from cosas import Alumno
#Primer clase basica

def main():
     '''Creancion de objeto con la llamada al constructor.
    al1=Alumno()
    al2 = Alumno()
    print(al1)
    print(al1.facultad,"\t", al2.facultad,"\t", Alumno.facultad)
    al1.facultad="FES ARAGON EDO MEX"
    #print(Alumno.facultad)
    print("________Vistazo a los objetos___")
    print(cars(al1)
    print(cars(al2)
    print("_______Modificar atributo publico_____")
    al1.edad=999
    print(cars(al1)
    print(cars(al2)'''
     al1=Alumno("Ruben",20,"ICO")
     al2=Alumno("Ayo",21,"ICO")
     print(al1.nombre,"\t",al1.facultad,"\t", vars(al1))
     print(al2.nombre, "\t", al2.edad,"\t", vars(al2))
     al2.edad=22
     #Cambio de valor del atributo edad
     print(al2.nombre, "\t", al2.edad, "\t", vars(al2))


main()