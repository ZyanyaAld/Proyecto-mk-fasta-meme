import os
import argparse
import time

"""
extract_fasta.py

Este script extrae secuencias FASTA del genoma de *E. coli* con base en coordenadas
de picos de unión para diferentes factores de transcripción (TF).

Requiere: 
1. El genoma de E. coli en formato txt.
2. Un archivo .tsv con columnas como: TF_name, Peak_start, Peak_end

Salida:
Archivos FASTA por cada TF con las secuencias extraídas.

"""

def cargar_genoma(fasta_path):
    """Carga el genoma desde un archivo txt y devuelve una única cadena de texto."""
    with open(fasta_path, 'r') as f:
        lineas = f.readlines()
    secuencia = ''.join([line.strip() for line in lineas if not line.startswith('>')])
    return secuencia.upper()

def leer_archivo_picos(peaks_path):
    datos = []
    with open(peaks_path, 'r', encoding='utf-8') as f:
        next(f)  # Saltar encabezado
        for i, linea in enumerate(f, start=2):
            partes = linea.strip().split('\t')
            try:
                tf_name = partes[2]  # columna 3
                start = int(float(partes[3]))  # columna 4
                end = int(float(partes[4]))    # columna 5
                datos.append({'TF_name': tf_name, 'start': start, 'end': end})
            except (ValueError, IndexError) as e:
                print(f"[Línea {i}] Error: {e} → {linea.strip()}")
    return datos


def extraer_secuencias(peaks_data, genoma):
    """Agrupa las secuencias extraídas por TF_name en un diccionario."""
    secuencias_por_tf = {}
    for entrada in peaks_data:
        tf = entrada['TF_name']
        start = entrada['start']
        end = entrada['end']
        if start < 0 or end > len(genoma) or start >= end:
            print(f"Coordenadas inválidas: {entrada}")
            continue
        secuencia = genoma[start:end]
        if tf not in secuencias_por_tf:
            secuencias_por_tf[tf] = []
        header = f">{tf}_{start}_{end}"
        secuencias_por_tf[tf].append((header, secuencia))
    return secuencias_por_tf

def guardar_fasta_por_tf(secuencias_por_tf, output_dir):
    """Guarda archivos FASTA separados por cada TF_name."""
    os.makedirs(output_dir, exist_ok=True)
    for tf, entradas in secuencias_por_tf.items():
        archivo_salida = os.path.join(output_dir, f"{tf}.fasta")
        with open(archivo_salida, 'w') as f:
            for header, secuencia in entradas:
                f.write(f"{header}\n{secuencia}\n")

def main():
    parser = argparse.ArgumentParser(description="Extrae secuencias FASTA a partir de coordenadas.")
    parser.add_argument(
        '-g', '--genome',
        default='data/E_coli_K12_MG1655_U00096.3.txt',
        help='Archivo FASTA del genoma de E. coli (por defecto: data/E_coli_K12_MG1655_U00096.3.txt).'
    )
    parser.add_argument(
        '-p', '--peaks',
        default='data/union_peaks_file.tsv',
        help='Archivo .tsv con picos de unión (por defecto: data/union_peaks_file.tsv).'
    )
    parser.add_argument(
        '-o', '--output',
        default='results/salidas_fasta',
        help='Directorio de salida (por defecto: results/salidas_fasta/).'
    )
    parser.add_argument(
        '--tf',
        help='Nombre de un solo factor de transcripción (TF) a extraer (opcional).'
    )

    args = parser.parse_args()
    start_time = time.time()

    print("Cargando genoma...")
    genoma = cargar_genoma(args.genome)

    print("Leyendo archivo de picos...")
    datos_picos = leer_archivo_picos(args.peaks)

    print("Extrayendo secuencias...")
    secuencias = extraer_secuencias(datos_picos, genoma)

    # Filtrar por TF si se especifica
    if args.tf:
        tf_buscado = args.tf.strip()
        if tf_buscado in secuencias:
            secuencias = {tf_buscado: secuencias[tf_buscado]}
            print(f"Extrayendo solo para TF: {tf_buscado}")
        else:
            print(f"No se encontró el TF '{tf_buscado}' en los datos.")
            print("TFs disponibles:", ', '.join(secuencias.keys()))
            return

    print(f"Guardando archivos en: {args.output}/")
    guardar_fasta_por_tf(secuencias, args.output)

    print(f"Proceso completado en {time.time() - start_time:.2f} segundos.")


if __name__ == "__main__":
    main()


