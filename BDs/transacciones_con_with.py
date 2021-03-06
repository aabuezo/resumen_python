# TRANSACCIONES
# ejemplo sin with porque hace commit automaticamente
import psycopg2 as bd


conexion = bd.connect(
    user='usuario',
    password='password',
    host='localhost',
    port='5432',
    database='test_db'
)

try:
    with conexion:
        with conexion.cursor() as cursor:

            sentencia = 'INSERT INTO personas(nombre, apellido, email) VALUES(%s, %s, %s)'
            valores = ('Alex', 'Rojas', 'arojas@mail.com')  # error...
            cursor.execute(sentencia, valores)

            sentencia = 'UPDATE personas SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
            valores = ('Juan', 'Perez', 'jperez@mail.com', 1)
            cursor.execute(sentencia, valores)

except Exception as e:
    print(f'Ocurrio un error: {e}')
    print('Se realizo rollback de la transaccion.')
finally:
    conexion.close()

print('Termina la transaccion, se hizo commit')