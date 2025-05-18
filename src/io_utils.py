import os

def guardar_fasta_por_tf(secuencias_por_tf, output_dir):
    """
    Guarda archivos FASTA separados por cada TF_name.
    Cada archivo contiene las secuencias correspondientes al TF.
    """
    os.makedirs(output_dir, exist_ok=True)
    for tf, entradas in secuencias_por_tf.items():
        archivo_salida = os.path.join(output_dir, f"{tf}.fasta")
        with open(archivo_salida, 'w') as f:
            for header, secuencia in entradas:
                f.write(f"{header}\n{secuencia}\n")
