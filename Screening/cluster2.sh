#!/bin/bash


out_dir="/project/agsgpa/Achyutan/modelB"
python_script="/home/madhusud/modeling_gene_expression/Screens/simulating_params_modelB.py"
param_file="/home/madhusud/modeling_gene_expression/Screens/three.txt" # master param file
lines_per_job=100  # how many lines per job (tune as needed)
group_name="param_screening_B"

# Split parameter file into chunks
out_prefix="$out_dir/params_chunk_"
split --numeric-suffixes --suffix-length=4 --lines=$lines_per_job "$param_file" "$out_prefix"

# Collect chunk files
chunk_files=${out_prefix}????   # expands to all split files

# ===== SUBMIT =====
for f in $chunk_files
do
    mxqsub --group-name "$group_name" \
           --runtime 1000 \
           --memory=30000 \
           --threads 1 \
           --stdout "$f.log" \
           --stderr "$f.err" \
           python3 "$python_script" "$f" "$f.out"
done

