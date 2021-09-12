""" programa para examinar a las personas
     en temas culturales e historicos """

puntos = 0
valid = False 


def Capitales(Cuestionario):
     while True:
          if Cuestionario == "Capitales":
               print("a)Santo Domingo\n", "b)Washintong DC\n", "c)Grecia\n")

               Pregunta_1 = str(input("Cual es la capital de Republica Dominicana?\n"))
               print("a)Santo Domingo\n", "b)Washintong DC\n", "c)Grecia\n")

          if Pregunta_1 == "Santo Domingo":
               print("Correcto")
               puntos += 1 
          else:
               print("respuesta no valida, la respuuesta es: ", Respuestas[0], puntos1)

     else:
          print("intente de nuevo..")

Cuestionario = str(input("eliga un cuestionario a elegir:\n"))

if Cuestionario == "Capitales":
     Capitales(Cuestionario)

else: 
     print("elija la respuesta correcta.")

     