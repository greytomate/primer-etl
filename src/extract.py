import pandas as pd
from pathlib import Path


def extraer_ventas():
    ruta = Path(__file__).parent.parent / "datos" / "ventas.csv"

    df = pd.read_csv(ruta)

    return df


if __name__ == "__main__":
    df = extraer_ventas()

    print("Datos extraídos correctamente.")
    print(df)