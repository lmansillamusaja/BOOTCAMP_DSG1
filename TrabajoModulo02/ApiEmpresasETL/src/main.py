from prefect import flow
from tasks.task_extract import(
    task_extract_ruc,
    task_extract_csv
)
from tasks.task_load import (
    task_load_empresas
)

PATH_CSV = './resources/empresas.csv'


@flow(name='ETL APIPERU')
def main_flow():
    lista_empresas = task_extract_csv(PATH_CSV)
    #print(lista_empresas)
    lista_empresas_completa = task_extract_ruc(lista_empresas)
    #print(lista_alumnos_completa)
    task_load_empresas(lista_empresas_completa)
    

if __name__ == '__main__':
    main_flow()