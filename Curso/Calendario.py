import calendar

#PARA ELEGIR EL AÑO DESEADO
año = int(input("Ingrese el año: "))

print(calendar.calendar(año)) 



# PARA ELEGIR EL AÑO Y MES DESEADO
y= int(input("Ingrese el año: "))
m= int(input("Ingrese el mes: "))
print(calendar.month(y, m))