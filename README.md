# Instructivo de Instalación y Uso

Este proyecto contiene dos scripts para eliminar duplicados en archivos de datos (CSV o Excel).  
- **deduplicate_phone.py:** Elimina registros duplicados basándose en la columna "Phone Number".  
- **deduplicate_business.py:** Elimina registros duplicados basándose en la columna "Business Name".

## Requisitos Previos

- Tener instalado [Python 3](https://www.python.org/downloads/).
- Visual Studio Code instalado (se usará la terminal integrada de VS Code).

## Instalación de Dependencias

1. **Abrir VS Code y cargar la carpeta del proyecto:**
   - Abre VS Code y selecciona `Archivo > Abrir Carpeta...` para elegir la carpeta donde se encuentra el proyecto.

2. **Abrir la Terminal Integrada:**
   - Ve a `Terminal > Nueva Terminal` para abrir la terminal de VS Code.

3. **Instalar las dependencias:**
   - Ejecuta el siguiente comando para instalar todo lo necesario:
     ```bash
     sh install_dependencies.sh
     ```
   - Alternativamente, puedes usar directamente:
     ```bash
     pip install -r requirements.txt
     ```

## Uso de los Scripts de Deduplicación

### 1. Deduplicación completa
- **Comando:**
  ```bash
  python pipeline.py <archivo_entrada> <archivo_salida>

### 2. Deduplicación por "Phone Number"
- **Comando:**
  ```bash
  python deduplicate_phone.py <archivo_entrada> <archivo_salida>


### 3. Deduplicación por "Business Name"
- **Comando:**
  ```bash
  python deduplicate_business.py <archivo_entrada> <archivo_salida>