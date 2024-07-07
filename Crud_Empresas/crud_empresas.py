import os
import tabulate
import time
from librerias.lib_empresas import buscar_empresa,mostrar_menu,cargar_datos,grabar_datos

f = open('empresas.txt','r')
str_empresas = f.read()
f.close()

lista_empresas = cargar_datos(str_empresas)
ANCHO = 50
opcion = 0


while(opcion < 5):
    os.system("clear")
    mostrar_menu(ANCHO)
    opcion = int(input("INGRESE OPCION : "))
    os.system("clear")
    if(opcion == 1):
        print("="*ANCHO)
        print(" " * 10 + "[1] REGISTRAR EMPRESA")
        print("="*ANCHO)
        ruc = input("RUC : ")
        razon_social = input("Razon Social : ")
        direccion = input("Direccion : ")
        dic_nuevo_empresa = {
            'ruc':ruc,
            'razon_social':razon_social,
            'direccion':direccion
        }
        lista_empresas.append(dic_nuevo_empresa)
        print(" EMPRESA REGISTRADO CON EXITO")
    elif(opcion == 2):
        print("="*ANCHO)
        print(" " * 10 + "[2] MOSTRAR EMPRESAS")
        print("="*ANCHO)
        cabeceras = ["RUC","RAZON SOCIAL","DIRECCION"]
        tabla = [empresa.values() for empresa in lista_empresas]
        print(tabulate.tabulate(tabla,headers=cabeceras,tablefmt="grid"))
        input("presione ENTER para continuar...")
        
        
    elif(opcion == 3):
        print("="*ANCHO)
        print(" " * 10 + "[3] ACTUALIZAR EMPRESA")
        print("="*ANCHO)
        valor_busqueda = input('INGRESE RUC DEL EMPRESA A ACTUALIZAR :')
        posicion_busqueda = buscar_empresa(valor_busqueda,lista_empresas)
        if posicion_busqueda == -1:
            print("NO SE ENCONTRO LA EMPRESA SOLICITADO")
        else:
            print(f' EMPRESA A ACTUALIZAR : {lista_empresas[posicion_busqueda].get("ruc")}')
            nuevo_ruc = input("RUC : ")
            nuevo_razon_social = input("RAZON SOCIAL : ")
            nuevo_direccion = input("DIRECCION : ")
            dic_actualizar_empresa = {
                'ruc':nuevo_ruc,
                'razon_social':nuevo_razon_social,
                'direccion':nuevo_direccion
            }
            lista_empresas[posicion_busqueda] = dic_actualizar_empresa
            print("EMPRESA ACTUALIZADO CON EXITO...")
        
    elif(opcion == 4):
        print("="*ANCHO)
        print(" " * 10 + "[4] ELIMINAR EMPRESA")
        print("="*ANCHO)
        valor_busqueda = input('INGRESE RUC DEL EMPRESA A ELIMINAR :')
        posicion_busqueda = buscar_empresa(valor_busqueda,lista_empresas)
        if posicion_busqueda == -1:
            print("NO SE ENCONTRO EL EMPRESA SOLICITADO")
        else:
            lista_empresas.pop(posicion_busqueda)
            print('EMPRESA ELIMINADO!!!')
        
    elif(opcion == 5):
        print("="*ANCHO)
        print(" " * 10 + "[5] SALIR")
        str_alumnos = grabar_datos(lista_empresas)
        fsalida = open('empresas.txt','w')
        fsalida.write(str_alumnos)
        fsalida.close()
        print("="*ANCHO)
        
    else:
        print("="*ANCHO)
        print(" " * 10 + "OPCIÓN INVALIDA!!!")
        print("="*ANCHO)
        
    time.sleep(1)