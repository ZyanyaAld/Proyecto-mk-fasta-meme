def cargar_genoma(fasta_path):
    """
    Carga el genoma desde un archivo txt y devuelve una única cadena de texto en mayúsculas.
    """
    with open(fasta_path, 'r') as f:
        lineas = f.readlines()
    secuencia = ''.join([line.strip() for line in lineas if not line.startswith('>')])
    return secuencia.upper()
