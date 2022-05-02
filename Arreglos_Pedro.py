#  Se solicita el número de estudiantes y el dato entrante se asigna a n
n = int(input("Digite cantidad de estudiantes: ")) 
codigo = [ (input("Digite codigo: "))  for x in range(n)]
nota = [eval(input("Digite Nota: ")) for x in range(n)]

# nota maxima y minima
print("Nota Maxima:", max(nota), " Nota Minima:", min(nota)) 

# Calculo de promedio
promedio = sum(nota)/n 
print("Promedio es: ", promedio)

# Cuantos estudiantes Aprobaron y Cuantos Reprobaron
aprobaron = [nota for nota in nota if nota >= 3] 
reprobaron = [nota for nota in nota if nota < 3]
print("Aprobaron: ", len(aprobaron), "  Reprobaron: ", len(reprobaron))

# se inicia variable para contar 
# los estudiantes quedaron en cada una de las categorias
a = 0
b = 0
c = 0
d = 0

# relacion entre codigos y notas
print("----Relacion codigo-notas----" )
print("Codigo", "Nota" )
for valor_a, valor_b in zip(codigo, nota): 
    if 0.5 <= valor_b < 2.0:
       print(valor_a, valor_b, " Insuficiente")
       a = a + 1
    elif 2.0 <= valor_b < 3.0:
        print(valor_a, valor_b, " Suficiente")
        b = b + 1
    elif 3.0 <= valor_b < 4.0:
        print(valor_a, valor_b, " Bien")
        c = c + 1
    elif 4.0 <= valor_b <= 5.0:
        print(valor_a, valor_b, " Muy Bien")
        d = d + 1
print(valor_a, valor_b)
#  impresion de cuantos estudiantes quedaron en cada una de las categorias
print("Insuficiente: ", a)
print("Suficiente: ", b)
print("Bien: ", c)
print("Muy Bien: ", d)

# Porcentajes de aprobados y reprobados
porcentaje1 = (100/n)*len(aprobaron)
porcentaje2 = (100/n)*len(reprobaron)
print("Pocentaje de Aprobados: ", porcentaje1,"%",  "  Porcentaje de Reprobados: ", porcentaje2,"%")

# estudiantes que obtuvieron las mas alta nota




 

