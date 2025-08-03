#!/usr/bin/env python3

import os
import argparse

def generate_assembly_conf(clean_dir, output_file):
    sample_dirs = sorted([
        d for d in os.listdir(clean_dir)
        if os.path.isdir(os.path.join(clean_dir, d))
    ])

    with open(output_file, "w") as f:
        f.write("[samples]\n")
        for sample in sample_dirs:
            full_path = os.path.abspath(os.path.join(clean_dir, sample))
            f.write(f"{sample}:{full_path}/\n")

    print(f"✅ assembly.conf gerado com {len(sample_dirs)} amostras: {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Gerar arquivo assembly.conf para Phyluce")
    parser.add_argument("--clean_dir", required=True, help="Diretório com os diretórios das reads limpas")
    parser.add_argument("--output", required=True, help="Caminho de saída do arquivo assembly.conf")
    args = parser.parse_args()

    generate_assembly_conf(args.clean_dir, args.output)

