# Rosenwald Benchmark

This repository provides annotation benchmark data for selected pages of the [**Rosenwald Guide**](https://gallica.bnf.fr/ark:/12148/cb344120051/date) (*Guide Rosenwald*), a historical French medical directory from the late 19th and early 20th centuries. The benchmark was created using the [Double Triangular Annotation Framework](https://github.com/nmrenyi/double-triangle-annotation).

## Overview

The Rosenwald Guide was a comprehensive directory of medical professionals practicing in France, including:
- Doctors of medicine and surgery (*Docteurs en médecine et en chirurgie*)
- Health officers (*Officiers de santé*)
- Dentists (*Chirurgiens-dentistes*)
- Women medical professionals

This benchmark contains **31 documents** (2,654 individual records) extracted from pages spanning **1887-1906**, plus one modern compilation (2025) of women medical professionals.

## Repository Structure

```
rosenwald-benchmark/
├── README.md                  # This file
├── combine_files.py          # Script to process raw exports
├── exports/                  # Raw export files (symlink)
│   └── *.tsv                # 64 paired files from annotation pipeline
└── rosenwald-benchmark/      # Processed benchmark data
    └── *.tsv                # 31 combined files (YYYY-NNNN.tsv)
```

## Data Format

Each TSV file in `rosenwald-benchmark/` contains structured data with 5 columns:

| Column | Description | Completeness |
|--------|-------------|--------------|
| **nom** | Name of medical professional | 100% |
| **année** | Year of graduation/certification | ~50-70% |
| **notes** | Professional titles and qualifications | ~20-40% |
| **adresse** | Practice address | 100% |
| **horaires** | Office hours | ~50-87% |

### Example Record

```tsv
nom             année   notes           adresse                 horaires
Bouchardat      1869    M A M AGR       boul St-Germain 108    
Bouchereau      1866    M H             Cabanis 1              
Bouchut         1843    AGR Mal des     Chaussée-d'Antin 38    1 à 3
                        enfants
```

### Common Abbreviations

**Titles/Qualifications (notes):**
- `AGR` - Agrégé (Professor)
- `M H` - Médecin des Hôpitaux (Hospital Physician)
- `M A M` - Membre de l'Académie de Médecine (Member of Academy of Medicine)
- `Ex-Int des Hôp` - Ex-Interne des Hôpitaux (Former Hospital Intern)
- `CH H` - Chirurgien des Hôpitaux (Hospital Surgeon)
- `Dent` - Dentiste (Dentist)
- `Mal des enfants` - Maladies des enfants (Pediatrics)

**Addresses:**
- `boul` - boulevard
- `av` - avenue
- `faub` - faubourg
- `pl` - place
- `q` - quai

**Hours:**
- `1 à 3` - 1 to 3 (o'clock)
- `Exc Dim` - Excepté Dimanche (Except Sunday)
- `Lun Mer Ven` - Lundi Mercredi Vendredi (Monday Wednesday Friday)
- `Mar Jeu Sam` - Mardi Jeudi Samedi (Tuesday Thursday Saturday)

## File Naming Convention

Files are named using the pattern `YYYY-NNNN.tsv`:
- `YYYY` - Publication year (1887-1906, or 2025 for modern compilation)
- `NNNN` - Page number from original document (e.g., 0029, 0198, 0501)

### Examples
- `1887-0029.tsv` - 1887 publication, page 29
- `1906-0501.tsv` - 1906 publication, page 501
- `2025-0101.tsv` - Modern compilation of women medical professionals

## Dataset Statistics

- **Total files:** 31
- **Total records:** 2,654 (excluding headers)
- **Unique names:** ~2,111 medical professionals
- **Time period:** 1887-1906
- **Geographic coverage:** Paris and French departments/colonies

### Document Categories

| Category | Count | Description |
|----------|-------|-------------|
| Paris doctors | 10 files | Docteurs en médecine et en chirurgie (Paris) |
| Provincial doctors | 20 files | Docteurs (départements et colonies) |
| Paris health officers | 4 files | Officiers de santé (Paris) |
| Provincial health officers | 16 files | Officiers de santé (départements et colonies) |
| Paris dentists | 4 files | Officiers de santé et dentistes (Paris) |
| Paris dental professionals | 6 files | Officiers de santé, chirurgiens-dentistes diplômés et dentistes |
| Women medical professionals | 2 files | Femmes médecins (modern compilation) |

## Usage

### Processing Raw Exports

**The exports/ folder could be found in this [link](https://github.com/nmrenyi/double-triangle-annotation/tree/main/site-ella-annoter/data/exports)**

The `combine_files.py` script processes raw annotation exports from the double-triangle annotation framework:

```bash
python combine_files.py
```

This script:
1. Reads paired files from `exports/` (files ending in `-1.tsv` and `-2.tsv`)
2. Extracts year-page identifiers from filenames
3. Combines paired files by removing duplicate headers
4. Outputs clean files to `rosenwald-benchmark/` with simplified naming

### Loading Data

**Python:**
```python
import pandas as pd

# Load a single document
df = pd.read_csv('rosenwald-benchmark/1887-0029.tsv', sep='\t')

# Load all documents
import glob
dfs = [pd.read_csv(f, sep='\t') for f in glob.glob('rosenwald-benchmark/*.tsv')]
all_data = pd.concat(dfs, ignore_index=True)
```

**R:**
```r
# Load a single document
data <- read.delim('rosenwald-benchmark/1887-0029.tsv', sep='\t')

# Load all documents
files <- list.files('rosenwald-benchmark', pattern='*.tsv', full.names=TRUE)
all_data <- do.call(rbind, lapply(files, read.delim, sep='\t'))
```

## Data Quality Notes

- **Empty fields:** Year, notes, and hours fields are frequently empty as this information was not always published in the original directory
- **Name variations:** Names may include titles (Mme, Mlle) for women professionals
- **Address abbreviations:** Historical French address abbreviations are preserved
- **Encoding:** Files are UTF-8 encoded to preserve French accented characters

## Source

This benchmark is derived from the **Guide Rosenwald**, a comprehensive medical directory published annually in France during the late 19th and early 20th centuries. The original pages were digitized and annotated using the Double Triangular Annotation Framework.

<!-- ## Citation

If you use this dataset in your research, please cite:

```bibtex
@dataset{rosenwald_benchmark,
  title={Rosenwald Benchmark: Historical French Medical Directory Dataset},
  author={Ren Yi},
  year={2026},
  url={https://github.com/nmrenyi/rosenwald-benchmark},
  note={Derived from Guide Rosenwald (1887-1906)}
}
```

## License

[Add license information here] -->

## Related Resources

- [Double Triangular Annotation Framework](https://github.com/nmrenyi/double-triangle-annotation)
- [Original Rosenwald Guide publications (1887-1906)](https://gallica.bnf.fr/ark:/12148/cb344120051/date)

## Contact

For questions or feedback about this benchmark:

**Ren Yi**  
Email: [renyi1006@gmail.com](mailto:renyi1006@gmail.com)

