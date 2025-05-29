# Proyecto de Automatización para la Identificación de Sitios de Unión de Factores de Transcripción en E. coli en experimentos de ChIP-Seq

Autor: Zyanya Valentina Velazquez Aldrete
Version:3

## Resumen

Este proyecto tiene como objetivo automatizar el proceso de identificación del sitio exacto de unión de los reguladores transcripcionales para 144 factores de transcripción (TFs) en el genoma completo de *Escherichia coli*. Las regiones de unión de estos TFs se han determinado mediante la técnica ChIP-seq.


### Genoma Completo de E. coli
Disponible en formato FASTA.

Archivo: E_coli_K12_MG1655_U00096.3.txt

## Archivo con codigo completo

El archivo que posee nuestro codigo completo, se ejecuta desde la raiz del proyecto:

python src/extract_fasta.py

### 📁 Modularización del Extractor de Secuencias

Como parte del avance del proyecto, el script original `extract_fasta.py` fue refactorizado y modularizado para mejorar su organización, reutilización y mantenibilidad. Esta nueva versión se ejecuta desde un archivo principal (`main.py`) y se apoya en módulos especializados.

####  Estructura del código modular

extractor_secuencias/
├── src/
│   ├── main.py          # Punto de entrada del programa
│   ├── genome.py        # Lectura del genoma desde archivo
│   ├── peaks.py         # Procesamiento del archivo de picos
│   └── io_utils.py      # Escritura de archivos FASTA por TF
├── data/
│   ├── E_coli_genome.fasta
│   └── tf_peaks.txt
└── results/
    └── output_estrucmodul/

#### Ejecución

Para extraer las secuencias, ejecutar desde la raíz del proyecto:

python src/main.py

También es posible especificar parámetros personalizados:

python src/main.py \
  -g data/E_coli_genome.fasta \
  -p data/tf_peaks.txt \
  -o results/output_estrucmodul \
  --tf LexA

#### 📤 Salida

Los archivos generados se guardan en el directorio `results/output_estrucmodul/`, uno por cada factor de transcripción (TF) encontrado en el archivo de picos.
