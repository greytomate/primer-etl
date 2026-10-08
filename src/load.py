from database import engine


def cargar_ventas(df):
    df.to_sql(
        "ventas",
        engine,
        if_exists="replace",
        index=False
    )


