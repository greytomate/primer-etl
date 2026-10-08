import pandas as pd


def transformar_ventas(df):
    df = df.copy()

    df["total_venta"] = (
        df["cantidad"] * df["precio_unitario"]
    )

    # Validar que no existan valores vacíos en total_venta
    if df["total_venta"].isnull().any():
        raise ValueError(
            "Error: existen valores vacíos en total_venta."
        )
    if (df["cantidad"] <= 0).any():
        raise ValueError(
        "Error: existen cantidades menores o iguales a cero."
    )

    if (df["precio_unitario"] <= 0).any():
        raise ValueError(
        "Error: existen precios menores o iguales a cero."
    )


    return df


if __name__ == "__main__":
    from extract import extraer_ventas

    df = extraer_ventas()
    df_transformado = transformar_ventas(df)

    print("Datos transformados correctamente.")
    print(df_transformado)