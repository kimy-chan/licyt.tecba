class PERSON:
    def __init__(self,nombre, apellido, ocupacion):
        self.nombre = nombre
        self.apellido = apellido
        self.ocupacion = ocupacion
    def saludar(self):
        return f"hola mi nombre es  {self.nombre} {self.apellido} soy su {self.ocupacion}  "
class A(PERSON):
    def saludardoctor(self,especialidad):
        return f"hola mi nombre es  {self.nombre} {self.apellido} mi ocupacion es {self.ocupacion} y mi especialidad es {especialidad}"
class B(PERSON):
    def saludarenfermera(self, cargo):
        return f"hola  mi nombre es  {self.nombre} {self.apellido} soy su {self.ocupacion} y cuido a los {cargo}"
class C(PERSON):
    def saludarcardiologo(self,especialidad):
        return f"hola mi nombre es  {self.nombre} {self.apellido} soy {self.ocupacion} y soy {especialidad}"
class D(PERSON):
    def saludardoctora(self,especialidad):
        return f"hola mi nombre es  {self.nombre} {self.apellido} soy {self.ocupacion} y mi especialidad es {especialidad}"
class I(PERSON):
    def personal(self,cargo):
        return f"hola mi nombre es  {self.nombre} {self.apellido}  soy el {self.ocupacion} y administro el reparto de las {cargo}"


print("BIENVENIDOS AL HOSPITAL TECBA")
print("""
*****************
1.RESERVAR CITA
2.ESPECIALIDADES
3.EMERGEGENCIAS
4.SALIR
******************
""")
usuario = input("ingrese su eleccion -> ")
if (usuario == "1"):
    print("""
    SELECCIONE SU CITA
    1.MEDICO GENERAL
    2.ENFERMERIA
    3.PERSONAL DE ADMINISTRACION
    4.SALIR
     """)
    cita = input("medico-> ")
    if (cita == "1"):
        diego = PERSON("diego","gomez","medico general")
        print(diego.saludar())
    if (cita == "2"):
        tania = B("Tania","muñoz","enfermera")
        print(tania.saludarenfermera("cuido a los pacientes"))
    if (cita == "3"):
        henry = I("henry","florez","administrador")
        print(henry.personal("fichas"))
    if (cita == "4"):
        print("gracias vuelva pronto")

if (usuario == "2"):
    print("""
      ESPECIALIDADES
      1.CARDIOLOGO
      2.ENDOSCOPIA
      3.UROLOGO
      4.GINECOLOGO
      5.RAYOS X 
      6.CIRUJIA GENERAL
      7.GASTROENTEREOLOGIA
      8.INFECTOLOGIA
      9.NEFROLOGIA
      10.NEUMOLOGIA
      11.NEUROLOGIA
      12.NUTRIOLOGIA
      13.OFTALMOLIGA
      14.SALIR

    """)
    cita = input("medico -> " )

    if (cita == "1"):
        lola = C("Lola","sanchez", "medico")
        print(lola.saludarcardiologo("cardiologo"))
    elif (cita == "2"):
        andrea = D("andrea","limachi","medico")
        print(andrea.saludardoctora("endoscopia"))
    elif (cita == "3"):
        hugo = C("Hugo","sanchez","medico")
        print(hugo.saludarcardiologo("urologo"))
    elif (cita == "4"):
        carlos = C("carlos","lopez","medico")
        print(carlos.saludarcardiologo("ginecologo"))
    elif (cita == "5"):
        lola = D("lola","lopez","medico")
        print(lola.saludardoctora("rayos x"))
    elif (cita == "6"):
        martin = D("martin","cruz","medico")
        print(martin.saludardoctora("cirujia general"))
    elif (cita == "7"):
        paola = D("paola","lopez","medico")
        print(paola.saludardoctora("gastroentereologia"))
    elif (cita == "8"):
        stefany = D("Stefany","vela","medico")
        print(stefany.saludardoctora("infectologia"))
    elif (cita == "9"):
        jhanet = D("jhanet","ramirez","medico")
        print(jhanet.saludardoctora("nefrologia"))
    elif (cita == "10"):
        estrella = D("estrella","lopez","medico")
        print(estrella.saludardoctora("neumologia"))
    elif (cita == "11"):
        angela = D("angela","perez","medico")
        print(angela.saludardoctora("neurologia"))
    elif (cita == "12"):
        abigail = C("abigail","chambi","medico")
        print(abigail.saludarcardiologo("nutriologa"))
    elif (cita == "13"):
        mariana = A("mariana","rodrigez","medico")
        print(mariana.saludardoctor("oftalmologia"))
if (usuario == "3"):
    print("Hola, en que lo podemos ayudar ")
if (usuario == "4"):
    print("Gracias por su visita ")






