def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Unidades por categoría")
    print("2. Búsqueda de productos por rango de precio")
    print("3. Actualizar precio de producto")
    print("4. Agregar producto")
    print("5. Eliminar producto")
    print("6. Salir")
    print("=====================================")


def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese opción: "))
            if 1 <= opcion <= 6:
                return opcion
            print("Debe seleccionar una opción válida")
        except ValueError:
            print("Debe seleccionar una opción válida")


def unidades_categoria(productos, stock, categoria):
    total = 0

    for codigo in productos:
        if productos[codigo][1].lower() == categoria.lower():
            total += stock[codigo][1]

    print(f"El total de unidades disponibles es: {total}")


def busqueda_precio(productos, stock, p_min, p_max):
    encontrados = []

    for codigo in stock:
        precio = stock[codigo][0]
        unidades = stock[codigo][1]

        if p_min <= precio <= p_max and unidades != 0:
            nombre = productos[codigo][0]
            encontrados.append(f"{nombre}--{codigo}")

    encontrados.sort()

    if len(encontrados) > 0:
        print(f"Los productos encontrados son: {encontrados}")
    else:
        print("No hay productos en ese rango de precios.")


def buscar_codigo(stock, codigo):
    codigo = codigo.upper()

    for clave in stock:
        if clave.upper() == codigo:
            return True

    return False


def actualizar_precio(stock, codigo, nuevo_precio):
    codigo = codigo.upper()

    if buscar_codigo(stock, codigo):
        stock[codigo][0] = nuevo_precio
        return True

    return False


def validar_texto(texto):
    return texto.strip() != ""


def validar_codigo(productos, codigo):
    if codigo.strip() == "":
        return False

    codigo = codigo.upper()

    for clave in productos:
        if clave.upper() == codigo:
            return False

    return True


def validar_peso(peso):
    return peso > 0


def validar_si_no(valor):
    return valor.lower() == "s" or valor.lower() == "n"


def validar_precio(precio):
    return precio > 0


def validar_unidades(unidades):
    return unidades >= 0


def convertir_si_no(valor):
    if valor.lower() == "s":
        return True
    return False


def agregar_producto(
    productos,
    stock,
    codigo,
    nombre,
    categoria,
    marca,
    peso_kg,
    es_importado,
    es_para_cachorro,
    precio,
    unidades
):
    codigo = codigo.upper()

    if buscar_codigo(stock, codigo):
        return False

    productos[codigo] = [
        nombre,
        categoria,
        marca,
        peso_kg,
        es_importado,
        es_para_cachorro
    ]

    stock[codigo] = [precio, unidades]

    return True


def eliminar_producto(productos, stock, codigo):
    codigo = codigo.upper()

    if buscar_codigo(stock, codigo):
        del productos[codigo]
        del stock[codigo]
        return True

    return False


def main():
    productos = {
        "M001": ["Alimento Premium", "comida", "DogPlus", 10, True, False],
        "M002": ["Arena Aglomerante", "higiene", "CatClean", 8, False, False],
        "M003": ["Snack Dental", "snack", "BiteJoy", 1, True, True],
        "M004": ["Shampoo Suave", "higiene", "PetCare", 0.5, False, True],
        "M005": ["Correa Nylon", "accesorio", "WalkPro", 0.3, True, False],
        "M006": ["Cama Mediana", "accesorio", "CozyPet", 2, False, False]
    }

    stock = {
        "M001": [32990, 12],
        "M002": [9990, 0],
        "M003": [5490, 25],
        "M004": [7990, 5],
        "M005": [11990, 7],
        "M006": [24990, 3]
    }

    salir = False

    while not salir:
        mostrar_menu()
        opcion = leer_opcion()

        if opcion == 1:
            categoria = input("Ingrese categoría a consultar: ")
            unidades_categoria(productos, stock, categoria)

        elif opcion == 2:
            datos_validos = False

            while not datos_validos:
                try:
                    p_min = int(input("Ingrese precio mínimo: "))
                    p_max = int(input("Ingrese precio máximo: "))

                    if p_min >= 0 and p_max >= 0 and p_min <= p_max:
                        datos_validos = True
                        busqueda_precio(productos, stock, p_min, p_max)
                    else:
                        print("Debe ingresar valores enteros válidos")

                except ValueError:
                    print("Debe ingresar valores enteros")

        elif opcion == 3:
            continuar = "s"

            while continuar.lower() == "s":
                codigo = input("Ingrese código del producto: ")

                try:
                    nuevo_precio = int(input("Ingrese nuevo precio: "))

                    if nuevo_precio > 0:
                        actualizado = actualizar_precio(stock, codigo, nuevo_precio)

                        if actualizado:
                            print("Precio actualizado")
                        else:
                            print("El código no existe")
                    else:
                        print("El precio debe ser mayor que cero")

                except ValueError:
                    print("Debe ingresar valores enteros")

                continuar = input("¿Desea actualizar otro precio (s/n)?: ")

        elif opcion == 4:
            try:
                codigo = input("Ingrese código del producto: ")
                nombre = input("Ingrese nombre: ")
                categoria = input("Ingrese categoría: ")
                marca = input("Ingrese marca: ")
                peso_kg = float(input("Ingrese peso (kg): "))
                es_importado_texto = input("¿Es importado? (s/n): ")
                es_para_cachorro_texto = input("¿Es para cachorro? (s/n): ")
                precio = int(input("Ingrese precio: "))
                unidades = int(input("Ingrese unidades: "))

                if not validar_codigo(productos, codigo):
                    print("El código no es válido o ya existe")
                elif not validar_texto(nombre):
                    print("El nombre no puede estar vacío")
                elif not validar_texto(categoria):
                    print("La categoría no puede estar vacía")
                elif not validar_texto(marca):
                    print("La marca no puede estar vacía")
                elif not validar_peso(peso_kg):
                    print("El peso debe ser mayor que cero")
                elif not validar_si_no(es_importado_texto):
                    print("Debe ingresar s o n para importado")
                elif not validar_si_no(es_para_cachorro_texto):
                    print("Debe ingresar s o n para cachorro")
                elif not validar_precio(precio):
                    print("El precio debe ser mayor que cero")
                elif not validar_unidades(unidades):
                    print("Las unidades deben ser mayor o igual a cero")
                else:
                    es_importado = convertir_si_no(es_importado_texto)
                    es_para_cachorro = convertir_si_no(es_para_cachorro_texto)

                    agregado = agregar_producto(
                        productos,
                        stock,
                        codigo,
                        nombre,
                        categoria,
                        marca,
                        peso_kg,
                        es_importado,
                        es_para_cachorro,
                        precio,
                        unidades
                    )

                    if agregado:
                        print("Producto agregado")
                    else:
                        print("El código ya existe")

            except ValueError:
                print("Debe ingresar valores numéricos válidos")

        elif opcion == 5:
            codigo = input("Ingrese código del producto a eliminar: ")
            eliminado = eliminar_producto(productos, stock, codigo)

            if eliminado:
                print("Producto eliminado")
            else:
                print("El código no existe")

        elif opcion == 6:
            salir = True
            print("Programa finalizado.")


if __name__ == "__main__":
    main()

# -----------------------------------------
# Evaluación Final Transversal FPY1101
# Sistema de gestión PetMarket
# Autor: Nicolás Ignacio Cares Toro
# -----------------------------------------

