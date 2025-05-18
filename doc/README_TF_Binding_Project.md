# Proyecto de Automatización para la Identificación de Sitios de Unión de Factores de Transcripción en E. coli en experimentos de ChIP-Seq

Autor: Zyanya Valentina Velazquez Aldrete

## Resumen

Este proyecto tiene como objetivo automatizar el proceso de identificación del sitio exacto de unión de los reguladores transcripcionales para 144 factores de transcripción (TFs) en el genoma completo de *Escherichia coli*. Las regiones de unión de estos TFs se han determinado mediante la técnica ChIP-seq.

## Datos Disponibles

### Archivo de Picos
Contiene información sobre las regiones de unión de los 144 factores de transcripción. Se organiza en las siguientes columnas:

- **Dataset_Ids**: Identificadores de los datasets. Cada identificador representa un experimento o condición específica bajo la cual se identificaron los sitios de unión para el TF correspondiente.
- **TF_name**: Nombre del factor de transcripción que se une a la secuencia de ADN especificada.
- **Peak_start**: Posición inicial del pico de unión en el genoma.
- **Peak_end**: Posición final del pico de unión en el genoma.
- **Peak_center**: Posición central del pico de unión en el genoma.
- **Peak_number**: Número secuencial del pico, útil para referencias internas dentro del mismo conjunto de datos.
- **Max_Fold_Enrichment**: Enriquecimiento máximo observado en el pico.
- **Max_Norm_Fold_Enrichment**: Enriquecimiento máximo normalizado.
- **Proximal_genes**: Genes próximos al sitio de unión.
- **Center_position_type**: Tipo de posición central del pico (por ejemplo, intergénica, intrónica, etc.).

### Genoma Completo de E. coli
Disponible en formato FASTA.

Archivo: E_coli_K12_MG1655_U00096.3.txt

## Objetivos del Proyecto

### Generación de Archivos FASTA
Desarrollar un programa que extraiga y compile las secuencias de picos para cada TF en archivos individuales en formato FASTA. Cada archivo representará un regulador específico.

### Automatización del Análisis de Motivos
Crear un script que automatice la ejecución del software `meme` para cada archivo FASTA generado, facilitando la identificación de motivos en los sitios de unión.

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

## Colaboración y Recursos

El proyecto será colaborativo, trabajando conjuntamente con un investigador que dispone de un servidor preparado para ejecutar el programa `meme`. Se compartirán los siguientes recursos con el colaborador:
- Secuencias en formato FASTA de todos los TFs.
- Archivo `U00096.3.fna`.
- Script para la generación de archivos FASTA y la ejecución de `meme`.
- URL del repositorio de GitHub donde se aloja el proyecto y el código, facilitando el feedback y las contribuciones de todos los colaboradores.

## Buenas Prácticas de Desarrollo

Para asegurar la calidad y mantenibilidad del software, el proyecto seguirá estas buenas prácticas:

- **Control de Versiones**: Uso de Git para el control de versiones, asegurando una gestión eficaz de los cambios y la colaboración.
- **Revisión de Código**: Implementación de revisiones de código periódicas para mejorar la calidad del software y compartir conocimientos entre el equipo.
- **Documentación Exhaustiva**: Mantener una documentación completa tanto del código como de los procesos operativos, asegurando que cualquier nuevo colaborador pueda integrarse fácilmente.
- **Pruebas Automatizadas**: Desarrollo de pruebas automatizadas para validar la funcionalidad y robustez del software.

## Plan de Implementación

1. **Desarrollo del Extractor de Secuencias**: Programación de la tarea que consiste en genera los archivos FASTA a partir del archivo de picos. Como es un proceso automatizado, todos la información requerida para ejecutar los programas debe ser por línea de comandos.
2. **Automatización del Análisis con `meme`**: Scripting del proceso de ejecución del análisis de motivos para cada TF.
3. **Integración y Pruebas**: Combinación de los módulos desarrollados y realización de pruebas integrales para asegurar la funcionalidad.
4. **Despliegue y Capacitación**: Implementación del sistema en el servidor del colaborador y capacitación de usuarios sobre su uso.
