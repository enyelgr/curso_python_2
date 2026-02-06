helado = input("¿Que helado te gusta?")
figura = input("¿Que figura quieres tu helado?")
choco = input("¿Lo quieres con chocolate?")
if helado == "uva" and figura == "triangular" and choco == "si":
    print("Tu helado esta listo")
elif helado == "fresa" and figura == "corazon" and choco == "no":
    print("Tu helado esta listo")
elif helado == "mora" and figura == "luna" and choco == "si":
    print("Tu helado esta listo")    
else:
    print("No tenemos esa combinacion")