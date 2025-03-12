import os
from datetime import datetime

# Obtener el directorio actual
directorio_actual = os.getcwd()
print(f"Directorio actual: {directorio_actual}")

# Crear un directorio llamado Datos_PXM
nuevo_directorio = os.path.join(directorio_actual, "Datos_PXM")
os.makedirs(nuevo_directorio, exist_ok=True)
print(f"Directorio creado: {nuevo_directorio}")

# Crear una nueva carpeta con la fecha del día actual dentro de Datos_PXM
fecha_actual = datetime.now().strftime("%Y%m%d")
directorio_fecha = os.path.join(nuevo_directorio, fecha_actual)
os.makedirs(directorio_fecha, exist_ok=True)
print(f"Directorio con fecha creado: {directorio_fecha}")

bitacora = "Inicia proceso"
bitacora += "\n Inicia etapa 1"
bitacora += "\n Inicia etapa 2"
bitacora += "\n Inicia etapa 3"
bitacora += "\n Inicia etapa final"

print(bitacora)
