#Variables
mis_tareas = []
opcion = "0"

while opcion != "3":
    print("""
          Elije una opción: 
     1. Agregar una tarea
     2. Ver mis tareas
     3. Salir""")

    opcion = input("")

    if opcion == "1" :
        print("Agrega la tarea: ")
        tarea = input("")
        mis_tareas.append(tarea)

    elif opcion == "2" :
        print("Tareas agendadas : ", mis_tareas)
    
    elif opcion == "3" :
        print("Saliendo")

    else :
        print("La opción no es válida ") 