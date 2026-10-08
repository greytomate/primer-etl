from database import engine
import pandas as pd


df = pd.read_sql("SELECT * FROM ventas", engine)

print("Datos cargados en PostgreSQL:")
print(df)