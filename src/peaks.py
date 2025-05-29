import pandas as pd

def leer_archivo_picos(peaks_path):
    """
    Lee un archivo .tsv con información de picos de unión y devuelve una lista de diccionarios.
    Cada diccionario contiene: TF_name, start, end.
    """
    try:
        df = pd.read_csv(peaks_path, sep='\t', usecols=[2, 3, 4], names=["TF_name", "start", "end"], header=0)
        
        # Convertir columnas a tipo numérico seguro
        df["start"] = pd.to_numeric(df["start"], errors="coerce").astype("Int64")
        df["end"] = pd.to_numeric(df["end"], errors="coerce").astype("Int64")
        
        # Eliminar filas con valores faltantes
        df = df.dropna(subset=["TF_name", "start", "end"])
        
        # Convertir a lista de diccionarios
        return df.to_dict(orient="records")

    except Exception as e:
        print(f"Error al leer el archivo de picos: {e}")
        return []
