from sqlalchemy import text
from database import engine


consulta = text("""
    SELECT
        constraint_name,
        constraint_type
    FROM information_schema.table_constraints
    WHERE table_name = 'ventas'
      AND constraint_type = 'PRIMARY KEY';
""")


with engine.connect() as conexion:
    resultado = conexion.execute(consulta)

    for fila in resultado:
        print(f"Restricción: {fila[0]}")
        print(f"Tipo: {fila[1]}")