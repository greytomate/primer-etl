from sqlalchemy import text
from database import engine


consulta = text("""
    SELECT
        COUNT(*) AS total_filas,
        COUNT(DISTINCT id_venta) AS ventas_unicas
    FROM ventas;
""")


with engine.connect() as conexion:
    resultado = conexion.execute(consulta).fetchone()

    print(f"Total de filas: {resultado[0]}")
    print(f"Ventas únicas: {resultado[1]}")


consulta_clave = text("""
    SELECT COUNT(*)
    FROM information_schema.table_constraints
    WHERE table_name = 'ventas'
      AND constraint_name = 'pk_ventas'
      AND constraint_type = 'PRIMARY KEY';
""")


with engine.connect() as conexion:
    clave_primaria = conexion.execute(consulta_clave).scalar()

    print(f"Clave primaria configurada: {'Sí' if clave_primaria == 1 else 'No'}")

print("\n--- Venta antes de la prueba ---")

consulta_venta = text("""
    SELECT id_venta, producto, cantidad, precio_unitario, total_venta
    FROM ventas
    WHERE id_venta = 1;
""")

with engine.connect() as conexion:
    venta = conexion.execute(consulta_venta).fetchone()

    if venta:
        print(venta)
    else:
        print("No se encontró la venta.")
