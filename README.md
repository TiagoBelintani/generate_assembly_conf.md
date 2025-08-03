
# generate_assembly_conf.py

This script creates an `assembly.conf` file compatible with **PHYLUCE**, listing sample names and paths to directories containing cleaned reads (after adapter trimming and quality filtering).

## Usage

```bash
python generate_assembly_conf.py --clean_dir /path/to/clean_reads --output /path/to/assembly.conf
```

##  Expected directory structure

The `--clean_dir` directory must contain subdirectories named after your samples. Each subdirectory should include the cleaned FASTQ files (e.g., after running `Trim Galore`):

```
clean_reads/
├── Mygalomorphae_001/
│   ├── sample1_val_1.fq.gz
│   └── sample1_val_2.fq.gz
├── Mygalomorphae_002/
│   ├── sample2_val_1.fq.gz
│   └── sample2_val_2.fq.gz
```

## 📝 Example output

The generated `assembly.conf` file will look like this:

```
[samples]
Mygalomorphae_001:/path/to/clean_reads/Mygalomorphae_001/
Mygalomorphae_002:/path/to/clean_reads/Mygalomorphae_002/
```

##  Author

Tiago Belintani  
Generated with love and Python

##  License

MIT
