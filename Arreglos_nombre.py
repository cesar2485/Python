
n = int(input("Digite cantidad de estudiantes: ")) #  Se solicita el número de estudiantes y el dato entrante se asigna a n
codigo = [ (input("Digite codigo: T000"))  for x in range(n)]
nota = [eval(input("Digite Nota: ")) for x in range(n)]
print("Nota Maxima:", max(nota), " Nota Minima:", min(nota)) # se imprime nota maxima y minima
promedio = sum(nota)/n # Calculo de promedio
aprobaron = [nota for nota in nota if nota >= 3] 
reprobaron = [nota for nota in nota if nota < 3]
print("Promedio es: ", promedio)
print("Aprobaron: ", len(aprobaron), "  Reprobaron: ", len(reprobaron))
#print(codigo)
#print(nota)

