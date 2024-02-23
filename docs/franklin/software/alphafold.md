# :material-molecule: :material-dna: Alphafold

Franklin has a deployment of deepmind's [alphafold](https://github.com/google-deepmind/alphafold) as well as its databases compiled from source[^1].
The databases are located at `/share/databases/alphafold`; this directory is exported as `$ALPHAFOLD_DB_ROOT` when the module is loaded.

This is _not_ a docker deployment.
As such, many of the examples provided online need to be slightly modified.
The main script supplied by the alphafold package is `run_alphafold.py`, which is the script that the docker container calls internally.
All the same command line arguments that can be passed to alphafold's `run_docker.py` script can be passed to `run_alphafold.py`, but the latter requires all the database locations be supplied:

```bash
run_alphafold.py \
--data_dir="$ALPHAFOLD_DB_ROOT" \
--uniref90_database_path=$ALPHAFOLD_DB_ROOT/uniref90/uniref90.fasta \
--mgnify_database_path=$ALPHAFOLD_DB_ROOT/mgnify/mgy_clusters_2022_05.fa \
--template_mmcif_dir=$ALPHAFOLD_DB_ROOT/pdb_mmcif/mmcif_files \
--obsolete_pdbs_path=$ALPHAFOLD_DB_ROOT/pdb_mmcif/obsolete.dat \
--bfd_database_path=$ALPHAFOLD_DB_ROOT/bfd/bfd_metaclust_clu_complete_id30_c90_final_seq.sorted_opt \
--uniref30_database_path=$ALPHAFOLD_DB_ROOT/uniref30/UniRef30_2021_03 \
--pdb70_database_path=$ALPHAFOLD_DB_ROOT/pdb70/pdb70 \
[OTHER ARGS]
```

Because this is annoying, we have supplied a wrapper script named `alphafold-wrapped` with our module that passes these common options for you.
Any of the arguments not passed above will be passed along to the `run_alphafold.py` script; for example:

```bash
alphafold-wrapped \
--output_dir=[OUTPUTS] \
--fasta_paths=[FASTA INPUTS] \
--max_template_date=2021-11-01 \
--use_gpu_relax=true
```

[^1]: Jumper, J., Evans, R., Pritzel, A., Green, T., Figurnov, M., Ronneberger, O., … Hassabis, D. (2021). Highly accurate protein structure prediction with AlphaFold. Springer Science and Business Media LLC. [https://doi.org/10.1038/s41586-021-03819-2](https://doi.org/10.1038/s41586-021-03819-2)