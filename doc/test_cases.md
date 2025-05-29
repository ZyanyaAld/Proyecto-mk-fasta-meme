# Casos de Prueba


### Caso 1: Archivo del genoma no se encuentra
- **Entradas**:
  - Ruta incorrecta o inexistente para el archivo FASTA del genoma
  - Archivo de picos válido
  - Directorio de salida
- **Esperado**:
  - `Error: Genome file not found`
- **Comando**:
  ```bash
  mk_fasta_from_peaks.py -i peak_file.txt -g Ecoli.fna -o fasta_peaks/
  ```

---

### Caso 2: Archivo de picos vacío
- **Entradas**:
  - Archivo de picos vacío
  - Archivo FASTA del genoma
  - Directorio de salida
- **Esperado**:
  - `Error: the peak file is empty`

---

### Caso 3: Posiciones fuera del rango del genoma
- **Entradas**:
  - Archivo de picos con picos fuera del tamaño del genoma
  - FASTA válido
- **Esperado**:
  - `Warning: Some peaks are bigger than the genome. Check the log.out file`
  - Se ignoran picos fuera de rango
  - Se crea `log.out`

---

### Caso 4: Coordenadas incompletas
- **Entradas**:
  - Archivo de picos con filas incompletas
  - FASTA válido
- **Esperado**:
  - `Error: Incomplete peak coordinates in the peak file. Check the log.out file`
  - Se ignoran filas incompletas
  - Se registra error en `log.out`

---

### Caso 5: Valores no numéricos en coordenadas
- **Entradas**:
  - Archivo de picos con valores no numéricos
- **Esperado**:
  - `Error: Non-numeric values in Peak_start or Peak_end.`
  - Se ignoran esas filas
  - Se registra en `log.out`

---
### Caso 6: Archivo de picos mal formateado
- *Entradas*:
  - Archivo con columnas faltantes
- *Esperado*:
  - Error: Invalid peak file format. Missing required columns.
  - No se generan archivos

---

### Caso 7: Archivo de genoma mal formateado
- *Entradas*:
  - FASTA inválido
- *Esperado*:
  - Error: Invalid genome file format. Missing required columns.


### Caso 8: Directorio de salida no existe
- **Entradas**:
  - Archivo de picos y genoma válidos
  - Directorio de salida inexistente
- **Esperado**:
  - Directorio creado automáticamente
  - Mensaje: `Directory "fasta_peaks/" created successfully.`
  - Log en `log.out`
