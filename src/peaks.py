def leer_archivo_picos(peaks_path):
    """
    Lee un archivo .tsv con información de picos de unión y devuelve una lista de diccionarios.
    Cada diccionario contiene: TF_name, start, end.
    """
    datos = []
    with open(peaks_path, 'r', encoding='utf-8') as f:
        next(f)  # Saltar encabezado
        for i, linea in enumerate(f, start=2):
            partes = linea.strip().split('\t')
            try:
                tf_name = partes[2]
                start = int(float(partes[3]))
                end = int(float(partes[4]))
                datos.append({'TF_name': tf_name, 'start': start, 'end': end})
            except (ValueError, IndexError) as e:
                print(f"[Línea {i}] Error: {e} → {linea.strip()}")
    return datos
