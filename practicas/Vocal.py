letra = input("Ingrese una vocal:").lower() #.lower() sirve para convertir las mayusculas 
                                            #ingresadas por minusculas automaticamente

if letra == 'a' or letra =='e' or letra == 'i' or letra == 'o' or letra == 'u':
    print(f"La letra '{letra}' es una vocal")
else:
    print(f"La letra '{letra}' no es vocal, es consonante")