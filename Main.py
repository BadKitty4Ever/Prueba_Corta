from Verificador import minusculas, mayusculas, numeros, ocho_o_mas

verificaciones = []

password = input("Password: ")

contador = 0

if minusculas(password):
    verificaciones.append("Letras minusculas")
    contador += 25

if mayusculas(password):
    verificaciones.append("Letras mayusculas")
    contador += 25

if numeros(password):
    verificaciones.append("Numeros")
    contador += 25

if ocho_o_mas(password):
    verificaciones.append("8 o mas")
    contador += 25

print("Nivel de Seguridad:",contador,"%")
print("Caracteristicas cumplidas:",verificaciones)