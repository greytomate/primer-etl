from extract import extraer_ventas
from transform import transformar_ventas
from load import cargar_ventas
import logging


# Configuración del sistema de logs
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("logs/etl.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


def ejecutar_etl():
    logger.info("Iniciando ETL...")

    # 1. Extraer
    df = extraer_ventas()
    logger.info(f"Registros extraídos: {len(df)}")

    # 2. Transformar
    df_transformado = transformar_ventas(df)
    logger.info(f"Registros transformados: {len(df_transformado)}")

    # 3. Cargar
    cargar_ventas(df_transformado)
    logger.info(f"Registros cargados: {len(df_transformado)}")


if __name__ == "__main__":
    try:
        ejecutar_etl()
        logger.info("ETL ejecutado correctamente.")

    except Exception as e:
        logger.error(f"Error durante el ETL: {e}")