
n = int(input("Digite cantidad de estudiantes: ")) #  Se solicita el número de estudiantes y el dato entrante se asigna a n
codigo = [ (input("Digite codigo: "))  for x in range(n)]
nota = [eval(input("Digite Nota: ")) for x in range(n)]

# se imprime nota maxima y minima
print("Nota Maxima:", max(nota), " Nota Minima:", min(nota)) 

# Calculo de promedio
promedio = sum(nota)/n 
print("Promedio es: ", promedio)

# Cuantos estudiantes Aprobaron y Cuantos Reprobaron
aprobaron = [nota for nota in nota if nota >= 3] 
reprobaron = [nota for nota in nota if nota < 3]
print("Aprobaron: ", len(aprobaron), "  Reprobaron: ", len(reprobaron))

# relacion entre codigos y notas
print("----relacion codigo-notas----" )
for indice in range(0, len(codigo)): # 
    print(codigo[indice], nota[indice])

 

