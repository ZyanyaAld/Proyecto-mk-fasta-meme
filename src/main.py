import argparse
import time
from genome import cargar_genoma
from peaks import leer_archivo_picos
from io_utils import guardar_fasta_por_tf

def extraer_secuencias(peaks_data, genoma):
    """
    Agrupa las secuencias extraídas por TF_name en un diccionario con headers.
    """
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

def main():
    parser = argparse.ArgumentParser(description="Extrae secuencias FASTA a partir de coordenadas.")
    parser.add_argument(
        '-g', '--genome',
        default='data/E_coli_K12_MG1655_U00096.3.txt',
        help='Archivo FASTA del genoma de E. coli.'
    )
    parser.add_argument(
        '-p', '--peaks',
        default='data/union_peaks_file.tsv',
        help='Archivo .tsv con picos de unión.'
    )
    parser.add_argument(
        '-o', '--output',
        default='results/output_estrucmodul',
        help='Directorio de salida (por defecto: results/output_estrucmodul/).'
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
