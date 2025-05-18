# src/extract_fasta.py
"""
Funciones para extraer secuencias FASTA a partir de coordenadas
y agruparlas por factor de transcripción (TF).
"""

def extraer_secuencias(peaks_data, genoma):
    """
    Recorre la lista `peaks_data` (diccionarios con claves
    'TF_name', 'start', 'end') y devuelve un diccionario:

        { tf_name: [(header, secuencia), ...], ... }

    * Valida que start/end estén dentro de rango.
    * Omite entradas inválidas y muestra un aviso.
    """
    secuencias_por_tf = {}

    for entrada in peaks_data:
        tf     = entrada["TF_name"]
        start  = entrada["start"]
        end    = entrada["end"]

        if start < 0 or end > len(genoma) or start >= end:
            print(f"Coordenadas inválidas: {entrada}")
            continue

        secuencia = genoma[start:end]
        header    = f">{tf}_{start}_{end}"

        # inicializa la lista si es la primera vez que vemos este TF
        secuencias_por_tf.setdefault(tf, [])
        secuencias_por_tf[tf].append((header, secuencia))

    return secuencias_por_tf
