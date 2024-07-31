import requests
from prefect import task
from config import Config
import csv

config = Config()


@task(name='extraer info de csv')
def task_extract_csv(file_csv):
    with open(file_csv,mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        lista_csv = []
        for row in csv_reader:
            tupla_csv = (row['ruc'],row['monto'])
            lista_csv.append(tupla_csv)
    
    return lista_csv

@task(name="Extraer info de ruc")
def task_extract_ruc(lista_empresas):
    lista_empresas_completa = []
    for tupla_empresa in lista_empresas:
        ruc = tupla_empresa[0]
        monto = tupla_empresa[1]

        print("Ruc :",ruc)

        data_request = {
            "ruc": ruc 
        }

        headers_request = {
            "Authorization": "Bearer " + config.api_token,
            "Content-Type": "application/json"
        }
        response = requests.post(config.api_url_dni,
                                json=data_request,
                                headers=headers_request)
        
        if response.status_code == 200:
            response_empresas = response.json()
            if response_empresas['success'] == True:
                
                data_empresas = response_empresas['data']
                tupla_empresa_completo = (data_empresas['ruc'],
                                    data_empresas['direccion'],
                                    data_empresas['nombre_o_razon_social'],
                                    monto)
                lista_empresas_completa.append(tupla_empresa_completo)
            else:
                print("ERROR AL CONECTARSE AL API : ",response_empresas['message'])
        else:
            print(f"error : {response.status_code}")

    return lista_empresas_completa