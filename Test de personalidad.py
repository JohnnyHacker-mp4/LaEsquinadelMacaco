contador_rv=0
contador_dc=0
contador_jm=0
p1=input("Si tuviera que elegir entre amor, dinero o salud,\n¿usted qué elige?\na.Amor\nb.Dinero\nc.Salud").strip()
if p1=="Amor" or p1=="a" or p1=="a." or p1=="a.Amor" or p1=="amor":
    contador_dc+=1
elif p1=="Dinero" or p1=="b" or p1=="b." or p1=="b.dinero" or p1=="dinero":
    contador_rv+=1
elif p1=="Salud" or p1=="c" or p1=="c." or p1=="b.salud" or p1=="salud":
    contador_jm+=1

p2=input("Un conocido suyo le propone un trío con una actriz p*rno, ¿aceptarías?\na.Claro que sí\b.No, nunca lo haría\nc.Todavía soy virgen :(").strip()
if p2=="a" or p2=="a." or p2=="Sí" or p2=="sí" or p2=="SI" or p2=="si":
    contador_rv+=1
elif p2=="b" or p2=="b." or p2=="NO" or p2=="no":
    contador_dc+=1
elif p2=="c" or p2=="c." or p2=="virgen":
    contador_jm+=1

p3=input("¿Cuál de estos fetiches se acercan más a tus gustos?\na.Cervix Penetrarion\nb.Sexo anal\c.Una relación basada en la confianza y amor mutuo").strip()
if p2=="a" or p2=="a.":
    contador_jm+=1
elif p2=="b" or p2=="b.":
    contador_dc+=1
elif p2=="c" or p2=="c.":
    contador_rv+=1
print("ANAL-izando información")
print("..."*10)
if contador_jm>contador_dc and contador_jm>contador_rv:
    print("FELICIDADES\nUN TIPO COMO TÚ SERÍA...\nMARCELO EL PUTO")
elif contador_dc>contador_rv and contador_dc>contador_jm:
    print("FELICIDADES\nUN TIPO COMO TÚ SERÍA...\nTheDIckTaco")
elif contador_rv > contador_dc and contador_rv > contador_jm:
    print("FELICIDADES\nUN TIPO COMO TÚ SERÍA...\nRoberto Gómez Bolaños")


