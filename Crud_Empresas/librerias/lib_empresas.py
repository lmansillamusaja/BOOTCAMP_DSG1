def mostrar_menu(ancho):
    print("="*ancho)
    print(" " * 10 + "CRUD DE EMPRESAS")
    print("="*ancho)
    print("""
         [1] REGISTRAR EMPRESA
         [2] MOSTRAR EMPRESA
         [3] ACTUALIZAR EMPRESA
         [4] ELIMINAR EMPRESA
         [5] SALIR
          """)
    print("="*ancho)

def buscar_empresa(valor_busqueda,lista_empresas):
    posicion_busqueda = -1
    for posicion in range(len(lista_empresas)):
        dic_empresas = lista_empresas[posicion]
        if valor_busqueda in dic_empresas.values():
            posicion_busqueda = posicion
            break
    return posicion_busqueda

def cargar_datos(str_datos):
    lista_empresas = []
    lista_general = str_datos.splitlines()
    for str_registro in lista_general:
        lista_registro = str_registro.split(',')
        dic_registro = {
        'ruc':lista_registro[0],
        'razon_social':lista_registro[1],
        'direccion':lista_registro[2]
        }
        lista_empresas.append(dic_registro)
    return lista_empresas

def grabar_datos(lista_empresas):
    str_empresas = ""
    for dic_registro in lista_empresas:
        for clave,valor in dic_registro.items():
            str_empresas += valor
            if clave != 'celular':
                str_empresas += ','
            else:
                str_empresas += '\n'
    
    return str_empresas

