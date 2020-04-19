
contraseña="Salamanca18"
clave=input("Ingresar contraseña: ")
while clave != contraseña:
    print("Contraseña incorrecta.")
    intento=input("Desea volver a intentarlo?(S/N)")
    if intento.upper()=="N":
        break
    elif intento.upper()=="S":
        clave=input("Ingresar contraseña: ")
if clave == contraseña:
    print("Contraseña corrcta.")
print("Fin del Prograama.")