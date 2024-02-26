print("\n -----Informacion personal----- \n")
nombre = input("Ingrese su nombre: ")
identificacion = input("Ingrese su nùmero de identificaciòn: ")
edad = input("Ingrese su edad: ")
altura = input("Ingrese su altura: ")
rh = input("Ingrese su tipo de sangre: ")

dataUser = [nombre,identificacion,edad,altura,rh]

print("\n ----Informacion residencia----- \n")
direccion = input("Ingrese su direccion: ")
barrio = input("Ingrese barrio: ")
ciudad = input("Ingrese ciudad: ")

dataDirecciones = [direccion,barrio,ciudad]

print("\n -----Informacion Educacion----- \n")
nivelEscolaridad = input("Ingrese su nivel de escolaridad: ")
institucion = input("Ingrese institucion: ")
ciudadEstudio = input("Ingrese ciudad: ")
año = input("Ingrese el año de graducion: ")

dataEstudios = [nivelEscolaridad,institucion,ciudadEstudio,año]

print("\n -----Informacion Laboral----- \n")
empresa = input("Ingrese nombre de la empresa: ")
cargo = input("Ingrese cargo ejercido: ")
añosLaborados = input("Ingrese años laborados: ")
ciudadLaboral = input("Ingrese ciudad: ")

dataLaboral = [empresa,cargo,añosLaborados,ciudadLaboral]

print("Datos guardados correctamente")

opcion = input("""---Para consultar informacion---
               1. Informacion Personal
               2. Inforamcion residencia
               3. Informacion eduacion
               4. Informacion laboral\n""")

if opcion == "1":
    print("\n -----Informacion personal----- \n")
    print(dataUser)
elif opcion == "2":
    print("\n ----Informacion residencia----- \n")
    print(dataDirecciones)
elif opcion == "3":
    print("\n -----Informacion Educacion----- \n")
    print(dataEstudios)
elif opcion == "4":
    print("\n -----Informacion Laboral----- \n")
    print(dataLaboral)

