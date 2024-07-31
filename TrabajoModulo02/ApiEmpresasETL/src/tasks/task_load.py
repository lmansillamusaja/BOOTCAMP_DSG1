import mysql.connector
from config import Config
from prefect import task

config = Config()

conn = mysql.connector.connect(
            user=config.mysql_user,
            password=config.mysql_password,
            host=config.mysql_host,
            database=config.mysql_database,
            port=config.mysql_port
        )


@task(name='carga de info en bd')
def task_load_empresas(empresas):
    try:
        cursor = conn.cursor()

        query_drop = "drop table if exists tbl_empresas"
        cursor.execute(query_drop)
        conn.commit()

        query_table = """
        create table if not exists tbl_empresas(
        id INT AUTO_INCREMENT PRIMARY KEY,
        ruc VARCHAR(20),
        direccion VARCHAR(255),
        razon_social VARCHAR(255),
        monto VARCHAR(20),
        fecha_creacion DATETIME default CURRENT_TIMESTAMP)
        """
        cursor.execute(query_table)
        conn.commit()

        query_insert = """
        insert into tbl_empresas(ruc,direccion,razon_social,monto)
        values(%s,%s,%s,%s)
        """

        for empresa in empresas:
            cursor.execute(query_insert,empresa)

        conn.commit()
        cursor.close()
        conn.close()
        print('datos guardados en bd...')

    except mysql.connector.Error as err:
        print(err)