import os

# Obtener el directorio actual
directorio_actual = os.getcwd()
print(f"Directorio actual: {directorio_actual}")

# Crear un directorio llamado Datos_PXM
nuevo_directorio = os.path.join(directorio_actual, "Datos_PXM")
os.makedirs(nuevo_directorio, exist_ok=True)
print(f"Directorio creado: {nuevo_directorio}")

bitacora = "Inicia proceso"
bitacora += "\n Inicia etapa 1"
bitacora += "\n Inicia etapa 2"
bitacora += "\n Inicia etapa 3"
bitacora += "\n Inicia etapa final"

print(bitacora)
