Tareas=[]
res=True
while res:
    print("Bienvenido",
    "\n1.Crear Tarea\n2.Eliminar Tarea\n3.Completar tarea")

    opc = int(input("Ingrese la opcion que desea seleccionar: "))

    if (opc==1):
        print("Ha seleccionado la opcion de Crear Tarea")

        tarea=str(input("Ingrese la tarea que desea guardar: "))
        Tareas.append(tarea)
        print("Tarea Guardada correctamente")

        preg=int(input("Desea volver al menu principal? 1(si) 2(no)"))

        if preg !=1:
            print("Hasta la proxima")
            res=False

    elif opc==2:
        print("Las tareas que ha guardado son: ")
        for i in range(len(Tareas)):
            print(i+1,":", Tareas[i])

        borrar=int(input("Digite el numero de la tarea que quiere borrar: "))

        if 1 <= borrar <= len(Tareas):
            TareaAEliminar = Tareas.pop(borrar - 1)
            print(f"Tarea {TareaAEliminar} eliminada")
        else:
            print("No existe una tarea con ese indice")
        
        preg=int(input("Desea volver al menu principal? 1(si) 2(no)"))

        if preg !=1:
            print("Hasta la proxima")
            res=False
    
    elif opc==3:
        print("Las tareas que ha guardado son: ")
        for i in range(len(Tareas)):
            print(i+1,":", Tareas[i])

        completar=int(input("Digite el numero de la actividad a completar"))
        if 1 <= completar <= len(Tareas):
            Tareas[completar] +=" Completada"
            print(f"Tarea {completar} ha sido completada")
        
        preg=int(input("Desea volver al menu principal? 1(si) 2(no)"))

        if preg !=1:
            print("Hasta la proxima")
            res=False
            
    else:
        print("Opcion no valida")
