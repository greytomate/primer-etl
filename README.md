ETL de ventas con Python y PostgreSQL
Descripción

Este proyecto implementa un proceso ETL (Extract, Transform, Load) para procesar datos de ventas desde un archivo CSV, aplicar transformaciones y validaciones de calidad, y cargar los resultados en una base de datos PostgreSQL.

El objetivo es practicar conceptos fundamentales de ingeniería de datos mediante un pipeline reproducible, modular y con registro de eventos.

Arquitectura del proyecto

El proceso sigue estas etapas:

Extracción: lectura de los datos desde datos/ventas.csv.
Transformación: cálculo del valor total de cada venta y validación de los datos.
Carga: almacenamiento de los resultados en PostgreSQL.
Monitoreo: registro de las etapas y los errores mediante logs.
Tecnologías utilizadas
Python
Pandas
SQLAlchemy
PostgreSQL
psycopg2
python-dotenv
Git
Validaciones implementadas
Verificación de valores vacíos en total_venta.
Validación de cantidades mayores que cero.
Validación de precios unitarios mayores que cero.
Estructura del proyecto
primer-etl/
├── datos/
│   └── ventas.csv
├── logs/
│   └── etl.log
├── src/
│   ├── database.py
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── etl.py
│   └── verificar_carga.py
├── .env
├── .gitignore
├── README.md
└── requirements.txt
Configuración y ejecución
1. Instalar las dependencias
pip install -r requirements.txt
2. Configurar las variables de entorno

Crear un archivo .env en la raíz del proyecto con las credenciales de PostgreSQL:

DB_USER=postgres
DB_PASSWORD=tu_contraseña
DB_HOST=localhost
DB_PORT=5433
DB_NAME=postgres

Reemplazar tu_contraseña por la contraseña local correspondiente. No publicar este archivo ni compartir credenciales reales.

3. Ejecutar el ETL

Desde la carpeta raíz del proyecto:

python src/etl.py

El proceso registra información sobre los registros extraídos, transformados y cargados. Los mensajes se muestran en la terminal y se guardan en el archivo de log.

Próximas mejoras
Implementar una estrategia de carga incremental.
Añadir validaciones adicionales de calidad de datos.
Mejorar el manejo de errores y las pruebas automatizadas.
Crear consultas analíticas y un dashboard en Power BI.
Autor

Proyecto personal de aprendizaje en ingeniería de datos.