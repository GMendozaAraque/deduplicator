import subprocess
import sys

def main():
    if len(sys.argv) != 3:
        print("Uso: python pipeline.py <archivo_entrada_business> <archivo_salida_clean>")
        sys.exit(1)

    business_input = sys.argv[1]
    clean_output = sys.argv[2]
    # Archivo intermedio generado por deduplicate_business.py
    intermediate_file = "intermediate.xlsx"

    # Ejecutar deduplicate_business.py
    print("Ejecutando deduplicate_business.py...")
    subprocess.run(["python", "deduplicate_business.py", business_input, intermediate_file], check=True)

    # Ejecutar deduplicate_phone.py con el archivo intermedio
    print("Ejecutando deduplicate_phone.py...")
    subprocess.run(["python", "deduplicate_phone.py", intermediate_file, clean_output], check=True)

    print(f"Proceso completado. Archivo final: {clean_output}")

if __name__ == "__main__":
    main()
