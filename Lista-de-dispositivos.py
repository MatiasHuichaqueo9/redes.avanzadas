file = open("Red-Python.py", "r")
user_ = "Matias"
pwd_ = "5912"
print("Bienvenido a la lista de datos")
print("Usuario: ")
user = input()
print("Contraseña: ")
pwd = input()
if user == user_ and pwd == pwd_:
    print("Bienvenido a la lista de dispositivo")
    for item in file:
        print(item)
    file.close()
else:
    print("usuario o contraseña invalido!")
    file.close()
    exit()

while True:
    respuesta = input("¿Deseas editar el programa? (s/n): ")
    if respuesta == "s":
        print("Acceso autorizado!")
        respuesta_valida = True
        dispositivo = input("Ingrese el nombre del dispositivo: ")
        direccion_IP = input("Ingrese la direccion IP: ")
        vlan = input("Vlan a la que pertenece: ")
        servicios_comprometidos = input("Servicios que tiene levantados: ")
        capa_a_la_que_pertenece = input("Ingrese a la capa que pertenece: ")
        print(dispositivo, "\n" + direccion_IP, "\n" + vlan, "\n" + servicios_comprometidos, "\n" + capa_a_la_que_pertenece, "\n")
        
        guardar = input("¿Desea guardar la informacion? (s/n): ")
        if guardar == "s":
            with open("Red-Python.py", "a") as archivo:
                archivo.write(dispositivo + ", " + direccion_IP + ", " + vlan + ", " + servicios_comprometidos+ ", " + capa_a_la_que_pertenece + "\n ")
                print("Informacion guardada con exito")
    elif respuesta == "n":
        print("Programa finalizado")
        break
    else:
        print("Opcion no valida. Intente de nuevo")
        
file = open("Red-Python.py", "r")
lista = file.readlines()
file.close()


print("La lista actualizada es: ")
for item in lista:
   print(item)
