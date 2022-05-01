
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
print("----Relacion codigo-notas----" )
print("Codigo", "Nota" )
for valor_a, valor_b in zip(codigo, nota): 
#for indice in nota :
    if 0.5 <= valor_b < 2.0:
       print(valor_a, valor_b, " Insuficiente")
       insuficiente = [int(valor_b)]
    elif 2.0 <= valor_b < 3.0:
        print(valor_a, valor_b, " Suficiente")
        suficiente = [int(valor_b)]
    elif 3.0 <= valor_b < 4.0:
        print(valor_a, valor_b, " Bien")
    elif 4.0 <= valor_b <= 5.0:
        print(valor_a, valor_b, " Muy Bien")

# cuantos estudiantes quedaron en cada una de las categorias
print("Suficiente: ", len(suficiente))
print("Insuficiente: ", len(insuficiente))

# Porcentajes de aprobados y reprobados
porcentaje1 = (n/100)*len(aprobaron)
porcentaje2 = (n/100)*len(reprobaron)
print("Aprobados: ", porcentaje1,"%",  "  Reprobados: ", porcentaje2,"%")


 

