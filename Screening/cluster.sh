#!/bin/bash

# Output directory
out_dir="/project/agsgpa/Achyutan"


# Full path to Python script
python_script="/home/madhusud/modeling_gene_expression/simulating_params.py"

# Logs with job ID
stdout_file="$out_dir/job_%J.log"
stderr_file="$out_dir/job_%J.err"

# Submit job
mxqsub --group-name "param_screening" \
       --runtime 1000 \
       --memory=30000 \
       --threads 1 \
       --stdout "$stdout_file" \
       --stderr "$stderr_file" \
       python3 "$python_script"
