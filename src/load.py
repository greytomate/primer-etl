from sqlalchemy import MetaData, Table
from sqlalchemy.dialects.postgresql import insert
from database import engine


def cargar_ventas(df):
    if df.empty:
        print("No hay ventas para cargar.")
        return 0

    # Obtener la estructura existente de la tabla
    metadata = MetaData()
    ventas = Table("ventas", metadata, autoload_with=engine)

    # Convertir el DataFrame en registros
    registros = df.to_dict(orient="records")

    # Preparar la inserción de registros
    sentencia = insert(ventas).values(registros)

    # Actualizar las columnas si la venta ya existe
    columnas_actualizables = {
        columna.name: getattr(sentencia.excluded, columna.name)
        for columna in ventas.columns
        if columna.name != "id_venta"
    }

    sentencia = sentencia.on_conflict_do_update(
        index_elements=["id_venta"],
        set_=columnas_actualizables
    )

    # Ejecutar la carga dentro de una transacción
    with engine.begin() as conexion:
        conexion.execute(sentencia)

    return len(registros)