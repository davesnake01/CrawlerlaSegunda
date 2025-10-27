import time
import pyodbc
from datetime import datetime, timedelta

def inserttoDatabase(titulo, texto, link , fecha, id_diario, fotourl):
    # con_string = (
    #     # El driver lo obtuve del panel de control de ODBC en windows
    #     r'DRIVER={ODBC Driver 17 for SQL Server};'
    #     r'SERVER=192.168.2.5;'
    #     r'DATABASE=RobotChile;'
    #     r'UID=sa;'
    #     r'PWD='';'
    # )
    fecha_lectura = datetime.now()
    print("Fecha Lectura:", fecha_lectura)

    dsn = 'sqlserverdatasource'
    user = 'sa'
    password = ''
    database = 'RobotChile'
    con_string = 'DSN=%s;UID=%s;PWD=%s;DATABASE=%s;' % (dsn, user, password, database)

    cnxn = pyodbc.connect(con_string)
    #print(con_string, cnxn)
    cursor = cnxn.cursor()


    try:

        storedProc = "Exec [dbo].[InsertFulltext] @leido = 0, @titular = ?, @link = ?," \
                     " @id_pais = 1, @nota = ?, @foto = ?, @fecha = ?,  @id_diario = ?, @fecha_lectura =?, @autor = ''"
        params = (titulo, link, texto,fotourl,fecha, id_diario, fecha_lectura)
        print(titulo, link, id_diario, sep="\n")

        cursor.execute(storedProc, params)
        cursor.commit()


        return 1
    except Exception as ex:
        print("=======> REGISTRO ERRONEO")
        print(ex)
        time.sleep(10)