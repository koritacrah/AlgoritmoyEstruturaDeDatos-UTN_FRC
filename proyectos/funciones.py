from clases import *
paises = (
    "Chile",
    "Argentina",
    "Brasil",
    "Bolivia",
    "Paraguay",
    "Uruguay",
    "Otro",
)


def op1(v):
    if not v:
        m = open("peajes-tp3.txt", "rt")
        vuelta = 0
        for i in m:
            if vuelta >= 1:
                t =Ticket(i[0:10],i[10:17],i[17],i[18],i[19],i[20:23])
                v.append(t)
            vuelta += 1
    else:
        print("Ya existen tikets guardados desea eliminar esa lista y crear una nueva?")
        print("1_ Si")
        print("2_ No")
        op = input("ingrese su opcion: ")
        if op == "1":
            m = open("peajes-tp3.txt", "rt")
            v = []
            vuelta = 1
            for i in m:
                if vuelta >= 1:
                    t =Ticket(i[0:10], i[10:17], i[17], i[18], i[19], i[20:23])
                    v.append(t)
                vuelta += 1
        else:
            pass
    return v




def validacion_incorrecta_por_cantidad(n, subclase, condicion):
    while len(subclase) != int(n):
        print("no se cumple " + condicion)
        subclase = input("ingrese de nuevo los parametros: ")
        # verifica que la cantidad de numeros ingresados en la subclase sdea la de n y la condicion es el mensaje de error


def validacion_incorrecta_por_numero(desde, hasta, subclase, condicion):
    while not (desde <= int(subclase) <= hasta):
        print("no se cumple " + condicion)
        subclase = input("ingrese de nuevo los parametros: ")
    # valida que el valor de subclase este entre esos dos numeros desde y hasta,


def detectar_pais_por_patente(lineas):
    if (
        lineas[0] == " "
        and "A" <= lineas[1] <= "Z"
        and "A" <= lineas[2] <= "Z"
        and "A" <= lineas[3] <= "Z"
        and "A" <= lineas[4] <= "Z"
        and "0" <= lineas[5] <= "9"
        and "0" <= lineas[6] <= "9"
    ):
        procedencia = 0  # chile
    else:
        if (
            "A" <= lineas[0] <= "Z"
            and "A" <= lineas[1] <= "Z"
            and "0" <= lineas[2] <= "9"
            and "0" <= lineas[3] <= "9"
            and "0" <= lineas[4] <= "9"
            and "A" <= lineas[5] <= "Z"
            and "A" <= lineas[6] <= "Z"
        ):
            procedencia = 1  # argentina

        else:
            if (
                "A" <= lineas[0] <= "Z"
                and "A" <= lineas[1] <= "Z"
                and "A" <= lineas[2] <= "Z"
                and "0" <= lineas[3] <= "9"
                and "A" <= lineas[4] <= "Z"
                and "0" <= lineas[5] <= "9"
                and "0" <= lineas[6] <= "9"
            ):
                procedencia = 2  # brasil
                # LLLNLNN
            else:
                if (
                    "A" <= lineas[0] <= "Z"
                    and "A" <= lineas[1] <= "Z"
                    and "0" <= lineas[2] <= "9"
                    and "0" <= lineas[3] <= "9"
                    and "0" <= lineas[4] <= "9"
                    and "0" <= lineas[5] <= "9"
                    and "0" <= lineas[6] <= "9"
                ):
                    procedencia = 3  # bolivia
                    # LLNNNNN
                else:
                    if (
                        "A" <= lineas[0] <= "Z"
                        and "A" <= lineas[1] <= "Z"
                        and "A" <= lineas[2] <= "Z"
                        and "A" <= lineas[3] <= "Z"
                        and "0" <= lineas[4] <= "9"
                        and "0" <= lineas[5] <= "9"
                        and "0" <= lineas[6] <= "9"
                    ):
                        procedencia = 4  # paraguay
                        # LLLLNN
                    else:
                        if (
                            "A" <= lineas[0] <= "Z"
                            and "A" <= lineas[1] <= "Z"
                            and "A" <= lineas[2] <= "Z"
                            and "0" <= lineas[3] <= "9"
                            and "0" <= lineas[4] <= "9"
                            and "0" <= lineas[5] <= "9"
                            and "0" <= lineas[6] <= "9"
                        ):
                            procedencia = 5  # uruguay
                            # LLLNNNN
                        else:
                            procedencia = 6  # otros paises
    return procedencia


def op2():
    cod = input("ingrese el codigo identificador de 10 digitos: ")
    validacion_incorrecta_por_cantidad(
        "10", cod, "el codigo identificador de 10 digitos"
    )
    pat = input(
        "\nIngrese la patente del vehiculo 7 caracteres alfanuméricos.\n"
        "Recuerde que si es de Chile, el primer carácter debe ser un espacio: "
    )
    validacion_incorrecta_por_cantidad("7", pat, "con la patente")
    vehiculo = int(
        input(
            "\nTIPO DE VEHICULO\n"
            "0 - Si es una moto.\n"
            "1 - Si es un auto.\n"
            "2 - Si es un camión.\n"
            "Ingrese el tipo de vehiculo: "
        )
    )
    validacion_incorrecta_por_numero(0, 2, vehiculo, "con el tipo de vehiculo")
    pago = int(
        input(
            "\nFORMA DE PAGO\n"
            "1 - Si es manual.\n"
            "2 - Si es telepeaje.\n"
            "Ingrese la forma de pago: "
        )
    )
    validacion_incorrecta_por_numero(1, 2, pago, "con la forma de pago")
    paisdecobro = int(
        input(
            "\nPAIS\n"
            "0 - Argentina.\n"
            "1 - Bolivia.\n"
            "2 - Brasil.\n"
            "3 - Paraguay.\n"
            "4 - Uruguay.\n"
            "Ingrese el país donde nos encontramos: "
        )
    )
    validacion_incorrecta_por_numero(
        0, 4, paisdecobro, "con el pais en donde nos encontramos"
    )
    distancia = input(
        "\nIngrese la cantidad de km recorridos.\n"
        "Recuerde que no son más de 3 dígitos: "
    )
    validacion_incorrecta_por_cantidad("3", distancia, "con la distancia ")
    t = Ticket(cod, pat, vehiculo, pago, paisdecobro, distancia)
    print(t)
    return t


def op3(v):
    if v == []:
        print("todavia no hay ningun tiket generado elija antes la opcion 1 o 2")
    else:
        n = len(v)
        if n > 1:
            for i in range(n - 1):
                for j in range(i + 1, n):
                    if v[i].codigo > v[j].codigo:
                        v[i].codigo, v[j].codigo = v[j].codigo, v[i].codigo
                # le asigno a la variable pais, el pais detectado por la patente
                pais = paises[(detectar_pais_por_patente(v[i].patente))]
                print(
                    "codigo del tiket: ",
                    v[i].codigo,
                    " -patente: ",
                    v[i].patente,
                    " -pais del vehiculo: ",
                    pais,
                    " -tipo de vehiculo: ",
                    v[i].vehiculo,
                    " -forma de pago: ",
                    v[i].pago,
                    " -pais de la cabina: ",
                    v[i].paisdecobro,
                    " km recorridos: ",
                    v[i].distancia,
                )
        else:
            pais = paises[(detectar_pais_por_patente(v[0].patente))]
            print(
                "codigo del tiket: ",
                v[0].codigo,
                " -patente: ",
                v[0].patente,
                " -pais del vehiculo: ",
                pais,
                " -tipo de vehiculo: ",
                v[0].vehiculo,
                " -forma de pago: ",
                v[0].pago,
                " -pais de la cabina: ",
                v[0].paisdecobro,
                " km recorridos: ",
                v[0].distancia,
            )


def op4(v):
    if v == []:
        print("todavia no hay ningun tiket generado elija antes la opcion 1 o 2")
    else:
        p = input("ingrese la patente a buscar: \n")
        x = input("ingrese cabina por la que pasó el vehiculo: ")
        encontrado = False
        n = len(v)
        for i in range(n - 1):
            if v[i].patente == p and v[i].paisdecobro == x:
                print("Registro encontrado:")
                print("Código del ticket:", v[i].codigo)
                print("Patente:", v[i].patente)
                print(
                    "País del vehículo:",
                    paises[(detectar_pais_por_patente(v[i].patente))],
                )  # País genérico en este ejemplo
                print("Tipo de vehículo:", v[i].vehiculo)
                print("Forma de pago:", v[i].pago)
                print("País de la cabina:", v[i].paisdecobro)
                print("Kilómetros recorridos:", v[i].distancia)
                encontrado = True
                break

        if not encontrado:
            print(
                "No se encontró ningún registro que coincida con los criterios especificados."
            )


def op5(v):
    if v == []:
        print("todavia no hay ningun tiket generado elija antes la opcion 1 o 2")
    else:
        c = input("ingrese el codigo a buscar: \n")
        encontrado = False
        n = len(v)
        if n == 1:
            if v[0].codigo == c:
                if v[0].pago == 1:
                    v[0].pago = 2
                else:
                    v[0].pago = 1
                print("Registro encontrado:")
                print("Código del ticket:", v[0].codigo)
                print("Patente:", v[0].patente)
                print(
                    "País del vehículo:",
                    paises[(detectar_pais_por_patente(v[0].patente))],
                )  # País genérico en este ejemplo
                print("Tipo de vehículo:", v[0].vehiculo)
                print("Forma de pago:", v[0].pago)
                print("País de la cabina:", v[0].paisdecobro)
                print("Kilómetros recorridos:", v[0].distancia)
                encontrado = True

            if not encontrado:
                print(
                    "No se encontró ningún registro que coincida con los criterios especificados."
                )
        else:
            for i in range(n - 1):
                if v[i].codigo == c:
                    if v[i].pago == 1:
                        v[i].pago = 2
                    else:
                        v[i].pago = 1
                    print("Registro encontrado:")
                    print("Código del ticket:", v[i].codigo)
                    print("Patente:", v[i].patente)
                    print(
                        "País del vehículo:",
                        paises[(detectar_pais_por_patente(v[i].patente))],
                    )  # País genérico en este ejemplo
                    print("Tipo de vehículo:", v[i].vehiculo)
                    print("Forma de pago:", v[i].pago)
                    print("País de la cabina:", v[i].paisdecobro)
                    print("Kilómetros recorridos:", v[i].distancia)
                    encontrado = True
                    break

            if not encontrado:
                print(
                    "No se encontró ningún registro que coincida con los criterios especificados."
                )


def op6(v):
    if v == []:
        print("todavia no hay ningun tiket generado elija antes la opcion 1 o 2")
    else:
        n = len(v)
        # Listado de paises
        conteo_paises = [0, 0, 0, 0, 0, 0, 0]
        if n == 1:
            procedencia = detectar_pais_por_patente(v[0].patente)
            conteo_paises[procedencia] += 1
            print("Chile")
            print(conteo_paises[0])
            print("Argentina")
            print(conteo_paises[1])
            print("Brasil")
            print(conteo_paises[2])
            print("Bolivia")
            print(conteo_paises[3])
            print("Paraguay")
            print(conteo_paises[4])
            print("Uruguay")
            print(conteo_paises[5])
            print("Otros")
            print(conteo_paises[6])
        else:
            for i in range(n - 1):
                procedencia = detectar_pais_por_patente(v[i].patente)
                conteo_paises[procedencia] += 1
            print("Chile")
            print(conteo_paises[0])
            print("Argentina")
            print(conteo_paises[1])
            print("Brasil")
            print(conteo_paises[2])
            print("Bolivia")
            print(conteo_paises[3])
            print("Paraguay")
            print(conteo_paises[4])
            print("Uruguay")
            print(conteo_paises[5])
            print("Otros")
            print(conteo_paises[6])


def op7(v):
    if v == []:
        print("todavia no hay ningun tiket generado elija antes la opcion 1 o 2")
    else:
        n = len(v)
        # Tickets por tipo de vehiculo
        pagos_tickets = [0, 0, 0]
        if n == 1:
            v[0].vehiculo = int(v[0].vehiculo)
            monto = calcular_monto(v[0])
            pagos_tickets[v[0].vehiculo] += monto
            print("Moto")
            print(pagos_tickets[0])
            print("Auto")
            print(pagos_tickets[1])
            print("Camion")
            print(pagos_tickets[2])
        else:
            for i in range(n - 1):
                v[i].vehiculo = int(v[i].vehiculo)
                monto = calcular_monto(v[i])
                pagos_tickets[v[i].vehiculo] += monto
            print("Moto")
            print(pagos_tickets[0])
            print("Auto")
            print(pagos_tickets[1])
            print("Camion")
            print(pagos_tickets[2], "\n")
    return pagos_tickets
    # for i in v:
    #     i.vehiculo = int(i.vehiculo)
    #     monto = calcular_monto(i)
    #     pagos_tickets[i.vehiculo] += monto
    # print("Moto")
    # print(pagos_tickets[0])
    # print("Auto")
    # print(pagos_tickets[1])
    # print("Camion")
    # print(pagos_tickets[2])


def calcular_monto(ticket):
    pais = paises[(detectar_pais_por_patente(ticket.patente))]
    if pais == "Bolivia":
        monto = 200
    elif pais == "Brasil":
        monto = 400
    else:
        monto = 300

    if ticket.pago == 1 and ticket.vehiculo == 0:
        monto = monto / 2
    if ticket.pago == 1 and ticket.vehiculo == 1:
        monto = monto
    if ticket.pago == 1 and ticket.vehiculo == 2:
        monto = monto + ((monto * 60) / 100)
    if ticket.pago == 2 and ticket.vehiculo == 0:
        monto = (monto / 2) - ((10 * (monto / 2)) / 100)
    if ticket.pago == 2 and ticket.vehiculo == 1:
        monto = monto - ((10 * monto) / 100)
    if ticket.pago == 2 and ticket.vehiculo == 2:
        monto = (
            monto + ((monto * 60) / 100) - (((monto + ((monto * 60) / 100)) * 10) / 100)
        )

    return monto


def op8(v):
    pagos_tickets = op7(v)
    total = pagos_tickets[0] + pagos_tickets[1] + pagos_tickets[2]
    if pagos_tickets[0] > pagos_tickets[1] and pagos_tickets[0] > pagos_tickets[2]:
        print("Las motos tienen mayor monto acumulado")
        print("Porcentaje de las motos sobre el total: ")
        print(int((pagos_tickets[0] / total) * 100), "%")
    elif pagos_tickets[1] > pagos_tickets[2]:
        print("Los autos tienen mayor monto acumulado")
        print("Porcentaje de los autos sobre el total: ")
        print(int((pagos_tickets[1] / total) * 100), "%")
    else:
        print("Los camiones tienen mayor monto acumulado")
        print("Porcentaje de los camiones sobre el total: ")
        print(int((pagos_tickets[2] / total) * 100), "%")


def op9(v):
    pass