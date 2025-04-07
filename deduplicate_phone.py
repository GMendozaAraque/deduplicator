import pandas as pd
import sys

def deduplicate_file(input_file, output_file):
    # Leer el archivo según su extensión
    if input_file.lower().endswith('.csv'):
        df = pd.read_csv(input_file)
    elif input_file.lower().endswith(('.xls', '.xlsx')):
        df = pd.read_excel(input_file)
    else:
        print("Formato no soportado. Por favor, usa un archivo CSV o Excel.")
        return

    # Eliminar duplicados basándose en "Phone Number"
    df_dedup = df.drop_duplicates(subset=['Phone Number'], keep='first')

    # Guardar el resultado en el mismo formato que el archivo de entrada
    if output_file.lower().endswith('.csv'):
        df_dedup.to_csv(output_file, index=False)
    elif output_file.lower().endswith(('.xls', '.xlsx')):
        df_dedup.to_excel(output_file, index=False)
    else:
        print("Formato de salida no soportado. Por favor, usa CSV o Excel.")
        return

    print(f"Datos deduplicados guardados en: {output_file}")

if __name__ == "__main__":
    # Uso: python deduplicate.py input_file output_file
    if len(sys.argv) != 3:
        print("Uso: python deduplicate.py <archivo_entrada> <archivo_salida>")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        deduplicate_file(input_file, output_file)
